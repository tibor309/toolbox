FROM python:3.11.6-slim-bookworm

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt install gcc -y

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "main.py"]