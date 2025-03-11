# Streamlit Chatbot with Ollama (LLaMA 3.2:1B) on Docker


## Prerequisites

- Docker installed on your system
- Basic knowledge of Docker commands

## 1. Build the Streamlit Chatbot Docker Image

### Build the Docker Image

Run the following command in the same directory as the `Dockerfile`:

```sh
docker build -t ai-chatbot .
```

## 2. Run Ollama on Docker

To run Ollama with the LLaMA 3.2:1B model, execute:

```sh
docker run -d --name ollama -p 11434:11434 ollama/ollama:latest
```

Pull and prepare the LLaMA 3.2:1B model:

```sh
docker exec -it ollama ollama pull llama3:1b
```

## 3. Run the Streamlit Chatbot Container

Once Ollama is running, start the chatbot container:

```sh
docker run -d --name ai-chatbot -p 8501:8501  streamlit-chatbot
```

Get the Container IP of the Ollama Container

Get the Container ID
```
docker ps
CONTAINER ID   IMAGE           COMMAND               CREATED          STATUS          PORTS                      NAMES
2cf4d51a43c9   ollama/ollama   "/bin/ollama serve"   2 minutes ago    Up 2 minutes    0.0.0.0:11434->11434/tcp   ollama
```
Get the IP 

In Windows 
```
docker inspect 2cf4d51a43c9 | findstr IPAddress
```
On Linux/Mac
```
docker inspect 2cf4d51a43c9 | grep IPAddress
```

## 4. Access the Chatbot

Open your browser and visit:

```
http://localhost:8501
```
Update the Backend URL

## 5. Stop and Remove Containers

To stop and remove all running containers:

```sh
docker stop ai-chatbot ollama && docker rm ai-chatbot ollama
```


