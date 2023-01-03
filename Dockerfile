FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get -y update \
    && apt-get install -y git wget cmake clang-10 llvm-10 lld-10 ninja-build libsdl2-dev libsdl2-mixer-dev freeglut3-dev automake libtool\
    && ln -s /usr/bin/llvm-ar-10 /usr/bin/llvm-ar \
    && ln -s /usr/bin/llvm-ranlib-10 /usr/bin/llvm-ranlib \
    && ln -s /usr/bin/lld-10 /usr/bin/lld \
    && ln -s /usr/bin/clang-10 /usr/bin/clang \
    && ln -s /usr/bin/clang++-10 /usr/bin/clang++ 