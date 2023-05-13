import openai
import json5
import pprint 

class QuizGenerator:
    def __init__(self, job_role, num_questions, openai_key):
        openai.api_key = openai_key
        self.job_role = job_role
        self.num_questions = num_questions
        self.prompt = f"Generate a MCQ quiz of {self.num_questions} questions for \"{self.job_role}\", give output in json format, where questions are the keys and there value is a list of options. e.g. "+ "{'question 1?': ['optionA','optionB','optionC','optionD']}"

    def generate_quiz(self):
        questions = {}
        questions = self._get_response()
        return questions

    def _get_response(self):
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt=self.prompt,
            max_tokens=2048,
            n=1,
            stop=None,
            temperature=0.5,
        )

        output_text = response.choices[0].text
        json_obj = json5.loads(output_text)
        return json_obj
    
if __name__ == "__main__":
    job_role = "data scientist"
    num_questions = 5
    openai_key = "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"
    print(f"Job Role: {job_role} [Ques No: {num_questions}]")

    quiz_generator = QuizGenerator(job_role, num_questions, openai_key)
    questions = quiz_generator.generate_quiz()
    pprint.pprint(questions)