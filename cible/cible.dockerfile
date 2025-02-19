FROM ubuntu:20.04
WORKDIR /app
RUN apt update && apt install -y evince curl
COPY malicious.pdf .
CMD evince malicious.pdf
