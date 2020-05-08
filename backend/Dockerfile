# pull official base image
FROM python:3.7-slim-buster

# set work directory
WORKDIR /usr/src/backend

# set environment variables
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1



# RUN apk update
# RUN pip install --upgrade pip
# RUN apk add --virtual build-deps gcc postgresql-dev  python3-dev musl-dev
# RUN apk add postgresql-dev
# RUN apk add jpeg-dev zlib-dev libjpeg
# RUN pip install Pillow
# RUN pip install psycopg2
# RUN apk del build-deps

# install dependencies
COPY ./requirements.txt /usr/src/backend/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
# COPY ./entrypoint.sh /usr/src/backend/entrypoint.sh

# copy project
COPY . /usr/src/backend/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/backend/entrypoint.sh"]