FROM ubuntu:18.04

WORKDIR /tmp
RUN apt-get update \
    && apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get update \
    && apt-get install -y python3.8 python3.8-dev python3-pip openssl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 1

RUN python3 --version

RUN openssl version

WORKDIR /data

COPY . .

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install -i https://mirror.baidu.com/pypi/simple/ -r requirements.txt

CMD ["python3", "chinese_segment_service.py" ]

