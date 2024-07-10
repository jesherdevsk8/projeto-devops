FROM python:3.9.12-alpine3.15

EXPOSE 5000

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY wsgi.py .
COPY config.py .
COPY conftest.py .
COPY application application
COPY tests tests

CMD [ "python", "wsgi.py" ]