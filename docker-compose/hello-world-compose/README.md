
### **Lab Steps**



#### **Build and Start the Services**
1. Build and start the services:
   ```bash
   docker compose up --build
   ```

2. Verify the services:
   - Access the backend directly at: `http://localhost:8000`
   - Access through Nginx proxy at: `http://localhost:8080`

---

#### **Explore Docker Compose Commands**
1. **View running containers**:
   ```bash
   docker ps
   ```

2. **Stop services**:
   ```bash
   docker compose stop
   ```

3. **Restart services**:
   ```bash
   docker compose restart
   ```

4. **Remove containers and networks**:
   ```bash
   docker compose down
   ```

---

#### **Modify the Backend Service**
1. Update the `app.py` file:
   ```python
   return "Hello, Docker Compose! Updated Backend Response."
   ```

2. Rebuild and restart the service:
   ```bash
   docker compose up --build
   ```

3. Verify the updated response.

---

#### **Experiment with the Nginx Configuration**
1. Modify `nginx/default.conf` to include a custom error page:
   ```nginx
   error_page 404 /custom_404.html;

   location = /custom_404.html {
       root /usr/share/nginx/html;
       internal;
   }
   ```

2. Reload Nginx:
   ```bash
   docker compose restart nginx
   ```

3. Test the custom 404 error by visiting an invalid path: `http://localhost:8080/nonexistent`.

---

#### **Scaling the Backend Service**
1. Scale the backend service to 3 instances:
   ```bash
   docker compose up --scale backend=3
   ```

2. Observe the container distribution:
   ```bash
   docker ps
   ```

3. Test load balancing (update Nginx config if required).

---

#### **Clean Up**
1. Stop and remove all containers, networks, and volumes:
   ```bash
   docker compose down -v
   ```

2. Optionally, remove built images:
   ```bash
   docker rmi python-backend
   ```

---

### **Learning Outcomes**
- Understand the structure of a `docker-compose.yml` file.
- Learn how to define and build services in Docker Compose.
- Explore service dependencies, volume mounts, and network configurations.
- Modify and restart services dynamically.
- Experiment with scaling and load balancing.
- Develop debugging and troubleshooting skills with Docker Compose.
