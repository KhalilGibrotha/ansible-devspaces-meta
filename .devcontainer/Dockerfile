FROM mcr.microsoft.com/devcontainers/python:3.11

# Install system dependencies
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    openssh-client \
    sshpass \
    git \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /workspace

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables for Ansible
ENV ANSIBLE_HOST_KEY_CHECKING=False \
    ANSIBLE_RETRY_FILES_ENABLED=False \
    ANSIBLE_STDOUT_CALLBACK=yaml \
    ANSIBLE_PYTHON_INTERPRETER=/usr/local/bin/python3

# Create ansible directory structure
RUN mkdir -p /home/vscode/.ansible \
    && chown -R vscode:vscode /home/vscode/.ansible

USER vscode
