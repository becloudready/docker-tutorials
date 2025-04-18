### **Hands-On Lab: Exploring Docker Storage Drivers and Persistent Data Management**

---

### **Lab Objective**
In this lab, students will:
1. Understand Docker storage drivers and their role in container storage.
2. Experiment with Docker's writable layer and observe data persistence behavior.
3. Use Docker volumes and bind mounts for persistent storage.

---

### **Prerequisites**
- Docker installed on your Linux system.
- Basic understanding of Docker concepts.

---

### **Part 1: Exploring the Writable Layer**

#### **Step 1.1: Run a Temporary Container**
Start a container using the `alpine` image:
```bash
docker run -dit --name temp-container alpine sh
```

#### **Step 1.2: Create Files Inside the Container**
Access the container shell and create a file:
```bash
docker exec -it temp-container sh
touch /test-file
echo "Hello, Docker!" > /test-file
cat /test-file
```

#### **Step 1.3: Stop and Remove the Container**
Stop and remove the container:
```bash
docker stop temp-container
docker rm temp-container
```

#### **Step 1.4: Verify File Persistence**
Run a new container with the same image and check if the file exists:
```bash
docker run -it alpine sh
ls /test-file
```

**Observation:**  
The file is no longer available, demonstrating that data in the writable layer is not persistent.

---

### **Part 2: Experimenting with Storage Drivers**

#### **Step 2.1: Check the Current Storage Driver**
Find the storage driver Docker is using:
```bash
docker info | grep "Storage Driver"
```

#### **Step 2.2: Inspect Container Layers**
Inspect the layers of an image:
```bash
docker image inspect alpine
```

Run a container, make changes, and inspect its layers:
```bash
docker run -dit --name layer-test alpine sh
docker exec -it layer-test sh -c "echo 'Layer Test' > /layer-file"
docker commit layer-test layer-image
docker image inspect layer-image
```

---

### **Part 3: Using Docker Volumes**

#### **Step 3.1: Create a Volume**
Create a named volume:
```bash
docker volume create my-volume
```

#### **Step 3.2: Attach the Volume to a Container**
Run a container with the volume attached:
```bash
docker run -dit --name volume-container -v my-volume:/data alpine sh
```

#### **Step 3.3: Write Data to the Volume**
Access the container shell and create a file in the volume:
```bash
docker exec -it volume-container sh
echo "Persistent data" > /data/persistent-file
```

#### **Step 3.4: Verify Data Persistence**
Stop and remove the container, then attach the volume to a new container:
```bash
docker stop volume-container
docker rm volume-container
docker run -it --name new-container -v my-volume:/data alpine sh
cat /data/persistent-file
```

**Observation:**  
Data in the volume persists across container lifecycles.

---

### **Part 4: Using Bind Mounts**

#### **Step 4.1: Create a Directory on the Host**
Create a directory on your host system:
```bash
mkdir ~/docker-bind-mount
echo "Hello from Host!" > ~/docker-bind-mount/host-file
```

#### **Step 4.2: Attach the Directory as a Bind Mount**
Run a container with the directory mounted:
```bash
docker run -dit --name bind-container -v ~/docker-bind-mount:/app alpine sh
```

#### **Step 4.3: Access and Modify the Bind Mount**
Access the container shell and verify the contents:
```bash
docker exec -it bind-container sh
ls /app
cat /app/host-file
echo "Modified by Container" >> /app/host-file
```

Verify changes from the host:
```bash
cat ~/docker-bind-mount/host-file
```

---

### **Part 5: Cleaning Up**

Remove all containers, volumes, and temporary files created during the lab:
```bash
docker rm -f $(docker ps -aq)
docker volume rm my-volume
rm -r ~/docker-bind-mount
```

---

### **Key Takeaways**
1. The writable layer in Docker is temporary and tied to the container's lifecycle.
2. Docker volumes provide persistent storage that is independent of container lifecycles.
3. Bind mounts enable direct interaction between host filesystems and containers.
4. Storage drivers play a critical role in managing container storage layers.

