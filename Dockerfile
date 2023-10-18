FROM python:3.11-alpine
RUN mkdir job_task_questions
WORKDIR  /job_task_questions
COPY pyproject.toml .
RUN pip3 install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

COPY . .

RUN chmod a+x docker/*.sh
