FROM python:3.10-alpine

WORKDIR /code

ENV FLASK_APP=app.python
ENV FLAS_RUN_HOST=0.0.0.0

RUN apk add --nocache gcc musl-dev linux-headers

COPY requirements.txt .

RUN pip install -r requirements

EXPOSE 5000

COPY . .

CMD ["flask", "run"]
