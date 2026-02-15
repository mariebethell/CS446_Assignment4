Docker Command Reference (with descriptions)

Image Building and Management
- docker build -t name:tag .
  Builds a Docker image from the Dockerfile in the current directory.

- docker images
  Lists all Docker images stored on your machine.

- docker rmi <image_id>
  Removes a Docker image from your system.

- docker tag <source_image> <username/repo:tag>
  Creates a new tag for an existing image, usually before pushing to a registry.

Container Management
- docker run -d -p host:container image
  Runs a container in detached mode and maps a host port to a container port.

- docker ps
  Shows all currently running containers.

- docker ps -a
  Shows all containers, including stopped ones.

- docker stop <container_id>
  Stops a running container.

- docker rm <container_id>
  Deletes a stopped container.

- docker logs <container_id>
  Displays the logs produced by a container.

- docker exec -it <container_id> sh
  Opens an interactive shell session inside a running container.

Docker Compose
- docker compose up --build -d
  Builds images (if needed) and starts all services in detached mode.

- docker compose down
  Stops and removes all services, networks, and containers created by Compose.

- docker compose ps
  Shows the status of services defined in docker-compose.yml.

- docker compose logs <service>
  Shows logs for a specific service (e.g., webapp or redis).

Docker Hub (Registry)
- docker login
  Logs you into Docker Hub.

- docker push <username/repo:tag>
  Uploads an image to Docker Hub.

- docker pull <username/repo:tag>
  Downloads an image from Docker Hub.

Networking
- docker network ls
  Lists all Docker networks on your system.

- docker network inspect <network_name>
  Shows detailed information about a specific network and connected containers.

System Cleanup
- docker system prune
  Removes unused containers, networks, and images to free disk space.

- docker volume prune
  Removes unused Docker volumes.