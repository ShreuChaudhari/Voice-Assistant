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

## Environment Variables

Ensure you have the following environment variables configured in both your local `.env` file (for development) and in your Render.io and Vercel deployment settings:

**Backend (`.env` and Render.io):**

* `SECRET_KEY`: Your Django secret key.
* `GEMINI_API_KEY`: Your API key for the Gemini language model (if you are using it).
* `FRONTEND_URL`: The URL of your deployed frontend application (e.g., `https://your-vercel-app.com`).

**Frontend (Vercel - if needed):**

* Any frontend-specific API keys or configuration variables.

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

## Contributing

[Add your contributing guidelines here if you plan to allow contributions.]

## License



