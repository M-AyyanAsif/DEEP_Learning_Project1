FROM python:3.10-slim

# Clean production environment setup - skip heavy updates and recommended bloat
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

# Create a secure non-root deployment user for Hugging Face
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:${PATH}"

WORKDIR /home/user/app

# Copy and install Python packages first (efficient layer caching)
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

# Copy remaining codebase structural components
COPY --chown=user . .

# Bind execution to Hugging Face's network socket port
EXPOSE 7860

CMD ["python", "app.py"]