Make sure Docker Desktop version 2 is installed then run following commands 
# docker compose config
# Validates and displays the final configuration that Docker Compose will use by merging the values 
# from the YAML file (docker-compose.yml). Useful for debugging and ensuring everything is correctly defined.
docker compose config 

# docker compose up -d
# Starts (or creates if needed) the containers in detached mode (running in the background).
# If the images do not exist, it builds them automatically.
docker compose up -d 

# docker compose ps
# Lists all running containers started by Docker Compose, displaying their names, states, and exposed ports.
docker compose ps 

# docker compose start
# Starts existing containers (those that were previously created or stopped), without recreating them.
docker compose start 

# docker compose down
# Stops and removes containers, networks, and volumes defined in the docker-compose.yml.
# Useful when you want to stop everything and clean up resources.
docker compose down

# docker compose up -d --build
# Rebuilds the images, forcing a re-creation of containers even if they already exist.
# It ensures that any changes in the Dockerfile or dependencies are reflected.
docker compose up -d --build
