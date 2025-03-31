import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL;

export const transcribeAudio = async (audioBlob) => {
    const formData = new FormData();
    formData.append("audio", audioBlob, "recording.webm");

    try {
        const response = await axios.post(`${API_URL}`, formData, {
            headers: { 'Content-Type': 'multipart/form-data' }
        });

        return response.data;
    } catch (error) {
        console.error("Error transcribing audio:", error);
        throw new Error('Failed to transcribe audio');
    }
};

export const processText = async (text) => {
    try {
        const response = await axios.post(`${API_URL}`, { text });
        return response.data;
    } catch (error) {
        console.error("Error processing text:", error);
        throw new Error('Failed to process text');
    }
};
