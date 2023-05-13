import openai
import json

class QuizGenerator:
    def __init__(self, job_role, num_questions, openai_key):
        openai.api_key = openai_key
        self.job_role = job_role
        self.num_questions = num_questions

    def generate_quiz(self):
        questions = {}
        questions = self._get_response()
        return questions

    def _get_response(self):
        response = openai.Completion.create(
            engine="davinci",
            prompt=f"Generate a quiz for \"{self.job_role}\" with {self.num_questions} questions in json format, where the question is the key and the value is a list of options.",
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.7,
        )

        print(response.choices[0].text)
        return json.loads(response.choices[0].text)
    
if __name__ == "__main__":
    job_role = "data scientist"
    num_questions = 5
    openai_key = "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"
    print(f"Job Role: {job_role} [Ques No: {num_questions}]")

    quiz_generator = QuizGenerator(job_role, num_questions, openai_key)
    questions = quiz_generator.generate_quiz()

    print(questions)