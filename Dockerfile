FROM python:3.9-slim

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app

ENTRYPOINT ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=80"]