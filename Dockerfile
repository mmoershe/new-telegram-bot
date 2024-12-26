FROM python:3.13-slim

WORKDIR /usr/src/app

COPY . . 

RUN apt update && apt upgrade -y curl

RUN curl -fsSL https://ollama.com/install.sh | sh

# RUN ollama serve

RUN ollama --version

RUN ollama pull llama3.2

RUN pip install -r requirements.txt

CMD python -u main.py
