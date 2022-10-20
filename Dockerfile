FROM python:3.8-alpine

LABEL "com.github.actions.name"="API Docker"
LABEL "com.github.actions.description"="Update Stack Docker (docker-compose) using backend API Docker"
LABEL "com.github.actions.icon"="refresh-cw"
LABEL "com.github.actions.color"="green"

LABEL version="0.0.1"
LABEL repository="https://github.com/roanfranklin/api-docker-action"
LABEL homepage="https://remf.com.br/"
LABEL maintainer="Roan Franklin <roanfranklin@gmail.com>"

RUN pip install --quiet --no-cache-dir python-dotenv requests
#github-action-utils

ADD entrypoint.py /entrypoint.py

CMD ["/entrypoint.py"]
ENTRYPOINT ["python"]
