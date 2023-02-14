FROM python:3.9.10-slim

COPY . DiscordAPI/

WORKDIR DiscordAPI
RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "main.py"]