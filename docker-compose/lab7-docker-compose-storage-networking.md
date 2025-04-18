### Lab: Exploring Docker Compose Networking, Storage, and Secrets

This lab introduces Docker Compose's networking, storage, and secret management features. Participants will create a multi-service setup that demonstrates how to connect services, persist data using volumes, and securely share secrets across containers.

---


### **Lab Objectives**
- Learn how to configure custom Docker networks in Compose.
- Experiment with volume mounts for persistent storage.
- Understand Docker secrets and their use in a Compose setup.

---

### **Lab Setup**

#### **Step 1: Project Structure**
Create the following directory and file structure:
```bash
mkdir docker-compose-lab
cd docker-compose-lab

mkdir -p app db secrets
touch docker-compose.yml app/app.py db/init.sql
```

---

#### **Step 2: Populate the Files**

**`docker-compose.yml`**
```yaml
services:
  db:
    image: postgres:latest
    container_name: postgres-db
    ports:
     - "5432:5432"
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD_FILE: /run/secrets/db_password
    volumes:
      - db_data:/var/lib/postgresql/data
      - ./db/init.sql:/docker-entrypoint-initdb.d/init.sql:ro
    secrets:
      - db_password
    networks:
      - app-network

  app:
    build:
      context: ./app
    container_name: flask-app
    environment:
      DATABASE_URL: postgres://myuser:@postgres-db:5432/mydatabase
    volumes:
      - ./app:/usr/src/app
    networks:
      - app-network
    ports:
      - "5000:5000"
    depends_on:
      - db

volumes:
  db_data:

networks:
  app-network:

secrets:
  db_password:
    file: ./secrets/db_password.txt
```

Dockerfile

```
# syntax=docker/dockerfile:1
FROM ubuntu:22.04

# install app dependencies
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip install flask==3.0.*

# install app
COPY app.py /

# final configuration
ENV FLASK_APP=app
EXPOSE 8000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
```

**`app/app.py`**
```python
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Docker Compose Networking, Storage, and Secrets Lab!"

@app.route('/db')
def db_connection():
    db_url = os.getenv("DATABASE_URL", "No DB URL Found")
    return f"Database connection string: {db_url}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

**`db/init.sql`**
```sql
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

INSERT INTO users (name) 
VALUES 
    ('Alice'), 
    ('Bob'), 
    ('Charlie'), 
    ('David'), 
    ('Emma'), 
    ('Frank'), 
    ('Grace'), 
    ('Helen'), 
    ('Ivy'), 
    ('Jack'), 
    ('Karen'), 
    ('Leo'), 
    ('Mona'), 
    ('Nina'), 
    ('Oliver');

```

**`secrets/db_password.txt`**
```plaintext
supersecretpassword
```

---

### **Lab Instructions**

#### **Part 1: Networking**
1. **Start the Services**:
   ```bash
   docker compose up --build
   ```

2. **Inspect the Network**:
   ```bash
   docker network ls
   docker network inspect docker-compose-lab_app-network
   ```

3. **Test Network Connectivity**:
   - Access the Flask app at `http://localhost:5000`.
   - Use the `/db` endpoint to see the database connection string.

4. **Connect to the `db` Container**:
   ```bash
   docker exec -it postgres-db psql -U myuser -d mydatabase
   ```
   - Query the `users` table:
     ```sql
     SELECT * FROM users;
     ```

#### **Part 2: Storage**
1. **Check Persistent Data**:
   - Stop and remove the containers:
     ```bash
     docker compose down
     ```
   - Start the services again:
     ```bash
     docker compose up
     ```
   - Verify that the data in the `users` table is still intact (persistent storage).

2. **Inspect the Volume**:
   ```bash
   docker volume ls
   docker volume inspect docker-compose-lab_db_data
   ```

3. **Clean Up the Volume**:
   ```bash
   docker compose down -v
   ```

#### **Part 3: Secrets**
1. **Inspect Secrets**:
   - View the secret file used in the Compose file:
     ```bash
     cat secrets/db_password.txt
     ```

2. **Verify Secret Usage**:
   - Check the `db` container environment to confirm the secret is mounted:
     ```bash
     docker exec -it postgres-db env | grep POSTGRES_PASSWORD
     ```
   - The password itself won't appear in plain text because it's securely injected.

3. **Update the Secret**:
   - Modify the `db_password.txt` file with a new password.
   - Restart the `db` service to reflect the change:
     ```bash
     docker compose up -d
     ```

4. **Test with Incorrect Secrets**:
   - Intentionally break the secret or environment variable and observe the impact.

---

### **Lab Wrap-Up**

#### **Clean-Up**
To remove all containers, networks, volumes, and secrets created during the lab:
```bash
docker compose down --volumes --remove-orphans
```
