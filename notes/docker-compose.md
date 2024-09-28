Here's a useful markdown guide for Docker Compose commands and notes:

## Docker Compose Commands

### Basic Commands

```bash
# Start services
docker compose up

# Start services in detached mode
docker compose up -d

# Stop and remove containers, networks
docker compose down

# View running services
docker compose ps

# View logs
docker compose logs

# Execute command in a running container
docker compose exec <service_name> <command>
```

### Building and Managing Images

```bash
# Build or rebuild services
docker compose build

# Pull service images
docker compose pull

# Push service images
docker compose push
```

### Service Lifecycle

```bash
# Start services
docker compose start

# Stop services
docker compose stop

# Restart services
docker compose restart

# Pause services
docker compose pause

# Unpause services
docker compose unpause
```

### Scaling and Running

```bash
# Scale a service
docker compose up --scale <service_name>=<num_instances>

# Run a one-off command
docker compose run <service_name> <command>
```

## Notes

1. **Compose File**: Docker Compose uses a YAML file (usually named `docker-compose.yml`) to define multi-container applications[1].

2. **Multiple Compose Files**: You can use multiple Compose files with the `-f` flag:
   ```bash
   docker compose -f docker-compose.yml -f docker-compose.prod.yml up
   ```

3. **Environment Variables**: Set environment variables in a `.env` file or use the `environment` key in your Compose file[1].

4. **Networking**: Compose sets up a single network for your app by default. Service names become hostnames that containers can use to communicate[1].

5. **Volumes**: Use the `volumes` key to mount paths on the host to the containers[1].

6. **Depends On**: Use `depends_on` to express dependency between services[1].

7. **Build Context**: When building images, you can specify a build context and alternate Dockerfile[1].

8. **Compose Version**: Ensure your Compose file version is compatible with your Docker Engine version[1].

9. **Project Name**: By default, Compose uses the directory name as the project name. Override this with the `-p` flag or `COMPOSE_PROJECT_NAME` environment variable[2].

10. **Scaling**: Not all services can be scaled. Those with static ports or singular volumes can't be scaled without additional configuration[4].

Remember to refer to the official Docker documentation for the most up-to-date and detailed information on Docker Compose usage and best practices.

Citations:
[1] https://docs.docker.com/reference/cli/docker/compose/
[2] https://gist.github.com/mkfares/41c9609fcde8d9f665210034e99d4bd9
[3] https://docs.docker.com/reference/cli/docker/compose/up/
[4] https://waytoeasylearn.com/learn/docker-compose-commands/
[5] https://devhints.io/docker-compose
[6] https://stackoverflow.com/questions/30063907/docker-compose-how-to-execute-multiple-commands
[7] https://docs.docker.com/get-started/workshop/08_using_compose/
[8] https://docs.docker.com/compose/