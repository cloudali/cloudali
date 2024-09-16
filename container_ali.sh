#!/bin/bash
curl -o ali_profile.py https://raw.githubusercontent.com/cloudali/cloudali/main/ali_profile.py

if [ ! -f ali_profile.py ]; then
    echo "Error: ali_profile.py not found after download."
    exit 1
fi
echo "Creating Dockerfile..."
cat <<EOF > Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY ali_profile.py /app/ali_profile.py
CMD ["python", "ali_profile.py"]
EOF

chmod +x container_ali.sh

if command -v python3 &> /dev/null && command -v pip3 &> /dev/null; then
    echo "Python and pip are already installed."
else
    echo "Python and pip are not installed. Please install them before proceeding."
    exit 1
fi

echo "Building the Docker image..."
docker build -t ali_cloud_engineer .

if [ $? -eq 0 ]; then
    echo "Running the Docker container..."
    docker run --rm ali_cloud_engineer
else
    echo "Failed to build the Docker image."
fi
