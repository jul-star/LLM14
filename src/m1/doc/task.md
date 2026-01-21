1. 
Steps:
*   **Get your OpenAI Key:** Sign up or log in at [platform.openai.com](https://platform.openai.com/) and find your API key section.
*   **Create a `.env` file:** In the same folder as this notebook, create a new text file and name it exactly `.env` (starting with a dot, no name before it).
*   **Add key to `.env`:** Open the `.env` file and add your key like this (replace the dummy text with your real keys):

```dotenv
OPENAI_API_KEY=sk-YourSecretOpenAIKeyGoesHereXXXXXXXXXXXXX
```
Now, let's write Python code to load these keys from the `.env` file without actually typing the keys into our script.