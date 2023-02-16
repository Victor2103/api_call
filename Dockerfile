FROM python:3.8

WORKDIR /workspace
ADD . /workspace

RUN pip install --no-cache-dir -r requirements.txt



RUN chown -R 42420:42420 /workspace
ENV HOME=/workspace



CMD playwright install && playwright install-deps && python3 speech_app/crash_speech.py
