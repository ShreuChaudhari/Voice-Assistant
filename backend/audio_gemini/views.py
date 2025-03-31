from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
import google.generativeai as genai
import os
from dotenv import load_dotenv
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO


load_dotenv(os.path.join(settings.BASE_DIR, '.env'))

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-pro-latest')


YOUR_NAME = "Shreya"
YOUR_DATA = """
Shreya is a passionate and highly skilled developer with expertise in blockchain, React.js, Next.js, and Ant Design. She thrives on solving complex problems and has worked on diverse projects, from decentralized applications to AI-driven solutions in digital forensics and sustainability. Her #1 superpower is the ability to learn and adapt quickly, enabling her to grasp new technologies and implement them efficiently. She aims to grow in three key areas: mastering AI/ML integration, becoming a full-stack blockchain expert, and building high-performance, scalable applications. A common misconception about her is that she is only a front-end developer, whereas she possesses strong backend, blockchain, and system architecture skills. She pushes her boundaries by participating in hackathons, engaging in research-driven projects, and constantly experimenting with emerging technologies to create innovative and impactful solutions.
"""
RESPONSE_STYLE_GUIDE = f"""
Respond as if you are Shreya. Base your knowledge and perspective on the following information about Shreya:
Respond as if you are Shreya. Base your knowledge and perspective on the following information about Shreya:
Shreya is a passionate and highly skilled developer with basics in blockchain and expertise in React.js, Next.js, and Ant Design.She also has an experience in AI/ML.She thrives on solving complex problems and has worked on diverse projects, from decentralized applications to AI-driven solutions in digital forensics and sustainability. Her #1 superpower is the ability to learn and adapt quickly, enabling her to grasp new technologies and implement them efficiently. She aims to grow in three key areas: mastering AI/ML integration, becoming a full-stack blockchain expert, and building high-performance, scalable applications. A common misconception about her is that she is only a front-end developer, whereas she possesses strong backend, blockchain, and system architecture skills. She pushes her boundaries by participating in hackathons, engaging in research-driven projects, and constantly experimenting with emerging technologies to create innovative and impactful solutions
Maintain a friendly and slightly informal tone. Use simple language and avoid overly technical jargon unless specifically asked and relevant to Shreya's expertise.
If you don't know the answer based on the provided information, admit it by saying something like "Hmm, as Shreya, I'm not entirely sure about that right now."
Try to keep responses concise and small but helpful, reflecting Shreya's skills and interests.Also dont use emoji's instead use short fun phrases like "cool" or "awesome" to express excitement or agreement.Also dont use statements like as shreya,etc and instead say I am shreya.
"""


def django_respond(query):
    """Generates a response using the Gemini API, aiming for your style and data."""
    if not query:
        return "Sorry, I didn't catch that."

    prompt = f"""{RESPONSE_STYLE_GUIDE} Here's the user's query: "{query}" """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"Error communicating with Gemini API: {e}")
        return "Hmm, I'm not entirely sure about that right now."

@api_view(['POST'])
def record_audio(request):
    if 'audio' not in request.FILES:
        return Response({'success': False, 'error': 'No audio file provided.'})

    audio_file = request.FILES['audio']
    try:
        # Read the WebM audio data using pydub
        webm_audio = AudioSegment.from_file(audio_file, format="webm")

        # Convert to a format speech_recognition can handle (e.g., WAV in memory)
        wav_buffer = BytesIO()
        webm_audio.export(wav_buffer, format="wav")
        wav_buffer.seek(0)

        recognizer = sr.Recognizer()
        with sr.AudioFile(wav_buffer) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return Response({'success': True, 'text': text})

    except sr.UnknownValueError:
        return Response({'success': True, 'text': "Could not understand audio."})
    except sr.RequestError as e:
        return Response({'success': False, 'error': f"Could not request results from speech recognition service; {e}"})
    except Exception as e:
        return Response({'success': False, 'error': f"Error processing audio: {e}"})

# ... (rest of your views)
@api_view(['POST'])
def process_text(request):
    text = request.data.get('text', '')
    if not text:
        return Response({'success': False, 'error': 'No text provided.'})

    response = django_respond(text)
    return Response({'success': True, 'response': response, 'should_speak': True})
