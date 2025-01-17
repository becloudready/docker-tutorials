### **Assignment: Understanding `CMD`, `RUN`, and `ENTRYPOINT`**

**Objective**: Build a Docker image that demonstrates the use of `CMD`, `RUN`, and `ENTRYPOINT` directives effectively and understand their differences.

---

####  Build a Custom Docker Image**
1. Create a directory named `custom-nginx`.
2. Inside the directory, create a `Dockerfile` with the following content:
   ```dockerfile
   FROM nginx:latest
   COPY index.html /usr/share/nginx/html/index.html
   ```
3. Add a custom `index.html` file to the same directory. Use the following content for `index.html`:
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>Custom Nginx</title>
   </head>
   <body>
       <h1>Welcome to My Custom Nginx!</h1>
       <p>This page is served from a custom Docker image built by you.</p>
   </body>
   </html>
   ```
4. Build a new Docker image with the command:
   ```bash
   docker build -t custom-nginx .
   ```

---

#### Run a Container from the Custom Image**
1. Run a container using the newly built `custom-nginx` image and expose it on port 9090:
   ```bash
   docker run -d -p 9090:80 custom-nginx
   ```
2. Open a web browser and visit `http://localhost:9090` to verify the custom nginx page is displayed.

---

#### Push the Image to Docker Hub**
1. Log in to Docker Hub using the `docker login` command:
   ```bash
   docker login
   ```
2. Tag your custom image to match your Docker Hub repository:
   ```bash
   docker tag custom-nginx <your-dockerhub-username>/custom-nginx
   ```
3. Push the image to Docker Hub:
   ```bash
   docker push <your-dockerhub-username>/custom-nginx
   ```
4. Verify the image is successfully uploaded by checking your Docker Hub account.


---
#### **Scenario**
You are tasked with creating a Docker container for a simple Python application that performs mathematical calculations. The application should allow users to provide arguments at runtime to customize the calculations.

#### **Steps**

1. **Create a Python Script**
   Write a Python script (`calculator.py`) that can perform basic arithmetic operations (addition, subtraction, multiplication, and division).  
   The script should accept arguments from the command line.

   ```python
   # calculator.py
   import sys

   def main():
       if len(sys.argv) != 4:
           print("Usage: python calculator.py <operation> <num1> <num2>")
           sys.exit(1)

       operation = sys.argv[1]
       num1 = float(sys.argv[2])
       num2 = float(sys.argv[3])

       if operation == "add":
           print(f"The result is: {num1 + num2}")
       elif operation == "substract":
           print(f"The result is: {num1 - num2}")
       elif operation == "multiply":
           print(f"The result is: {num1 * num2}")
       elif operation == "divide":
           if num2 != 0:
               print(f"The result is: {num1 / num2}")
           else:
               print("Error: Division by zero.")
       else:
           print("Error: Unsupported operation.")

   if __name__ == "__main__":
       main()
   ```

2. **Write the Dockerfile**
   Create a Dockerfile that demonstrates the use of `RUN`, `CMD`, and `ENTRYPOINT`.

   ```dockerfile
   # Use Python as the base image
   FROM python:3.10-slim

   # Set the working directory inside the container
   WORKDIR /app

   # Copy the Python script into the container
   COPY calculator.py /app/

   # Install any dependencies (if needed)
   # Using RUN to demonstrate execution at build time
   RUN echo "Building the Docker image and setting up the environment..."

   # Use ENTRYPOINT to ensure the script is always run with Python
   ENTRYPOINT ["python", "calculator.py"]

   # Set a default CMD for the container
   CMD ["add", "10", "20"]
   ```

3. **Build the Docker Image**
   Build the Docker image with a suitable tag.

   ```bash
   docker build -t calculator .
   ```

4. **Run the Container**
   Run the container with and without overriding the default `CMD`.

   - **Default CMD**:
     ```bash
     docker run calculator
     ```
     This should perform the default addition operation (10 + 20).

   - **Override CMD**:
     ```bash
     docker run calculator subtract 30 10
     ```
     This should perform the subtraction operation (30 - 10).

5. **Experiment with ENTRYPOINT**
   Try overriding the `ENTRYPOINT` and see what happens:

   ```bash
   docker run --entrypoint echo calculator "Overriding entrypoint"
   ```
   This should override the `ENTRYPOINT` and print "Overriding entrypoint".

6. **Document the Observations**
   Answer the following questions:
   - What happens when `CMD` is overridden?
   - What happens when `ENTRYPOINT` is overridden?
   - Why use `CMD` and `ENTRYPOINT` together?

---

#### **Deliverables**
1. Dockerfile with properly configured `CMD`, `RUN`, and `ENTRYPOINT`.
2. Screenshots or logs of running the container with various configurations.
3. Written observations and answers to the provided questions.

