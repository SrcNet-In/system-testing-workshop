FROM mcr.microsoft.com/playwright/python:v1.54.0-jammy

USER root

RUN pip3 install poetry==1.8.2
RUN poetry config virtualenvs.create false

RUN groupadd user
RUN adduser --system --no-create-home --disabled-password --shell /bin/bash user

WORKDIR /opt/System-Test-Demo-BDD

COPY --chown=user pyproject.toml .
COPY --chown=user poetry.lock .

ENV POETRY_VIRTUALENVS_CREATE=false

RUN poetry lock --no-update
RUN poetry install --no-root

COPY --chown=user . .

# Optional: Only create symlink if src exists
RUN [ -d "src" ] && mkdir -p /app && ln -s /opt/System-Test-Demo-BDD/src /app/src || true

USER user

# Replace with your actual entrypoint script or command
CMD ["pytest", "-s" , "-v"]