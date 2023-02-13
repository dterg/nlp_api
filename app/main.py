from flair.data import Sentence
from flair.models import SequenceTagger
from fastapi import FastAPI

from utils import jsonify_flair


app = FastAPI()

#TODO - define this in an env var along with dockerfile
tagger = SequenceTagger.load("flair/ner-english")


@app.get("/")
def predict(txt: str):
    sentence = Sentence(txt)
    tagger.predict(sentence)
    return list(jsonify_flair(sentence))


if __name__ == "__main__":
    predict('Test where Dieter is a name and Google is a company.')
