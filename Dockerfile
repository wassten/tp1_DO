FROM python:3.8-buster

WORKDIR /tp1

RUN pip install --no-cache-dir requests==2.25.1

COPY tp1.py .

CMD ["python", "tp1.py"]