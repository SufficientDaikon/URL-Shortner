#syntax=docker/dockerfile:1

FROM python:3.8-slim

WORKDIR /app

COPY /requirements.txt ./

RUN pip install  -r requirements.txt

COPY . .

EXPOSE 80 3306 5000

CMD [ "python3", "app.py", "-m" , "flask", "run", "--host=0.0.0.0"]
