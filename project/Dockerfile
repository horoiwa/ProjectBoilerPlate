FROM python:3.9.13-buster

ARG UID
ARG GID
ARG GROUPNAME
ARG USERNAME=jovyan

RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -u $UID -g $GID $USERNAME
RUN usermod -aG sudo jovyan

USER $USERNAME
WORKDIR /project

ENV PATH $PATH:/home/jovyan/.local/bin
ENV PYTHONPATH $PYTHONPATH:/project

RUN echo $PATH && echo $PYTHONPATH
RUN pip install poetry
COPY --chown=$UID:$GID pyproject.toml poetry.lock* ./
RUN poetry config virtualenvs.create false && \
    poetry install --no-root
