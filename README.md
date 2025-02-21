***Hello Captain Docker Project***  [****URL***](https://roadmap.sh/projects/basic-dockerfile)

****Description***

This is a simple Docker project that prints "Hello, Captain!" to the console when the Docker container is run. The project demonstrates the creation of a Docker image using an Alpine Linux base image, and a single command to display a message before exiting.

****Dockerfile Explanation***

The Dockerfile is straightforward and contains the following instructions:

    FROM alpine:latest: This line specifies the base image for the Docker container.
    We use the latest version of Alpine Linux, a lightweight Linux distribution perfect for small and efficient Docker images.
    

    CMD ["echo", "Hello, Captain!"]: This line sets the command to be executed when the Docker container is started. 
    It runs the echo command, which prints "Hello, Captain!" to the console.

Build and Use the Docker Image

****Prerequisites***

    Before building and running this Docker image, ensure you have Docker installed on your system.
    Download and install Docker from the official Docker website.
    Either manually create a Dockerfile and copy the content of the Dockefile from this repo or clone this repo locally.

****Instructions***

Follow these steps to build and run the Docker image:

    Build the Docker Image

    Navigate to the directory containing the Dockerfile and run the following command:

    docker build -t hello-captain .

This command builds the Docker image and tags it with the name hello-captain.

    Run the Docker Image

    After building the image, you can run it using:

    docker run --rm hello-captain

This command runs the Docker container, which prints "Hello, Captain!" to the console. The --rm flag automatically removes the container after it exits.
