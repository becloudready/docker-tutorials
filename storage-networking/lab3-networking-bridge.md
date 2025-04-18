

# Hands-On Lab: Understanding Docker Networking - Bridge Concepts

In this hands-on lab, you'll explore Docker's bridge networking concepts, including the default bridge network, user-defined bridges, and their real-world applications.

---

## **Lab Objectives**
1. Understand the default Docker bridge network.
2. Create and manage user-defined bridge networks.
3. Illustrate real-world scenarios using both types of networks.

---

## **Prerequisites**
- Docker installed on your system.
- Basic understanding of Docker commands and concepts.

---

## **Part 1: Exploring the Default Docker Bridge Network**

### **Step 1.1: Verify Docker Network**
Run the following command to list all Docker networks:
```bash
docker network ls
```

You should see the `bridge` network, which is Docker's default network.

### **Step 1.2: Inspect the Default Bridge Network**
Inspect the details of the default bridge network:
```bash
docker network inspect bridge
```

### **Step 1.3: Create Containers Using the Default Network**
Run two containers and test connectivity:
```bash
docker run -dit --name container1 alpine sh
docker run -dit --name container2 alpine sh
```

### **Step 1.4: Test Connectivity**
Attach to `container1` and try pinging `container2`:
```bash
docker exec -it container1 sh
ping container2
```

Notice that the containers cannot communicate by name in the default bridge network. They can only communicate via IP addresses.

---

## **Part 2: Creating and Using a User-Defined Bridge Network**

### **Step 2.1: Create a User-Defined Bridge Network**
Create a custom bridge network:
```bash
docker network create my_bridge_network
```

Verify its creation:
```bash
docker network ls
```

### **Step 2.2: Run Containers on the User-Defined Bridge Network**
Run two containers attached to the custom bridge network:
```bash
docker run -dit --name app1 --network my_bridge_network alpine sh
docker run -dit --name app2 --network my_bridge_network alpine sh
```

### **Step 2.3: Test Name-Based Connectivity**
Attach to one container and ping the other:
```bash
docker exec -it app1 sh
ping app2
```

Unlike the default bridge network, containers in a user-defined bridge network can communicate using their container names.

---

## **Part 3: Real-World Scenario: Multi-Container Application**

### **Scenario: A Simple Web Application with a Backend**

In this scenario, you'll set up a web server (frontend) and a database (backend) connected through a user-defined bridge network.

### **Step 3.1: Create a User-Defined Network**
```bash
docker network create webapp_network
```

### **Step 3.2: Run a Database Container**
Run a PostgreSQL database container:
```bash
docker run -d \
  --name db \
  --network webapp_network \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=pass \
  -e POSTGRES_DB=mydb \
  postgres
```

### **Step 3.3: Run a Web Server Container**
Run an Nginx container connected to the same network:
```bash
docker run -d \
  --name webserver \
  --network webapp_network \
  nginx
```

### **Step 3.4: Configure and Test the Setup**
Inspect the network to see container details:
```bash
docker network inspect webapp_network
```

Attach to the `webserver` container and verify the database is reachable:
```bash
docker exec -it ubuntu sh
apt update -y && apt install -y postgresql-client
psql -h db -U user -d mydb -c '\l'
```

---

## **Part 4: Cleaning Up**
After completing the lab, clean up resources:
```bash
docker stop container1 container2 app1 app2 db webserver
docker rm container1 container2 app1 app2 db webserver
docker network rm my_bridge_network webapp_network
```
---
Assignment

You are  tasked with setting up a proof-of-concept (PoC) for a basic web application. The application consists of the following components:

- Frontend (Web Server): A container running Nginx that serves a static webpage.
- Backend (Database): A PostgreSQL database container storing application data.
- Ensure frontend and backend are seggregated with different bridge networks

