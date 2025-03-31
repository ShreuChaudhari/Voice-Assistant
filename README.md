# Voice Assistant Project

This project is a simple voice assistant that allows users to record audio and have it processed by a backend, potentially using a large language model like Gemini.

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

## Setup and Installation

### Backend (Django - Render.io Deployment)

1.  **Clone the repository:**
    ```bash
    git clone <your_backend_repository_url>
    cd <your_backend_directory>
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file in the project's root directory** and add your environment variables:
    ```
    SECRET_KEY=your_django_secret_key
    GEMINI_API_KEY=your_gemini_api_key
    # Add other environment variables as needed
    ```

5.  **Make migrations and apply them:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Create a superuser (optional, for Django Admin):**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Deployment to Render.io:**
    * Push your code to a Git repository (e.g., GitHub, GitLab, Bitbucket).
    * Create a new Web Service on Render.io and connect it to your repository.
    * **Build Command:** `pip install -r requirements.txt`
    * **Start Command:** `gunicorn src.wsgi:application`
    * **Environment Variables:** Add your `SECRET_KEY`, `GEMINI_API_KEY`, and `FRONTEND_URL` (set to your Vercel app URL) in the Render.io dashboard.
    * Ensure your CORS settings in `src/settings.py` are correctly configured to allow requests from your frontend.

### Frontend (React - Vercel Deployment)

1.  **Clone the repository:**
    ```bash
    git clone <your_frontend_repository_url>
    cd <your_frontend_directory>
    ```

2.  **Install dependencies:**
    ```bash
    npm install  # or yarn install
    ```

3.  **Set the backend API URL:** In your frontend code (e.g., `app.jsx`), ensure that the `axios.post` requests are pointing to the correct URL of your deployed Django backend on Render.io (e.g., `https://your-app-name.onrender.com/api/record/`).

4.  **Deployment to Vercel:**
    * Push your code to a Git repository.
    * Create a new project on Vercel and connect it to your repository.
    * Vercel should automatically detect it as a Next.js or React project and configure the build settings.
    * Ensure that any necessary environment variables for your frontend are set in the Vercel dashboard.

## Usage

1.  Open the URL of your deployed frontend application in a web browser.
2.  Click the "Start Recording" button to begin recording audio using your microphone (you might be prompted for microphone access).
3.  Speak into your microphone.
4.  Click the "Stop Recording" button to end the recording.
5.  The frontend will send the audio data to your backend API for processing.
6.  The conversation, including your transcribed text and the AI's responses, will be displayed in the conversation area.
7.  If the backend is configured for text-to-speech, the AI's responses might also be spoken aloud.

## Project Structure
