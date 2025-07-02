# Image including all necessary dependencies to run the application
FROM amd64/ubuntu:24.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    python3-pip \
    software-properties-common \
    unzip \
    ninja-build \
    wget \
    m4 \
    git

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
    wget https://github.com/bitwuzla/bitwuzla/archive/refs/tags/0.8.0.zip && \
    unzip 0.8.0.zip && \
    cd bitwuzla-0.8.0 && \
    ./configure.py && \
    cd build && ninja install

# Copy the test application into the image
COPY . /app

WORKDIR /app

# Create a virtual environment and install the application dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt --break-system-packages


# Run tests: LOG_LEVEL=5 TIMEOUT=10s KEEP_TEMP=True CVC5_PATH=cvc5 python3 test_runner.py
