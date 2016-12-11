# Dockerfile to build and test DeepDive inside a container
#
# `make build-in-container test-in-container` uses master image built by this.
# `util/build/docker/` contains utilities relevant to this.
FROM debian
MAINTAINER deepdive-dev@googlegroups.com

# Install essential stuffs
RUN apt-get update && apt-get install -qy \
        coreutils \
        bash \
        curl \
        sudo \
        git \
        build-essential \
        postgresql-client \
        vim \
        python-pip \
        python-dev \
        wget \
        aptitude \
        nmap \
        build-essential \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Set up a non-superuser
ARG USER=wordsum
ENV USER=$USER
RUN adduser --disabled-password --gecos "" $USER \
 && adduser $USER adm \
 && bash -c "echo '%adm ALL=(ALL:ALL) NOPASSWD: ALL' | tee -a /etc/sudoers"
USER $USER

# Get a fresh clone of deepdive
ARG BRANCH=master
ENV BRANCH=$BRANCH
WORKDIR /deepdive
COPY .git .git
RUN sudo chown -R $USER .
RUN git checkout .

# Install deepdive build/runtime dependencies
RUN make depends \
 && sudo apt-get clean \
 && sudo rm -rf /var/lib/apt/lists/*

# Build deepdive
RUN make bundled-runtime-dependencies
RUN make

# ENV
ENV PATH /deepdive/dist/stage/bin/:$PATH
ENV PATH /usr/lib/postgresql/9.4/bin:$PATH
ENV PYTHONPATH /usr/local/lib/python2.7/dist-packages

# Install CoreNLP
RUN /deepdive/dist/stage/bin/deepdive corenlp install
