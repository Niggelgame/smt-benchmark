# Image including all necessary dependencies to run the application
FROM amd64/ubuntu:24.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    python3-meson \
    software-properties-common \
    unzip \
    ninja-build \
    wget

# Install build tool 
RUN pip install meson --break-system-packages

# Install Solvers
# Install Yices2
RUN cd /tmp && \
    wget https://yices.csl.sri.com/releases/2.6.5/yices-2.6.5-x86_64-pc-linux-gnu-static-gmp.tar.gz && \
    tar -xvf yices-2.6.5-x86_64-pc-linux-gnu-static-gmp.tar.gz && \
    mv yices-2.6.5/bin/yices /usr/local/bin/yices && \
    mv yices-2.6.5/bin/yices-smt2 /usr/local/bin/yices-smt2 && \
    rm -rf yices-2.6.5-x86_64-pc-linux-gnu-static-gmp.tar.gz yices-2.6.5

# Install CVC5
RUN cd /tmp && \
    wget https://github.com/cvc5/cvc5/releases/download/cvc5-1.2.0/cvc5-Linux-x86_64-static-gpl.zip && \
    unzip cvc5-Linux-x86_64-static-gpl.zip && \
    mv cvc5-Linux-x86_64-static-gpl/bin/cvc5 /usr/local/bin/cvc5 && \
    rm -rf cvc5-Linux-x86_64-static-gpl.zip cvc5-Linux-x86_64-static-gpl

# Install Bitwuzla
RUN cd /tmp && \
    wget https://github.com/bitwuzla/bitwuzla/archive/refs/tags/0.5.0.zip && \
    unzip 0.5.0.zip && \
    cd bitwuzla-0.5.0 && \
    ./configure.sh && \
    


