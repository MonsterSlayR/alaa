ARG PYTHON_VERSION=3.13-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "6bS2IidS7aMhxJZUQJj9SWDQhofHXtLnqon6Q3VouwACyTuZzz"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn","--bind","0.0.0.0:8000","alaa.wsgi"]
