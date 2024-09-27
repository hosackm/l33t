FROM golang:1.23.1

WORKDIR /root

# RUN apk update && apk add build-base cmake wget git tar ninja pkgconfig xz
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt-get install -y build-essential cmake wget git tar ninja-build pkg-config xz-utils libcriterion-dev glibc-source
# RUN wget https://github.com/Snaipe/Criterion/releases/download/v2.4.2/criterion-2.4.2-linux-x86_64.tar.xz -O criterion-2.4.2-linux-x86_64.tar.xz && \
#     tar -xvf criterion-2.4.2-linux-x86_64.tar.xz && \
#     cp -r criterion-2.4.2/include /usr/local/include && \
#     cp -r criterion-2.4.2/lib /usr/local/lib

COPY CMakeLists.txt /root/
COPY go.mod /root/
COPY go.sum /root/
COPY requirements.txt /root/
COPY problems /root/problems

COPY cmake/FindCriterion.cmake /usr/share/cmake/Modules/
RUN mkdir -p build && cd build && cmake .. -G Ninja && ninja
