# Dockerfile
FROM python:3.9.5-slim 

WORKDIR /usr/src/app/app

COPY . .

RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2
RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 5000

CMD ["python", "run.py"] 