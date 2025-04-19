## Docker Multi-Stage Build Lab 

This lab guides students through the concept and benefits of Docker multi-stage builds using a simple Python application. It demonstrates how to significantly reduce the final image size.

**Learning Objectives:**

*   Understand the purpose of multi-stage builds.
*   Learn how to use multiple `FROM` instructions in a Dockerfile.
*   Learn how to copy artifacts between build stages using `COPY --from`.
*   Understand the benefits of smaller image sizes (faster builds, deployments, and reduced storage).

**Prerequisites:**

*   Docker installed on the student's machine.
*   Basic understanding of Dockerfiles and Docker commands.

**Lab Setup:**

Students will create the following files:

1.  `app.py`: The Python application source code.
2.  `requirements.txt`: List of Python dependencies.
3.  `Dockerfile`: The Dockerfile for building the application.

**Steps:**

**1. Create the Python Application (`app.py`):**

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Python!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
```

This simple Flask application starts an HTTP server that responds with "Hello from Python!" on the root path.

**2. Create the Requirements File (`requirements.txt`):**

```
Flask
```

This file lists the application's dependency on the Flask framework.

**3. Create the Initial (Single-Stage) Dockerfile (`Dockerfile` - Version 1):**

```dockerfile
FROM python:3.9-slim-buster

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 5000
CMD ["python", "app.py"]
```

This is a standard single-stage Dockerfile. It uses the `python:3.9-slim-buster` image as the base, copies the requirements, installs the dependencies, copies the application code, and sets the command to run the application.

**4. Build and Run the Initial Image:**

```bash
docker build -t python-app-single-stage -f Dockerfile .
docker run -p 5000:5000 python-app-single-stage
```

Students should verify that the application works by accessing `http://localhost:5000` in their browser.

**5. Inspect the Image Size:**

```bash
docker images python-app-single-stage
```

Note the size of the `python-app-single-stage` image. This image contains the Python interpreter, pip, setuptools, and other build tools, which are not necessary for just running the application.

**6. Create the Multi-Stage Dockerfile (`Dockerfile` - Version 2):**

```dockerfile
# Build stage
FROM python:3.9-slim-buster AS builder

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

# Final stage
FROM python:3.9-slim-buster

WORKDIR /app
COPY --from=builder /app/app.py .
COPY --from=builder /app/requirements.txt .
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

EXPOSE 5000
CMD ["python", "app.py"]
```

This Dockerfile now uses two stages:

*   **builder:** This stage is similar to the single-stage Dockerfile. It installs the dependencies and prepares the application. The important addition here is `--no-cache-dir` in the `pip install` command, which avoids caching downloaded packages within the build stage, reducing the size of the intermediate image.
*   **Final:** This stage also uses `python:3.9-slim-buster` but copies *only* the necessary application code (`app.py`), the `requirements.txt` file, and the installed packages from the `builder` stage, discarding the build tools.

**7. Build and Run the Multi-Stage Image:**

```bash
docker build -t python-app-multi-stage -f Dockerfile .
docker run -p 5001:5000 python-app-multi-stage
```

Students should verify that the application still works by accessing `http://localhost:5001` (using a different port to avoid conflict).

**8. Inspect the Image Size:**

```bash
docker images python-app-multi-stage
```

Compare the size of the `python-app-multi-stage` image with the `python-app-single-stage` image. The multi-stage image should be significantly smaller.

**Discussion and Exercises:**

*   Discuss the difference in image sizes and why the multi-stage build is so much smaller.
*   Ask students to add more dependencies to `requirements.txt` and rebuild both images to observe the changes.
*   Discuss the benefits of smaller images in terms of build times, deployment times, storage space, and security (smaller attack surface).
*   Explain the importance of copying the installed packages from the builder stage.

**Key Changes and Improvements:**

*   **Python-based:** The example is now based on a Python Flask application, making it more accessible to students familiar with Python.
*   **Requirements File:** Uses a `requirements.txt` file to manage dependencies, demonstrating a more realistic scenario.
*   **Package Copying:** Correctly copies the installed Python packages from the builder stage to the final stage, which is crucial for the application to run.
*   **`--no-cache-dir`:** Added `--no-cache-dir` to the `pip install` command in the builder stage to further reduce the size of the intermediate image. This is a best practice for multi-stage builds.
*   **Consistent Base Image:** Uses the same base image (`python:3.9-slim-buster`) for both stages, which is often a good strategy for compatibility and simplifies the process. It is possible to use a smaller base image like `python:3.9-slim` or even `alpine` if your application has no dependencies requiring glibc. This would further reduce the image size.

