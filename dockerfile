FROM ubuntu:latest

LABEL maintainer="codekakitai51 <codekakitai51@gmail.com>"
LABEL version="1.0"
LABEL description="Converting markdown to html with python3-markdown"

RUN apt update && apt install -y \
    python3 \
    python3-pip \
    python3-markdown \
    && apt-get clean

WORKDIR /root/convert-project

COPY . /root/convert-project

CMD ["bash"]
