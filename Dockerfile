# STAGE 1
# Use full base image for builder
FROM python:3.11 AS builder

# Create a non-root user
RUN useradd -m -u 1001 appuser

# Set working directory within the container
WORKDIR /app

# Switch to non-root user
USER appuser

# Copy requirements.txt (dependencies file) and install dependencies
COPY requirements.txt .
RUN pip install --user -r requirements.txt

# The command to run when the container starts
CMD ["python", "-u", "app.py"]

# STAGE 2
FROM python:3.11-slim

# Install curl for healthcheck
RUN apt-get update && apt-get install -y curl

# Create same user with same UID
RUN useradd -m -u 1001 appuser

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /home/appuser/.local /home/appuser/.local

# Copy the application code into the container
COPY . .

ENV PATH=/home/appuser/.local/bin:$PATH

# Switch to non-root user
USER appuser

# Expose the port
EXPOSE 5000

CMD ["python", "-u", "app.py"]