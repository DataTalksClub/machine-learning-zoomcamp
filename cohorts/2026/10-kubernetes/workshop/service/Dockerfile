FROM python:3.13.5-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

ENV PATH="/app/.venv/bin:$PATH"

COPY pyproject.toml uv.lock .python-version ./

RUN uv sync --locked

COPY app.py clothing-model.onnx ./

EXPOSE 8080

ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
