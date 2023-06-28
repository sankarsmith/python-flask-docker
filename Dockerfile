FROM python:3.11-alpine
LABEL maintainer="lorenz.vanthillo@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --root-user-action=ignore
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
EXPOSE 8080
ENTRYPOINT ["python"]
CMD ["src/app.py"]
