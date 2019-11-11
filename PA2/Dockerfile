FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-minimal golang-go python3-flask
COPY . /PA2
WORKDIR /PA2
ENTRYPOINT ["python"]
CMD ["autograde.py"]
