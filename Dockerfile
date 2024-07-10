FROM python:3.9.12-alpine3.15

EXPOSE 5000

WORKDIR /app
COPY . .

COPY requirements.txt .

RUN pip install -r requirements.txt

CMD [ "python", "wsgi.py" ]