# pull official base image
# good practice to use Alpine images when possible
FROM python:3.8.0-alpine

# set working directory
WORKDIR /usr/src/app

# ENV variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# add & install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# run server
CMD python manage.py run -h 0.0.0.0