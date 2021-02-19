FROM python:3.8.5

RUN apt-get update && apt install -y locales \
        && apt-get clean \
        && rm -rf /var/lib/apt/lists/*

RUN echo "LC_ALL=en_US.UTF-8" >> /etc/environment && \
	echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen && \
	echo "LANG=en_US.UTF-8" > /etc/locale.conf && \
	locale-gen en_US.UTF-8

WORKDIR /app/

# hadolint ignore=DL3013
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY . /app/
CMD ["gunicorn", "-b", "0.0.0.0:80", "config.wsgi", "--timeout", "90"]
