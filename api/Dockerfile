FROM python:3.10.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first (https://dockertraining.readthedocs.io/en/latest/django/)
ENV PYTHONUNBUFFERED 1

WORKDIR /api_workdir

COPY requirements/dev.txt .
COPY makefile .

RUN make build-docker

COPY ./ .

EXPOSE 8000

CMD ["python3", "verdantech_api/manage.py", "runserver", "--settings=verdantech_api.settings.development"]
