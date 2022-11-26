FROM  python:3.9.6-slim-buster

WORKDIR /seeker

COPY database.json /seeker
COPY requirements.txt /seeker

RUN pip install bs4
RUN pip install wikipedia
RUN pip install -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8000
COPY . .
CMD ["flask", "run"]