### Assignment: Building a Simplified Data Application with Docker Compose

#### **Objective**
The goal of this assignment is to create a data application using **Docker Compose**, incorporating concepts of storage, networking, and multiple interconnected applications. This assignment will also involve initializing a database and deploying monitoring tools (Prometheus and Grafana) to ensure proper application monitoring.

---

### **Assignment Requirements**

#### **1. Application Overview**
You are tasked with creating a simplified data application with the following components:
- **Frontend**: A **Streamlit** application for user interaction.
- **Database**: A **PostgreSQL** database for persistent storage, preloaded with a table and sample data during initialization.
- **Monitoring**: Deploy **Prometheus** for metrics collection and **Grafana** for visualizing application metrics.

#### **2. Functional Requirements**
- **Frontend**:
  - Provide a web interface using Streamlit.
  - The interface should allow users to query and visualize data directly from the database.
- **Database**:
  - Use PostgreSQL with an initialized schema and preloaded data.
  - The database schema should include a sample table (e.g., `users` or `sales`).
- **Monitoring**:
  - Configure Prometheus to scrape metrics from all running services.
  - Set up a Grafana dashboard to visualize the metrics (CPU, memory, requests, etc.).

#### **3. Technical Requirements**
- **Docker Compose Configuration**:
  - Use Docker Compose to define and orchestrate all services.
  - Services should include `frontend`, `db`, `prometheus`, and `grafana`.
- **Networking**:
  - Create a private network for the application.
  - Ensure secure communication between services using the Docker network.
  - Expose necessary ports for external access (e.g., 8501 for Streamlit, 9090 for Prometheus, and 3000 for Grafana).
- **Storage**:
  - Use volumes for persistent storage of the database and Prometheus data.
  - Ensure that logs and other stateful data are not lost upon container restart.

#### **4. Steps to Follow**
1. **Database Initialization**:
   - Create a SQL script to initialize the database schema and insert sample data.
   - Mount the SQL script as a volume in the PostgreSQL container.

2. **Frontend Service**:
   - Create a Streamlit application to interact directly with the database.
   - Include features for querying and visualizing data from the database.

3. **Monitoring Setup**:
   - Configure Prometheus to scrape metrics from all running services.
   - Set up a Grafana container with a predefined dashboard to visualize Prometheus metrics.

4. **Docker Compose**:
   - Write a `docker-compose.yml` file to define and manage all services.
   - Include health checks for all services to ensure proper initialization.

---

### **Deliverables**
1. A `docker-compose.yml` file defining all services.
2. A folder structure with:
   - `frontend/`: Contains the Streamlit app.
   - `db/`: Contains the SQL initialization script.
   - `monitoring/`: Configuration files for Prometheus and Grafana.
3. Documentation (in a `README.md` file) that includes:
   - Setup and deployment instructions.
   - Descriptions of each service and their interactions.
   - How to access the application and monitoring dashboards.

---

### **Evaluation Criteria**
- **Completeness**:
  - All components (frontend, database, Prometheus, Grafana) are correctly configured and working.
- **Code Quality**:
  - Clean and modular code for the frontend.
- **Docker Knowledge**:
  - Proper usage of volumes, networks, and multi-service orchestration in Docker Compose.
- **Monitoring**:
  - Prometheus and Grafana are correctly set up and functional.
- **Documentation**:
  - Clear and concise instructions in the `README.md` file.

---

### **Bonus Tasks**
1. Add additional metrics or alerts in Prometheus and visualize them in Grafana.
2. Use environment variables in `docker-compose.yml` for configuration (e.g., database credentials).

