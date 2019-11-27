
FROM kennethreitz/pipenv

WORKDIR /app

COPY . /app/

RUN pipenv install --deploy --system

env GOOGLE_APPLICATION_CREDENTIALS=/app/helloeveryone/credentials.json

CMD ["python3", "/app/helloeveryone/translate.py"]
