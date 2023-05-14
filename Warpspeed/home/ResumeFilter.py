import openai
import pdfminer.high_level
import docx

class ResumeFilter:
    def __init__(self, resume_list, job_role, openai_key, additional_skills_list, top_n):
        self.resume_list            = resume_list
        self.job_role               = job_role
        openai.api_key              = openai_key

        self.additional_skills_list = []
        for skill in additional_skills_list:
            self.additional_skills_list.append(skill.lower())

        self.top_n                  = top_n

    def start(self):
        openai_skills = self.generate_skills()
        self.keyword_list = self.additional_skills_list + openai_skills

        matched_texts = []
        text_list     = []
        for resume_file in self.resume_list:
            try:
                if resume_file.split(".")[-1] == "docx":
                    text = self.docx_to_text(resume_file) 
                elif resume_file.split(".")[-1] == "pdf":
                    text = self.pdf_to_text(resume_file)

                text = text.lower()
                text_list.append(text)
                count = 0
                for keyword in self.keyword_list:
                    if keyword in text:
                        count += 1
                matched_texts.append(count)
            except Exception as e:
                print(f"Error [ResumeFilter]: {e}")

        top_matched_files = self.find_top_matched_applicants(matched_texts, text_list)
        return top_matched_files

    def generate_skills(self):
        prompt = f"List the top 10 skills required for a {self.job_role}"
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=prompt,
            temperature=0.5,
            max_tokens=100,
            n=1,
            stop=None,
        )

        raw_skills = response.choices[0].text.strip().split("\n")
        skills = []
        for skill in raw_skills:
            skills.append(skill.split(".")[-1].strip().lower())
        return skills  

    def pdf_to_text(self, pdf_path):
        with open(pdf_path, 'rb') as file:
            text = pdfminer.high_level.extract_text(file)
        return text

    def docx_to_text(self, docx_path):
        doc = docx.Document(docx_path)
        text = ""
        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"
        return text
    
    def find_top_matched_applicants(self, matched_texts, text_list):
        matched_files = [self.resume_list[i] for i in range(len(self.resume_list)) if matched_texts[i] > 0]
        matched_texts = [(text_list[i], matched_texts[i]) for i in range(len(text_list)) if matched_texts[i] > 0]

        matched_texts.sort(key=lambda x: x[1], reverse=True)
        top_matched_texts = [text[0] for text in matched_texts[:self.top_n]]
        top_matched_files = [matched_files[text_list.index(text)] for text in top_matched_texts]
        return top_matched_files

if __name__ == "__main__":
    # Example usage
    job_role   = "Data Scientist"
    openai_key = "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"
    additional_skills_list = ["Python", "django"]
    resume_list = ["Divya.pdf", "Neha.pdf"]
    top_n = 1

    print(f"Job Role: {job_role}")
    generator = ResumeFilter(resume_list, job_role, openai_key, additional_skills_list, top_n)
    top_matched_files = generator.start()
    print(top_matched_files)

