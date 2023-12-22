FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -U pip && pip install -r requirements.txt

COPY ./app /app/app
COPY ./bin /app/bin
COPY wsgi.py /app/wsgi.py
WORKDIR /app

RUN useradd app-user
USER app-user

EXPOSE 8000

ENTRYPOINT ["bash", "/app/bin/run.sh"]

