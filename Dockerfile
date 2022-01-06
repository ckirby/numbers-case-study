#
# Docker file for creating Backend components. Meant to be built via Docker
# Compose or in CI.
#
# Arguments:
#
#   dev - Whether or not Pipenv should install dev dependencies. "true" if so.
FROM python:3.9-slim

ARG dev="false"

EXPOSE 8080
WORKDIR /app/trellis

# Install application dependencies.
COPY Pipfile* ./
RUN pip install --no-cache-dir pipenv
RUN PIPENV_DEV=$dev pipenv install --system --deploy

COPY . .