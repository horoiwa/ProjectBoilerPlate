FROM python:3.9.13-buster

ARG UID
ARG GID
ARG GROUPNAME

ARG USERNAME=jovyan
ARG PASSWORD=jovyan

RUN apt-get update && apt-get install -y sudo
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -u $UID -g $GID $USERNAME && \
    echo $USERNAME:$PASSWORD | chpasswd
RUN usermod -aG sudo $USERNAME

USER $USERNAME
WORKDIR /project

ENV PATH $PATH:/home/jovyan/.local/bin
ENV PYTHONPATH $PYTHONPATH:/project

RUN pip install poetry
COPY --chown=$UID:$GID pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-root
