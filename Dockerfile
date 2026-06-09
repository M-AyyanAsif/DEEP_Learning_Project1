FROM python:3.10-slim

<<<<<<< HEAD
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    && rm -rf /var/lib/apt/lists/*

=======
# Install system dependencies
RUN apt-get update -y && apt-get install -y awscli git && rm -rf /var/lib/apt/lists/*

# Create a non-root user for Hugging Face security
>>>>>>> 578e7f68f7edccf75be8a865a97f6e32673e9426
RUN useradd -m -u 1000 user
USER user
ENV PATH="/home/user/.local/bin:${PATH}"

WORKDIR /home/user/app

<<<<<<< HEAD

ENV PYTHONPATH=src

=======
# Copy requirements and install
>>>>>>> 578e7f68f7edccf75be8a865a97f6e32673e9426
COPY --chown=user requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir --upgrade -r requirements.txt

<<<<<<< HEAD
COPY --chown=user . .

EXPOSE 7860

=======
# Copy the rest of the application files
COPY --chown=user . .

# Expose Hugging Face's mandatory port
EXPOSE 7860

# Run the flask application
>>>>>>> 578e7f68f7edccf75be8a865a97f6e32673e9426
CMD ["python", "app.py"]