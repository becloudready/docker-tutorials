## Docker Labs

### **Lab 1: Exploring Docker Images**

#### **Objective:**
Learn how to pull, list, and manage Docker images effectively.

#### **Tasks:**

**Pulling Images:**
Pull the **Ubuntu** image from Docker Hub:
  ```bash
  docker pull ubuntu
  ```
Pull the **Alpine** image:
  ```bash
  docker pull alpine
  ```

**Listing Images:**
View all the downloaded images using:
  ```bash
  docker images
  ```

**Inspecting Layers:**
Use the `docker history` command to inspect the layers of the **Ubuntu** image:
  ```bash
  docker history ubuntu
  ```

**Removing Images:**
Remove the **Alpine** image using:
  ```bash
  docker rmi alpine
  ```
Verify that it has been deleted by listing all images again.

**Best Practices:**
Identify unused images and clean up the system using:
  ```bash
  docker system prune
  ```



---

### Combining Image and Container Management**

#### **Objective:**
Learn how to combine image and container operations to create a workflow.

#### **Tasks:**

Pull the **Python** image:
  ```bash
  docker pull python
  ```

Run a container from the **Python** image and start a Python REPL:
  ```bash
  docker run -it python
  ```

Inside the container, write and execute a simple Python script:
  ```python
  print("Hello, Docker!")
  ```

Exit the container and save its ID using:
  ```bash
  docker ps -a
  ```

Commit the container changes to a new image:
  ```bash
  docker commit <container_id> python-custom
  ```

Run a new container from the **python-custom** image:
  ```bash
  docker run -it python-custom
  ```




## Assignment - Image Management

Problem Statement:

You are tasked with managing and working with Docker images. Perform the following:

- Pull the nginx image from Docker Hub.

- Tag the image with a custom name of your choice.

- Save the tagged image to a tar file for offline use.

- Delete the image from your local machine.

- Load the image back from the tar file and verify its presence using the docker images command.


