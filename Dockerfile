FROM mcr.microsoft.com/playwright:v1.30.0-focal

WORKDIR /workspace
ADD . /workspace

RUN apt-get update && apt-get install -y python3-pip

RUN pip install --no-cache-dir -r requirements.txt



RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace



CMD python3 speech_app/crash_speech.py
