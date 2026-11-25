FROM python:3.12.9-slim

# xgboost needs the OpenMP runtime on slim images
RUN apt-get update \
    && apt-get install -y --no-install-recommends libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:0.11.26 /uv /bin/uv

WORKDIR /app

# Install only the runtime dependencies, exactly as pinned in uv.lock
COPY pyproject.toml uv.lock ./
RUN uv sync --locked --no-dev --no-install-project
ENV PATH="/app/.venv/bin:$PATH"

COPY features.py predict.py model.bin ./

RUN useradd --create-home appuser
USER appuser

EXPOSE 9696
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:9696/health')"

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]
