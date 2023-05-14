import speech_recognition as sr
import pyttsx3
import openai
import pprint

class OpenAIInterview:
    def __init__(self, api_key):
        self.api_key = api_key
        self.openai = openai
        self.openai.api_key = self.api_key
        self.model_engine = "text-davinci-002"
        self.response = {}

        # Initialize speech recognition engine
        self.recognizer = sr.Recognizer()

        # Initialize text-to-speech engine
        self.tts_engine = pyttsx3.init()

    def speak(self, text):
        self.tts_engine.say(text)
        self.tts_engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)

        try:
            print("Recognizing...")
            text = self.recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
            return ""
        except sr.RequestError:
            print("Sorry, I'm having trouble accessing the speech recognition service.")
            return ""

    def generate_questions(self, job_role, num_questions):
        prompt = f"Generate {num_questions} interview questions for a {job_role} position."
        completions = self.openai.Completion.create(
            engine=self.model_engine,
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        questions = completions.choices[0].text.strip().split("\n")
        questions = questions[:num_questions]
        answers = []
        ratings = []

        for i, question in enumerate(questions):
            self.response[question] = {'answer': '', 'rating': ''}
            self.speak(f"Question {i+1}: {question}")
            print(f"Q{i+1}. {question}")

            self.speak("Please provide your answer.")
            answer = self.listen()
            self.response[question]['answer'] = answer

            rating = self.rate_answer(answer, question)
            self.response[question]['rating'] = rating

            answers.append(answer)
            ratings.append(rating)

            print(f"Rating for your answer to Q{i+1}: {rating}/10")

            if i < len(questions) - 1:
                follow_up_question = self.generate_follow_up_question(answer)
                self.speak(f"Follow-up question: {follow_up_question}")
                print(f"Follow-up: {follow_up_question}")

                self.speak("Please provide your answer.")
                follow_up_answer = self.listen()

                follow_up_rating = self.rate_answer(follow_up_answer, follow_up_question)
                self.response[follow_up_question] = {'answer': follow_up_answer, 'rating': follow_up_rating}
                answers.append(follow_up_answer)
                ratings.append(follow_up_rating)

                print(f"Rating for your answer to the follow-up for Q{i+1}: {follow_up_rating}/10")

        return questions, answers, ratings



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
        rating = str(completions.choices[0].text.strip())
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
        return follow_up_question

if __name__ == "__main__":
    api_key = "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"
    interview = OpenAIInterview(api_key)
    job_role = input("Enter the job role: ")
    num_questions = int(input("Enter the number of questions to be asked: "))
    questions, answers, ratings = interview.generate_questions(job_role, num_questions)
    pprint.pprint(interview.response)