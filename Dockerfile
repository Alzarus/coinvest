# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip before installing packages
# RUN pip3 install --upgrade pip setuptools wheel

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Make port 8051 available to the world outside this container
EXPOSE 8051

# Define environment variable
ENV NAME investcrip-front

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# streamlit run <python_file.py> when the container launches
ENTRYPOINT ["streamlit", "run", "./src/cripto-board.py", "--server.port=8051", "--server.address=0.0.0.0"]

# Run app.py when the container launches
# CMD ["python", "./src/cripto-board.py"]
