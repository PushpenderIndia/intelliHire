import openai
import json5
import pprint 
import requests
import json

class QuizGeneratorAI:
    def __init__(self, job_role, num_questions, openai_key):
        openai.api_key = openai_key
        self.job_role = job_role
        self.num_questions = num_questions
        self.prompt = f"Generate a MCQ quiz of {self.num_questions} questions for \"{self.job_role}\", give output in json format, where questions are the keys and there value is a dictionary which contains 'options' & 'answer' key, 'options' key value should be list of options & 'answer' value should be correct option. e.g. "+ "{'this is test ques?': {'option':['optionA','optionB','optionC','optionD'], 'answer': 'optionA'}, 'this is test ques2?': {'option':['optionA','optionB','optionC','optionD'], 'answer': 'optionD'}}"
        print("Prompt:", self.prompt)

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
        print(output_text)
        final_output_text = ""
        index = 1
        if ("1." in output_text or "2. " in output_text) and "{\"1. " not in output_text:
            for line in output_text.split("\n"):
                if f"{index}. " not in line:
                    final_output_text += line + "\n"
                index += 1
        print("Output: ", final_output_text)
        json_obj = json5.loads(final_output_text)
        return json_obj


if __name__ == "__main__":
    job_role = "data scientist"
    num_questions = 5
    openai_key = "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"
    print(f"Job Role: {job_role} [Ques No: {num_questions}]")

    quiz_generator = QuizGeneratorAI(job_role, num_questions, openai_key)
    questions = quiz_generator.generate_quiz()
    pprint.pprint(questions)