
## Install Ollama on Linux

```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```

```
Unable to find image 'ollama/ollama:latest' locally
latest: Pulling from ollama/ollama
6414378b6477: Pull complete
9423a26b200c: Pull complete
629da9618c4f: Pull complete
00b71e3f044c: Pull complete
Digest: sha256:18bfb1d605604fd53dcad20d0556df4c781e560ebebcd923454d627c994a0e37
Status: Downloaded newer image for ollama/ollama:latest
2352d454e7117a79459cd7d1413e686680a80927494ff6dbd70faebd3dcfabb0
```

## Pull Llama 3.2:1b Model

```
curl http://localhost:11434/api/pull -d '{
  "model": "llama3.2:1b"
}'
```

```
docker exec -it ollama ollama ls
```

## Test if the model is serving

```
curl http://localhost:11434/api/chat -d '{
  "model": "llama3.2:1b",
  "messages": [
    {
      "role": "user",
      "content": "Where is Paris"
    }
  ],
  "stream": false
}'
```

```
docker exec -it ollama ollama ps
NAME           ID              SIZE      PROCESSOR    UNTIL
llama3.2:1b    baf6a787fdff    2.2 GB    100% CPU     4 minutes from now
```


## Clone the AI Application

Fork the Github Repo - https://github.com/db-agent/db-agent

```
git clone https://github.com/db-agent/db-agent.git

```

## Build and deploy the App

```
cd db-agent
docker compose -f docker-compose.local.yml build
docker compose -f docker-compose.local.yml up -d
# Check logs
docker compose -f docker-compose.local.yml logs -f


```

