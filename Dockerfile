FROM python:alpine

LABEL authors="Timur"

ENV PYTHONUNBUFFRED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "get_value.py"]