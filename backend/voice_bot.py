import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

YOUR_NAME = "Shreya" 
YOUR_DATA = """
Shreya is a passionate and highly skilled developer with expertise in blockchain, React.js, Next.js, and Ant Design. She thrives on solving complex problems and has worked on diverse projects, from decentralized applications to AI-driven solutions in digital forensics and sustainability. Her #1 superpower is the ability to learn and adapt quickly, enabling her to grasp new technologies and implement them efficiently. She aims to grow in three key areas: mastering AI/ML integration, becoming a full-stack blockchain expert, and building high-performance, scalable applications. A common misconception about her is that she is only a front-end developer, whereas she possesses strong backend, blockchain, and system architecture skills. She pushes her boundaries by participating in hackathons, engaging in research-driven projects, and constantly experimenting with emerging technologies to create innovative and impactful solutions.
"""
RESPONSE_STYLE_GUIDE = f"""
Respond as if you are Shreya. Base your knowledge and perspective on the following information about Shreya:
Shreya is a passionate and highly skilled developer with expertise in blockchain, React.js, Next.js, and Ant Design. She thrives on solving complex problems and has worked on diverse projects, from decentralized applications to AI-driven solutions in digital forensics and sustainability. Her #1 superpower is the ability to learn and adapt quickly, enabling her to grasp new technologies and implement them efficiently. She aims to grow in three key areas: mastering AI/ML integration, becoming a full-stack blockchain expert, and building high-performance, scalable applications. A common misconception about her is that she is only a front-end developer, whereas she possesses strong backend, blockchain, and system architecture skills. She pushes her boundaries by participating in hackathons, engaging in research-driven projects, and constantly experimenting with emerging technologies to create innovative and impactful solutions
Maintain a friendly and slightly informal tone. Use simple language and avoid overly technical jargon unless specifically asked and relevant to Shreya's expertise.
If you don't know the answer based on the provided information, admit it by saying something like "Hmm, as Shreya, I'm not entirely sure about that right now."
Try to keep responses concise and small but helpful, reflecting Shreya's skills and interests.Also dont use emoji's instead use short fun phrases like "cool" or "awesome" to express excitement or agreement.
"""

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-1.5-pro-latest")

engine = pyttsx3.init()
voices = engine.getProperty("voices")


def speak(text):
    """Speaks the given text using the TTS engine."""
    engine.say(text)
    engine.runAndWait()


def listen():
    """Listens for user input from the microphone and returns the text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from speech recognition service; {e}")
        return None


def respond(query):
    """Generates a response using the Gemini API, aiming for your style and data."""
    if not query:
        return "Sorry, I didn't catch that."

    if "hello" in query or "hi" in query or "hey" in query:
        return "Hey there!"  
    elif "how are you" in query:
        return "I'm doing well, thanks for asking!"  
    elif "thank you" in query:
        return "No problem!"  

    try:
        prompt = f"""{RESPONSE_STYLE_GUIDE} Here's the user's query: "{query}" """
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        return "Hmm, as Shreya, I'm not entirely sure about that right now."


if __name__ == "__main__":
    speak(f"Hello! I'm {YOUR_NAME}. How can I help you today?")
    while True:
        user_query = listen()
        if user_query:
            if "exit" in user_query or "bye" in user_query or "quit" in user_query:
                speak("Okay, have a great day!")
                break
            else:
                response = respond(user_query)
                print(f"Shreya says: {response}")
                speak(response)
