# Use latest Python runtime as a parent image
FROM centos/python-36-centos7

# Meta-data
LABEL maintainer="william surles <williamsurles@gmail.com>"

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY requirements.txt .

# pip install
RUN pip install -r requirements.txt

# Make port available to the world outside this container
EXPOSE 8050

# Create mountpoint
VOLUME /app

# ENTRYPOINT allows us to specify the default executible
ENTRYPOINT ["python"]

# CMD sets default arguments to executable which may be overwritten when using docker run
CMD ["app.py"]
