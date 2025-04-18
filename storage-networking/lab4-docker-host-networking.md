### **Lab Objective**

Learn how to:
1. Use the **host network driver** in Docker.
2. Install and use the `ip` command in a Debian-based Nginx container.
3. Explore network configurations for containers with host networking.

---

### **Prerequisites**
- Docker installed on your system.
- Basic knowledge of Docker and Linux networking.

---

### **Part 1: Setting Up an Nginx Container with Host Networking**

#### **Step 1.1: Run the Nginx Container**
Run an Nginx container with the **host network driver**:
```bash
docker run -dit --name nginx-host --network host nginx
```

#### **Step 1.2: Verify the Container is Running**
Check that the container is running:
```bash
docker ps
```

---

### **Part 2: Installing the `ip` Command**

#### **Step 2.1: Attach to the Container**
Access the running container's shell:
```bash
docker exec -it nginx-host sh
```

#### **Step 2.2: Update the Package Manager**
Inside the container, update the package list:
```bash
apt-get update
```

#### **Step 2.3: Install `iproute2`**
Install the `iproute2` package to gain access to the `ip` command:
```bash
apt-get install -y iproute2
apt-get install -y iputils-ping
```

#### **Step 2.4: Verify Installation**
Run the `ip` command to view the container's network configuration:
```bash
ip addr
```

---

### **Part 3: Exploring Network Configurations**

#### **Step 3.1: Identify Host Network Details**
Since the container is using the host network, the output of `ip addr` should reflect the host's network interfaces and IP address.

#### **Step 3.2: Test Network Connectivity**
Ping an external service to confirm connectivity:
```bash
ping -c 4 google.com
```

#### **Step 3.3: Test Port Exposure**
Access the Nginx server by navigating to the host's IP address in your browser:
```plaintext
http://<host_ip>
```

---

### **Part 4: Cleaning Up**

#### **Step 4.1: Stop and Remove the Container**
Stop the running container:
```bash
docker stop nginx-host
```

Remove the container:
```bash
docker rm nginx-host
```

---

### **Key Observations**
1. The container shares the same network stack as the host when using the host network driver.
2. Ports exposed by the container are directly accessible via the host's IP.
3. Installing the `ip` command allows for detailed inspection of network interfaces and configurations.

---

### **Optional Challenge**

1. Use the `ip` command to display routing information inside the container:
   ```bash
   ip route
   ```
2. Run a second container with the same configuration and observe potential port conflicts.
