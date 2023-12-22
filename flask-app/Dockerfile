FROM python:3.9-slim

COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY ./app /app/app
COPY wsgi.py /app/wsgi.py
WORKDIR /app

RUN useradd app-user
USER app-user

EXPOSE 8000

ENTRYPOINT ["gunicorn", "wsgi:application", "--bind", "0.0.0.0:8000", "--log-level=debug", "--workers=4"]
