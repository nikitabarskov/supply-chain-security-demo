FROM docker.io/library/python:3.11.8@sha256:47d0618fb878d93e1b8cacb184fd8f727ae95c1b85d5959723e1d3e1848e2aba AS python

WORKDIR /srv/workspace

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py main.py

ENTRYPOINT [ "python", "main.py" ]
