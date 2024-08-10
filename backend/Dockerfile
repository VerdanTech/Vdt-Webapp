FROM python:3.12

WORKDIR /workdir

COPY ./requirements ./requirements

#  Update pip tooling
RUN pip install --upgrade pip

# Install package manager
RUN pip install uv

# Install dependencies
RUN uv pip install --system -r requirements/dev.txt

#CMD ["litestar", "run"]
