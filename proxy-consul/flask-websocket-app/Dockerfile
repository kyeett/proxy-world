FROM python:3.6

MAINTAINER Magnus Wahlstrand "magnus.wahlstrand@gmail.com"

COPY app.py /app/
COPY nginx.conf /app
COPY requirements.txt /app/
ADD templates /app/templates

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]