#!/bin/bash

# Build script for Render.com deployment

echo "Starting build process..."

# Upgrade pip to latest version
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Create necessary directories
mkdir -p logs

echo "Build completed successfully!"
