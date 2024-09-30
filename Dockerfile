FROM golang:1.23.1

WORKDIR /root

COPY . .

ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && apt-get install -y build-essential cmake \
    wget git tar ninja-build pkg-config xz-utils libcriterion-dev \
    libbison-dev libigraph-dev gdb python3 python3-pip

RUN wget https://ziglang.org/download/0.13.0/zig-linux-x86_64-0.13.0.tar.xz -O /root/zig-linux-x86_64-0.13.0.tar.xz &&\
    tar -xvf /root/zig-linux-x86_64-0.13.0.tar.xz &&\
    ln -s /root/zig-linux-x86_64-0.13.0/zig /usr/local/bin

RUN pip install -r requirements.txt --break-system-packages

RUN go mod download

RUN zig build

CMD ["python3", "build_and_test.py"]
