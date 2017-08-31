FROM dangerfarms/wc-base:latest
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
RUN apk --update --no-cache add curl
RUN curl https://raw.githubusercontent.com/django/django/master/extras/django_bash_completion >> ~/.bashrc
COPY requirements.txt /app/
COPY requirements.dev.txt /app/
RUN pip install -r requirements.dev.txt -U
COPY . /app/
