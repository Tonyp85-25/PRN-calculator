FROM python:3.9-alpine3.13
LABEL maintainer="ap"

ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt /tmp/requirements.txt 
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY . /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
        then /py/bin/pip install -r /tmp/requirements.dev.txt; \
    fi && \
    rm -rf /tmp && \
    if [ $DEV = "false" ]; \
        then rm -rf ./api/tests; \
    fi && \
    apk del .tmp-build-deps && \
    adduser \
    # Do not assign password
        -D \  
    # Do not create home directory
        -H \
        fast-api

ENV PATH="/py/bin:$PATH"
USER fast-api

    

  