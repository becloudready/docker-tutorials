### Installation

**Setup the Repo**
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

**Install Docker Community edition**
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

**Run Hello world**
```
sudo docker run hello-world
```
**Modify the user permission so that you can run docker command without sudo**

For AWS Ubuntu instance
```
sudo usermod -a -G docker ubuntu
```
Logout and Login before executing below commands
---

### **Assignment Tasks**

#### **Task 1: Pull an Image from Docker Hub**
1. Use the `docker pull` command to download the official **nginx** image from Docker Hub:
   ```bash
   docker pull nginx
   ```
2. Verify the image is available locally using the `docker images` command:
   ```bash
   docker images
   ```
3. Run a container from the **nginx** image and expose it on port 8080:
   ```bash
   docker run -d -p 8080:80 nginx
   ```
4. Open a web browser and visit `http://localhost:8080` to confirm nginx is running.

---
### **Lab 2: Working with Containers**

#### **Objective:**
Understand how to start, list, interact with, and manage Docker containers.

#### **Tasks:**

**Starting a Container:**
Run a container using the **Ubuntu** image in interactive mode:
  ```bash
  docker run -it ubuntu
  ```
Inside the container, run the command:
  ```bash
  echo "Hello from Ubuntu!"
  ```
Exit the container by typing `exit`.

**Listing Containers:**
View running containers:
  ```bash
  docker ps
  ```
View all containers (including stopped ones):
  ```bash
  docker ps -a
  ```

**Stopping and Removing Containers:**
Start a new **Alpine** container:
  ```bash
  docker run -d --name my-alpine alpine sleep 300
  ```
Stop the container:
  ```bash
  docker stop my-alpine
  ```
Remove the container:
  ```bash
  docker rm my-alpine
  ```

**Interactive Mode:**
Run a new **nginx** container in detached mode:
  ```bash
  docker run -d --name my-nginx nginx
  ```
Attach to the running container:
  ```bash
  docker exec -it my-nginx bash
  ```
Run the command:
  ```bash
  ls /usr/share/nginx/html
  ```
Exit the container's shell by typing `exit`.

