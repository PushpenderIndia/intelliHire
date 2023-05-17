import speech_recognition as sr
import pyttsx3
import openai
import pprint
from gtts import gTTS

class OpenAIInterview:
    def __init__(self, api_key, interview_id, output_directory):
        self.api_key = api_key
        self.openai = openai
        self.openai.api_key = self.api_key
        self.model_engine = "text-davinci-002"
        self.interview_id     = interview_id
        self.output_directory = output_directory + "/"

        # Initialize speech recognition engine
        self.recognizer = sr.Recognizer()

        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()

    def text_to_audio(self, text, output_file):
        # Create a gTTS object with the text and specify the language (e.g., 'en' for English)
        tts = gTTS(text=text, lang='en')

        # Save the audio to a file
        tts.save(output_file)

    def ask_first_question(self, job_role):
        prompt = f"As an HR interviewer, what is a good question to ask a candidate for the role of {job_role}?"
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=50,
            n=1,
            stop=None,
            temperature=0.7
        )

        hr_question = response.choices[0].text.strip()
        output_file_path = self.output_directory+f"response_{self.interview_id}.mp3"
        output_file_url  = f"/static/response_{self.interview_id}.mp3"
        self.text_to_audio(hr_question, output_file_path)
        return output_file_url, hr_question

    def rate_answer(self, answer, question):
        prompt = f"On a scale of 1 to 10, how would you rate the following answer to the question '{question}':\nAnswer: {answer}\n"
        completions = self.openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        rating_text = completions.choices[0].text.strip()
        rating = int(''.join(filter(str.isdigit, rating_text)))
        return rating

    def generate_follow_up_question(self, answer):
        prompt = f"Generate a follow-up question based on the following answer:\nAnswer: {answer}"
        completions = self.openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        message = completions.choices[0].text
        follow_up_question = message.strip()
        output_file_path = self.output_directory+f"response_{self.interview_id}.mp3"
        output_file_url  = f"/static/response_{self.interview_id}.mp3"
        self.text_to_audio(follow_up_question, output_file_path)
        return output_file_url, follow_up_question

if __name__ == "__main__":
    api_key = "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"

    interview_id = 10
    output_directory = ""
    interview = OpenAIInterview(api_key, interview_id, output_directory)
    job_role      = input("Enter the job role: ")
    num_questions = int(input("Enter the number of questions to be asked: "))

    # print(interview.ask_first_question(job_role))
    text = "Hello, how are you?"
    output_file = "output.mp3"
    interview.text_to_audio(text, output_file)

    #questions, answers, ratings = interview.generate_questions(job_role, num_questions)
    #pprint.pprint(interview.response)