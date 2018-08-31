FROM ubuntu:18.04

# Install some packages.
RUN apt-get update && apt-get install -y --no-install-recommends \
  python3-minimal python3-setuptools python3-pip && pip3 install qiskit && \
  rm -f /usr/bin/python && ln -s /usr/bin/python3 /usr/bin/python && \
  rm -f /usr/bin/pip && ln -s /usr/bin/pip3 /usr/bin/pip

WORKDIR /data

# Just to keep it running.
CMD tail -f /dev/null
