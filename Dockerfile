FROM python:3.12

WORKDIR /workdir

COPY ./requirements ./requirements

#  Update pip tooling
RUN pip install --upgrade pip pip-tools wheel
# Install dependencies
RUN pip-sync requirements/dev.txt
