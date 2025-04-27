# 📦 Node.js Backend

## Development (with Hot Reloading)

**Dockerfile.dev** will be used.

### Build Development Image
```bash
docker build -f Dockerfile.dev -t rock-oak-node-backend-dev .
```

### Run Development Container (with Live Reloading)
```bash
docker run -p 5500:5500 -v $(pwd):/app rock-oak-node-backend-dev
```
- **Explanation:**  
Mounts current code directory (`$(pwd)`) to `/app` inside the container for live reloading (using something like `nodemon`).

### Install Node Modules inside the Container (if needed)
```bash
docker exec -it <container-id> npm install
```

---

## Production

**Dockerfile** (production) will be used.

### Build Production Image
```bash
docker build -t rock-oak-node-backend:0.0.0 .
```

### Run Production Container
```bash
docker run --name rock-oak-node -p 5500:5500 rock-oak-node-backend:0.0.0
```

---