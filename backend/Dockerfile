FROM python:3.12

WORKDIR /workdir

COPY ./requirements ./requirements

# Install backend dependencies
COPY ./requirements ./requirements
RUN pip install --upgrade pip && \
    pip install uv && \
    uv pip install --system -r ./requirements/dev.txt