import speech_recognition as sr

class AudioToTextConverter:
    def __init__(self, audio_file):
        self.audio_file = audio_file

    def convert_to_text(self):
        recognizer = sr.Recognizer()

        # Load the audio file
        with sr.AudioFile(self.audio_file) as source:
            audio_data = recognizer.record(source)

        # Convert speech to text
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Usage example
    audio_converter = AudioToTextConverter("audio.wav")
    text = audio_converter.convert_to_text()
    print(text)