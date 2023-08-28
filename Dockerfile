FROM python:3.9-slim

# ENV DB_PASSWORD Password

COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY ./app /dapp/app
COPY ./bin /dapp/bin
COPY wsgi.py /dapp/wsgi.py
WORKDIR /dapp

RUN useradd flaskuser
USER flaskuser

EXPOSE 8080

ENTRYPOINT ["bash", "/dapp/bin/run.sh"]