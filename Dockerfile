FROM python:3.8-buster

WORKDIR /tp1

RUN pip install --no-cache-dir requests==2.25.1

COPY tp1.py .

ENTRYPOINT ["streamlit", "run"]

CMD ["tp1.py"]