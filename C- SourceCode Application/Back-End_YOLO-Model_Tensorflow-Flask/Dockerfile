FROM python:3.6-slim
COPY requirements.txt /deploy
COPY ./deploy /deploy

WORKDIR /deploy/

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

EXPOSE 80
ENTRYPOINT ["python", "object.py"]