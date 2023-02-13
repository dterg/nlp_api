# Config

This API simply loads a flair model (based on transformers) and serves it with an
endpoint. To configure which model (SequenceTagger) to use, define it in the config file.

# Running the API

When in the root directory (`nlp_api`), run:

`docker build -t nlp_api .`

Then run the image and forward the port:

`docker run -d -p 80:80 -t nlp_api`