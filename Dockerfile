FROM python:3.9.9-slim-buster

WORKDIR /de-challenge

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "/de-challenge/main.py"] 