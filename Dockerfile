FROM python:3.8

COPY app.py test_app.py random_words.py words_alpha.txt requirements.txt ./

RUN pip3 install -r requirements.txt