FROM python:3.7

RUN pip install tweepy

WORKDIR /src
COPY . .

ENTRYPOINT ["python"]
CMD ["tweet.py"]