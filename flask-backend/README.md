

# 🐍 Flask Backend

## Development (with Hot Reloading)

**Dockerfile.dev** (or similar) for Flask dev server.

### Build Development Image
```bash
docker build -f Dockerfile.dev -t rock-oak-flask-backend-dev .
```

### Run Development Container (with Live Reloading)
```bash
docker run -p 5000:5000 -v $(pwd):/app -e FLASK_ENV=development rock-oak-flask-backend-dev
```
- **Explanation:**  
`-e FLASK_ENV=development` enables Flask's debug mode for hot reloading.  
Mounts the code directory for automatic reloading.

---

## Production

**Dockerfile** (production) will be used.

### Build Production Image
```bash
docker build -t rock-oak-flask-backend:0.0.0 .
```

### Run Production Container
```bash
docker run --name rock-oak-flask -p 5000:5000 rock-oak-flask-backend:0.0.0
```
- Usually served via a production server (e.g., Gunicorn) inside the container.

---


# Docker Compose Script 
I’ll create a **`docker-compose.yml`** file that supports both:

- Development mode (`Dockerfile.dev`)
- Production mode (`Dockerfile`)

👉 **Here’s the `docker-compose.yml`**:

---

# 📦 `docker-compose.yml`

```yaml
version: '3.8'

services:
  flask-backend-dev:
    container_name: flask-backend-dev
    build:
      context: .
      dockerfile: Dockerfile.dev
    ports:
      - "5000:5000"
    volumes:
      - .:/app
    environment:
      - FLASK_ENV=development
    command: flask run --host=0.0.0.0 --port=5000
    restart: unless-stopped

  flask-backend-prod:
    container_name: flask-backend-prod
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5001:5000" # Notice different external port to avoid conflict with dev
    restart: unless-stopped
```

---

# 🎯 Usage Instructions

### Run **Development Server**
```bash
docker-compose up flask-backend-dev
```

- Runs Flask dev server with **live reload**.
- Code changes automatically reflected inside the container.

---

### Run **Production Server**
```bash
docker-compose up flask-backend-prod
```

- Runs production server with **Gunicorn**.
- Stable, production-ready environment.

---

### Running the Flask App

1. **Development**:  
   After setting up the `docker-compose.yml`, you can run the Flask dev server:
   ```bash
   docker-compose up flask-backend-dev
   ```
   The API will be available at `http://localhost:5000/api/dummy`.

2. **Production**:  
   To run the Flask app with **Gunicorn** in production mode:
   ```bash
   docker-compose up flask-backend-prod
   ```
   The API will be available at `http://localhost:5001/api/dummy`.

---

### Stop Containers
```bash
docker-compose down
```

---

# 🌟 Some Notes:
- We expose **port 5000** for dev and **port 5001** for prod to avoid conflicts if both are up.
- Live reload happens only for `flask-backend-dev`.
- `volumes: .:/app` mounts the code during dev but **not in prod**.
- `restart: unless-stopped` ensures the containers auto-restart on server reboot (good for prod servers).

---

# ✅ Final Directory Structure

```bash
your-flask-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── Dockerfile.dev
├── docker-compose.yml
└── (other files/folders)
```

---
