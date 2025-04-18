# Streamlit Chatbot with Ollama (LLaMA 3.2:1B) on Docker

![ai chatbot docker](https://github.com/user-attachments/assets/54c784f2-b3c4-4270-81b7-9b2e5a10e2d6)

## Prerequisites

- Docker installed on your system
- Basic knowledge of Docker commands

## Build the Streamlit Chatbot Docker Image

### Build the Docker Image

Run the following command in the same directory as the `Dockerfile`:

```sh
docker build -t ai-chatbot .
```

## Run Ollama on Docker

To run Ollama with the LLaMA 3.2:1B model, execute:

```sh
docker run -d --name ollama -p 11434:11434 ollama/ollama:latest
```
If you have GPU in your machine then use

```sh
docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

Pull and prepare the LLaMA 3.2:1B model:

```sh
docker exec -it ollama ollama pull llama3.2:1b
```

## Run the Streamlit Chatbot Container

Once Ollama is running, start the chatbot container:

```sh
docker run -d --name ai-chatbot -p 8501:8501  ai-chatbot
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

## Access the Chatbot

Open your browser and visit:

```
http://localhost:8501
```
Update the Backend URL

![image](https://github.com/user-attachments/assets/8e8b9004-a072-47be-b9c5-f314eda6ef8a)


### Check if Ollama is serving your model

For CPU Only 
```
docker exec ollama ollama ps
NAME           ID              SIZE      PROCESSOR    UNTIL
llama3.2:1b    baf6a787fdff    2.2 GB    100% CPU     4 minutes from now
```
With GPU support

```
docker exec ollama ollama ps
NAME           ID              SIZE      PROCESSOR    UNTIL
llama3.2:1b    baf6a787fdff    2.7 GB    100% GPU     4 minutes from now
```

## Stop and Remove Containers

To stop and remove all running containers:

```sh
docker stop ai-chatbot ollama && docker rm ai-chatbot ollama
```


