# 🎙️ Jarvis — Custom Speech-to-Text to GPT AI Pipeline  

## 📌 Overview  
**Jarvis** is a **custom-built AI system** that captures speech, converts it into text using an AI-driven speech-to-text model powered by **Whisper (Python)**, and sends the recognized text to **OpenAI's GPT API via Node.js** to generate intelligent, contextual responses.  

The project is structured for future expansion with **Java (Gradle)**, where you can add custom GPT-powered functions as your needs grow.

---

## 🛠️ Requirements

### Global Requirements  
- **Python 3.10+**  
- **Node.js 18+**  
- **Java 17+**  
- **Gradle 8+**

---

## 🔐 `.env` Configuration  

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxxxxxx
```

This key is used in both **Node.js** and **Java** components.

---

## 🗂️ Project Structure

```
/jarvis
├── .env                       # API Key for OpenAI
├── src/
│   └── main/
│       ├── Speech.py           # Python Whisper-based Speech-to-Text
│       ├── apiCall/
│       │   └── callGPT.js      # Node.js GPT API Integration
│       └── java/               # Placeholder for future Java GPT Integration
├── stt_output.txt              # Text output from Speech.py
└── build.gradle / build.gradle.kts  # For Java (if needed)
```

---

## 🐍 Python: Custom Speech-to-Text (Whisper AI)

### Install Required Packages  
```bash
python3 -m venv venv
source venv/bin/activate
pip install openai-whisper sounddevice soundfile
```

### Run Speech-to-Text  
```bash
python3 src/main/Speech.py
```

✅ This records from your microphone, transcribes it using **OpenAI Whisper locally**, and writes the result to `stt_output.txt`.

---

## 🟢 Node.js: GPT API Integration

### Install Required Packages  
```bash
npm init -y
npm install dotenv openai
```

### Run GPT API Call  
```bash
node src/main/apiCall/callGPT.js
```

This reads `stt_output.txt` and sends it as a prompt to **GPT-3.5 or GPT-4**.

---

## ☕ Java + Gradle (For Future GPT Custom Functions)

### Purpose  
This directory is prepared for future GPT-related functionality written in **Java (Gradle)**.  
You can later build:
- Custom GPT pipelines
- Complex workflows
- Enterprise-grade AI integrations  

### Example `build.gradle.kts` (Kotlin DSL)
```kotlin
dependencies {
    implementation("com.theokanning.openai-gpt3-java:service:0.14.0")
    implementation("com.squareup.okhttp3:okhttp:4.9.3")
}
```

### Java GPT Example (Optional Future Usage)
```java
OpenAiService service = new OpenAiService(System.getenv("OPENAI_API_KEY"));
CompletionRequest completionRequest = CompletionRequest.builder()
    .prompt("Your transcribed speech here")
    .model("text-davinci-003")
    .maxTokens(100)
    .build();
System.out.println(service.createCompletion(completionRequest).getChoices().get(0).getText());
```

---

## 🚦 Commands Quick Reference

| Task               | Command                                      |
|--------------------|----------------------------------------------|
| Python Venv        | `source venv/bin/activate`                    |
| Install Python     | `pip install openai-whisper sounddevice soundfile` |
| Run STT            | `python3 src/main/Speech.py`                  |
| Node.js Init       | `npm init -y && npm install dotenv openai`    |
| Run GPT (Node)     | `node src/main/apiCall/callGPT.js`            |
| Java Build (Gradle)| `./gradlew build`                             |

---

## 🚀 Why This is Custom  
✅ Local AI transcription (Whisper) — **No SaaS STT dependency**  
✅ Modular GPT API use — **Easily portable between Node & Java**  
✅ `.env` powered — **No keys hardcoded**  
✅ Ready for **custom GPT functions in Java**  
