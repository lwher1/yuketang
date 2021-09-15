FROM python:3.6.4

RUN mkdir /app

copy *.py  requirements.txt  rsa_public_key.pem /app/

WORKDIR /app

RUN pip install -r  requirements.txt

CMD ["python","main.py"]
