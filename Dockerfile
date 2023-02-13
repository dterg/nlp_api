FROM python:3.8-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y unixodbc-dev gcc g++
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

RUN pip freeze

RUN python -c 'from flair.models import SequenceTagger; SequenceTagger.load("flair/ner-english")'

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]