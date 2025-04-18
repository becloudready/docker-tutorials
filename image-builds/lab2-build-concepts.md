
### **Lab Title**
**Exploring Docker Build: Environment Variables, Build Arguments, Tags, Layering, and Multi-Stage Builds**

---

### **Lab Objectives**
1. Understand the use of build arguments (`ARG`) and environment variables (`ENV`) in Dockerfiles.
2. Learn about tagging images and versioning.
3. Explore Docker image layering and caching for efficient builds.
4. Implement multi-stage builds to optimize image size.
5. Apply best practices for Dockerfile creation.

---

### **Pre-requisites**
1. Docker installed on your system.
2. Basic knowledge of Docker commands and image creation.
3. A code editor (e.g., VSCode).
4. Git installed.

---

### **Lab Setup**
Create a project folder structure:
```
docker-build-lab/
├── stage-1-simple-build/
│   └── Dockerfile
├── stage-2-env-vars/
│   ├── Dockerfile
│   ├── app/
│   │   └── app.py
├── stage-3-build-args/
│   ├── Dockerfile
│   ├── config/
│   │   └── config.txt
├── stage-4-layering/
│   ├── Dockerfile
│   ├── app/
│   │   └── main.py
├── stage-5-multi-stage/
│   ├── Dockerfile
│   └── app/
│       ├── requirements.txt
│       └── app.py
```

---

### **Stage 1: Simple Build**
**Objective**: Build a basic image with a single layer.
1. Create a `Dockerfile`:
    ```dockerfile
    # Base image
    FROM alpine:3.17

    # Add a command
    CMD ["echo", "Hello, Docker!"]
    ```
2. Build and run:
    ```bash
    docker build -t simple-build .
    docker run simple-build
    ```

---

### **Stage 2: Using Environment Variables**
**Objective**: Illustrate the use of environment variables.
1. Add the following `Dockerfile`:
    ```dockerfile
    FROM python:3.9-slim

    # Set environment variable
    ENV APP_ENV=development

    # Copy and run the app
    COPY app/ /app
    WORKDIR /app
    CMD ["python", "app.py"]
    ```
2. Create a simple Python app:
    ```python
    # app/app.py
    import os
    print(f"Running in {os.getenv('APP_ENV')} environment")
    ```
3. Build and run:
    ```bash
    docker build -t env-example .
    docker run env-example
    ```

---

### **Stage 3: Build Arguments**
**Objective**: Use `ARG` to customize builds.
1. Create a `Dockerfile`:
    ```dockerfile
    FROM ubuntu:20.04

    # Define build argument
    ARG VERSION="1.0"

    # Use the argument
    RUN echo "Building version $VERSION"

    CMD ["echo", "Build complete!"]
    ```
2. Build with different arguments:
    ```bash
    docker build -t build-arg-example --build-arg VERSION=2.0 .
    ```

---

### **Stage 4: Layering and Caching**
**Objective**: Illustrate how layering works and optimize builds.
1. Add the following `Dockerfile`:
    ```dockerfile
    FROM python:3.9-slim

    # Install dependencies
    RUN pip install flask

    # Copy app code
    COPY app/ /app

    # Set working directory and run the app
    WORKDIR /app
    CMD ["python", "main.py"]
    ```
2. Create a simple Flask app:
    ```python
    # app/main.py
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello from Flask!"

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
    ```
3. Build and run:
    ```bash
    docker build -t flask-app .
    docker run -p 5000:5000 flask-app
    ```

---

### **Stage 5: Multi-Stage Build**
**Objective**: Reduce image size using a multi-stage build.
1. Create a `Dockerfile`:
    ```dockerfile
    # Stage 1: Build dependencies
    FROM python:3.9-slim as builder

    WORKDIR /app
    COPY app/requirements.txt .
    RUN pip install -r requirements.txt --target /app/dependencies

    # Stage 2: Create final image
    FROM python:3.9-slim
    WORKDIR /app
    COPY --from=builder /app/dependencies /app/dependencies
    COPY app/ /app

    ENV PYTHONPATH=/app/dependencies
    CMD ["python", "app.py"]
    ```
2. Add `requirements.txt`:
    ```
    flask
    ```
3. Build and run:
    ```bash
    docker build -t multi-stage-example .
    docker run -p 5000:5000 multi-stage-example
    ```

---

### **Key Concepts to Explore in Each Stage**
1. **Environment Variables**: Show how to pass runtime variables.
2. **Build Arguments**: Customize image creation during the build process.
3. **Image Tagging**: Use `-t` to version images.
4. **Layering**: Modify the `Dockerfile` to see caching in action.
5. **Multi-Stage Builds**: Reduce image size by separating build dependencies.

