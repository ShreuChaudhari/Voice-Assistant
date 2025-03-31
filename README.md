# Voice Assistant 

***Deployed Link*** : https://voice-assistant-zeta-ten.vercel.app/

*Imagine having a voice assistant that sounds just like me! This web app, which works great on any phone or computer, learns how I talk. So when you ask it something, it'll respond in my own words and even use information from my personal notes and chats to give you really specific answers – it's like having a digital version of me ready to help.*

## Overview

The project consists of two main parts:

* **Frontend:** A React web application that provides the user interface for recording audio and displaying the conversation.
* **Backend:** A Django REST Framework API that receives audio recordings, processes them (e.g., transcribes the audio), and potentially interacts with a language model to generate responses.

## Technologies Used

**Frontend:**

* React
* Axios (for making HTTP requests)
* `useRef`, `useState` (React Hooks)
* Web API (`mediaDevices`, `MediaRecorder`, `SpeechSynthesisUtterance`)

**Backend:**

* Python
* Django
* Django REST Framework (DRF)
* `python-dotenv` (for managing environment variables)
* `django-cors-headers` (for handling Cross-Origin Resource Sharing)
* Potentially: Google Cloud AI Platform (Vertex AI) or the `google-generativeai` library for interacting with Gemini.

Setup and Installation (Local Development)
Clone the repository:

Bash

git clone <your_repository_url>
cd <your_project_directory>
Navigate to the backend directory:

Bash

cd backend
Create a virtual environment (recommended):

Bash

python -m venv venv
source venv/bin/activate  # On Linux/macOS
venv\Scripts\activate  # On Windows
Install backend dependencies:

Bash

pip install -r requirements.txt
Create a .env file in the backend directory and add your environment variables:

SECRET_KEY=your_django_secret_key
GEMINI_API_KEY=your_gemini_api_key
FRONTEND_URL=http://localhost:5173 # Default frontend development URL
# Add other backend environment variables as needed
Make and apply backend migrations:

Bash

python manage.py makemigrations
python manage.py migrate
Run the backend development server:

Bash

python manage.py runserver 0.0.0.0:8000
(The backend will be accessible at http://localhost:8000/ by default)

Open a new terminal and navigate to the frontend directory:

Bash

cd ../frontend
Install frontend dependencies:

Bash

npm install  # or yarn install
Start the frontend development server:

Bash

npm run dev  # or yarn dev - adjust based on your frontend script
(The frontend will usually be accessible at http://localhost:5173/)

Set the backend API URL: In your frontend code (e.g., app.jsx), ensure that the axios.post requests are pointing to your local backend development server URL (e.g., http://localhost:8000/api/record/).

## CORS Configuration

The backend is configured to allow requests from the specified origins in the `CORS_ALLOWED_ORIGINS` setting in `src/settings.py`. Make sure your frontend's URL is included in this list.

## Further Development

Possible areas for further development include:

* Implementing actual audio transcription on the backend.
* Integrating with the Gemini language model for generating intelligent responses.
* Adding user authentication.
* Improving the user interface and user experience.
* Adding support for different audio formats.
* Implementing more robust error handling.


## License



