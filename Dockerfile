FROM python:3.10-slim

# Install system dependencies
RUN apt-get update -y && apt-get install -y awscli git && rm -rf /var/lib/apt/lists/*

# Create a non-root user for Hugging Face security
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:${PATH}"

WORKDIR /home/user/app

# Copy requirements and install
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

# Copy the rest of the application files
COPY --chown=user . .

# Expose Hugging Face's mandatory port
EXPOSE 7860

# Run the flask application
CMD ["python", "app.py"]