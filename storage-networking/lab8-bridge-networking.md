## Docker Networking Assignment: Building a Web App with Bridge Networks

This assignment focuses on understanding and implementing Docker bridge networks to isolate and manage different components of a simple web application. You will create two separate bridge networks: one for the frontend and one for the backend.

**Learning Objectives:**

*   Understand the concept of Docker bridge networks.
*   Learn how to create and manage custom bridge networks.
*   Learn how to connect containers to specific networks.
*   Practice inter-container communication using Docker networks.
*   Understand basic containerization of a web application.

**Scenario:**

You will build a simple web application consisting of a frontend (a basic HTML page served by Nginx) and a backend (a simple "Hello World" service using Python Flask). These components will communicate over a dedicated backend network, while the frontend will be accessible from the host machine.

**Tasks:**

1.  **Backend Network and Service:**
    *   Create a Docker bridge network named `backend-network`.
    *   Create a Dockerfile for a simple Python Flask application that returns "Hello from Backend!". This application should listen on port 5000. Example:

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route("/")
    def hello():
        return "Hello from Backend!"

    if __name__ == "__main__":
        app.run(debug=True, host='0.0.0.0', port=5000)
    ```

    *   Build the backend image and name it `backend-app`.
    *   Run a container from the `backend-app` image and connect it to the `backend-network`. Name the container `backend`.

2.  **Frontend Network and Service:**
    *   Create a Docker bridge network named `frontend-network`.
    *   Create a simple `index.html` file with the following content (or similar):

    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Frontend</title>
    </head>
    <body>
        <h1>Welcome to the Frontend</h1>
        <p id="backend-message">Fetching message from backend...</p>
        <script>
            fetch('http://backend:5000') // Use container name for resolution
                .then(response => response.text())
                .then(data => document.getElementById('backend-message').innerText = data)
                .catch(error => document.getElementById('backend-message').innerText = "Error connecting to backend.");
        </script>
    </body>
    </html>
    ```

    *   Create a Dockerfile for an Nginx container that serves the `index.html` file. You can use a multi-stage build to copy the HTML file. Example Dockerfile:

    ```dockerfile
    FROM nginx:alpine AS builder
    COPY index.html /usr/share/nginx/html

    FROM nginx:alpine
    COPY --from=builder /usr/share/nginx/html /usr/share/nginx/html
    EXPOSE 80
    ```

    *   Build the frontend image and name it `frontend-app`.
    *   Run a container from the `frontend-app` image and connect it to the `frontend-network`. Map port 80 of the container to port 8080 of the host machine. Name the container `frontend`. Also connect the container to the `backend-network`.

3.  **Verification:**
    *   Access the application by navigating to `http://localhost:8080` in your web browser. You should see the "Welcome to the Frontend" message, and the message from the backend ("Hello from Backend!") should be displayed below it.
    *   Use `docker network inspect backend-network` and `docker network inspect frontend-network` to verify the network configurations and the connected containers.
    *   Use `docker ps` to verify the running containers and their port mappings.

**Deliverables:**

*   All Dockerfiles (backend and frontend).
*   The `index.html` file.
*   A brief document explaining the steps you took and any challenges you encountered.
*   Screenshots demonstrating the working application in your browser and the output of the `docker network inspect` commands.

**Bonus:**

*   Use Docker Compose to orchestrate the entire setup.
*   Explore using a custom DNS server within Docker to resolve container names instead of relying on Docker's built-in DNS (e.g., using `dnsmasq`).

This assignment will help you gain practical experience with Docker networking and container orchestration. Remember to document your steps and explain your reasoning. Good luck!
