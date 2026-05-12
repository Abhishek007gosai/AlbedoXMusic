FROM python:3.11-slim

WORKDIR /app

RUN apt-get update -y && \
    apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    unzip \
    git \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Deno
RUN curl -fsSL https://deno.land/install.sh | sh

ENV DENO_INSTALL="/root/.deno"
ENV PATH="${DENO_INSTALL}/bin:${PATH}"

# Install uv
RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"

# Copy dependency files
COPY pyproject.toml ./

# Optional: copy uv.lock only if exists
COPY uv.lock* ./

# Install dependencies
RUN uv sync || pip install -r requirements.txt

# Copy project files
COPY . .

# Start bot
CMD ["bash", "start"]
