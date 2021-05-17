FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

WORKDIR /app

COPY ./app ./app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--reload", "--host=0.0.0.0"]