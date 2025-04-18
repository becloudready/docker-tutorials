# Assignment: Building a 3-Tier Application Using Docker Compose

## Objective
This assignment will guide you through designing and deploying a 3-tier application architecture using **Docker Compose**. The 3-tier architecture includes a web server (frontend), an application server (backend), and a database server (DB). Each tier is containerized and orchestrated using Docker Compose.

---

## Application Overview

You will create a simple web application with the following components:

1. **Web Server (Frontend)**: A **Nginx** server to serve static content and act as a reverse proxy for the application server.
2. **Application Server (Backend)**: A Python Flask application that handles business logic and interacts with the database.
3. **Database Server**: A **PostgreSQL** database to store application data.

---

## Tasks

### 1. Database Server
- Use PostgreSQL as the database.
- Initialize the database with a schema and some sample data.
- Expose the necessary port to allow the application server to connect.

### 2. Application Server
- Create a Flask application that:
  - Connects to the database to fetch and store data.
  - Exposes RESTful APIs for the web server to consume.
- Use environment variables to configure database credentials.

### 3. Web Server
- Use Nginx to serve static files.
- Configure Nginx as a reverse proxy to forward API requests to the application server.

### 4. Docker Compose
- Define all three services (`web`, `app`, `db`) in a `docker-compose.yml` file.
- Set up networking to allow communication between the services.
- Use Docker volumes for persistent data storage.


---

## Deliverables
1. A `docker-compose.yml` file to orchestrate the services.
2. Configuration files for the database, application, and web server.
3. A fully functional 3-tier application accessible from the browser.
4. A `README.md` with clear setup and deployment instructions.

