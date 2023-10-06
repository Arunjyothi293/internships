import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Function to convert speech to text
def speech_to_text():
    with sr.Microphone() as source:
        print("Please speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand your speech."
        except sr.RequestError as e:
            return f"Sorry, there was an error with the speech recognition service: {e}"

# Main program
if __name__ == "__main__":
    result = speech_to_text()
    print(f"You said: {result}")
