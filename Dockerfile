
FROM python:3.10-bullseye

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pipenv
RUN pip install pipenv

COPY Pipfile Pipfile.lock /code/
COPY . /code/

WORKDIR /code

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list 
RUN apt-get update
RUN ACCEPT_EULA=Y apt-get -y install msodbcsql17 \
    unixodbc \
    unixodbc-dev \
    tdsodbc \
    freetds-common \ 
    freetds-bin \ 
    freetds-dev

RUN adduser --disabled-password --no-create-home admin && chown -R admin:admin /code
RUN pipenv run pip install --upgrade setuptools
RUN pipenv install --system --deploy

USER admin