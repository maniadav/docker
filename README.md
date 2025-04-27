# Docker Guide

This document provides all important commands related to working with Docker for development and production.

---

## Docker Basics

**Check Docker Version**
```bash
docker --version
```

**Check Docker Info**
```bash
docker info
```

---

## Containers

**List All Running Containers**
```bash
docker ps
```

**List All Containers (including stopped ones)**
```bash
docker ps -a
```

**Start a Container**
```bash
docker start <container-id or container-name>
```

**Stop a Container**
```bash
docker stop <container-id or container-name>
```

**Restart a Container**
```bash
docker restart <container-id or container-name>
```

**Remove a Container**
```bash
docker rm <container-id or container-name>
```

**Remove All Stopped Containers**
```bash
docker container prune
```

---

## Images

**List All Docker Images**
```bash
docker images
```

**Remove a Docker Image**
```bash
docker rmi <image-id or image-name>
```

**Remove All Unused Images**
```bash
docker image prune
```

**Remove All Unused Images, Containers, Networks**
```bash
docker system prune
```

---

## Push Container to DockerHub

**Tag Image (if needed)**
```bash
docker tag <local-image>:<tag> <user>/<image_name>:<tag>
```

**Push Image**
```bash
docker push <user>/<image_name>:<tag>
```

---

## Pull Container from DockerHub

**Pull Image**
```bash
docker pull <user>/<image_name>:<tag>
```

---

## Development Container Setup

**Build the Development Container**
```bash
docker build -f Dockerfile.dev -t <dev_image_name> .
```

**Run the Development Container with Hot-Reloading**
```bash
docker run -p 5500:5500 -v $(pwd):/app <dev_image_name>
```

**Ensure Dependencies are Installed in the Container**
```bash
docker exec -it <container-id> npm install
```

*(Tip: You can get the `<container-id>` using `docker ps`.)*

---

## Production Container Setup

**Build the Production Container**
```bash
docker build -t <prod_image_name>:version .
```

**Run the Production Container**
```bash
docker run --name rock-oak -p 5500:5500 <prod_image_name>:version
```

---

## Other Useful Commands

**View Container Logs**
```bash
docker logs <container-id or container-name>
```

**Execute a Shell Inside a Running Container**
```bash
docker exec -it <container-id or container-name> sh
```
or (if bash is installed)
```bash
docker exec -it <container-id or container-name> bash
```

**Stop All Running Containers**
```bash
docker stop $(docker ps -q)
```

**Remove All Containers**
```bash
docker rm $(docker ps -a -q)
```

**Remove All Images**
```bash
docker rmi $(docker images -q)
```

**Update Docker Image**
- Rebuild the image:
```bash
docker build -t <image-name>:<tag> .
```
- Push the updated image:
```bash
docker push <user>/<image_name>:<tag>
```

---

## Tips

- Always pull the latest image before using:
```bash
docker pull <user>/<image_name>:<tag>
```
- Use tags properly (`latest`, `dev`, `prod`, `v1.0.0`, etc.) to manage versions easily.
- Always clean up unused containers and images to save disk space.

---

# 🎯 That's it!  
If you want, I can also generate a nice markdown table summarizing commands for even easier quick lookup. Want me to add that too? 🚀  
