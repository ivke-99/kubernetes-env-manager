ARG PYTHON_VERSION=3.11-slim

# Stage 0, instaling dev packages
FROM python:${PYTHON_VERSION} as builder
LABEL maintainer="Ivan Djuraki <ivandjuraki@protonmail.com>"
ENV PYTHONUNBUFFERED 1
ARG APP_VERSION
ENV APP_VERSION=$APP_VERSION

WORKDIR /wheels
COPY ./requirements/ /wheels/requirements/
RUN pip install -U pip && pip wheel -r ./requirements/prod.txt

# Stage 1, no dev packages on wheels
FROM python:${PYTHON_VERSION}
ENV PYTHONUNBUFFERED=1
ARG APP_VERSION
ENV APP_VERSION=$APP_VERSION

COPY --from=builder /wheels /wheels
RUN pip install -U pip \
       && pip install -r /wheels/requirements/prod.txt \
                      -f /wheels \
       && rm -rf /wheels \
       && rm -rf /root/.cache/pip/*


# Copy code to docker
COPY ./ /opt/app/
COPY ./config/ /opt/app/config/
WORKDIR /opt/app
RUN python setup.py install
# Collect our static media.

# Specify the command to run when the image is run.
CMD "/opt/app/config/run.sh"