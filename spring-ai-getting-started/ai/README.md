# Spring AI Lab

This repo is a result of my journey reading the [Spring AI Documentation](https://spring.io/projects/spring-ai)

### Chat Client 

```
curl --get --data-urlencode 'input=Create a summary about Brazil.' http://localhost:8080/chat/client/call
curl --get -N --data-urlencode 'input=Create a summary about Brazil.' http://localhost:8080/chat/client/stream
curl --data '{"input": "Tell my a joke"}' -H "Content-type: application/json"  http://localhost:8080/chat/client

curl --get http://localhost:8080/chat/client/actor
curl --get http://localhost:8080/chat/client/actors

curl --get http://localhost:8080/chat/client/actors/stream
```

### Chat History

```
curl --get --data-urlencode 'input=My name is Johni.' http://localhost:8080/chat/history
curl --get --data-urlencode 'input=What is my name?' http://localhost:8080/chat/history
```

### Chat Model

```
curl --get --data-urlencode 'input=Tell my a joke about dogs.' http://localhost:8080/chat/model
```

### Chat Client Request

```
curl --get --data-urlencode 'input=Tell my a joke about cats.' http://localhost:8080/chat/client/request
```

### Chat Prompts

```
curl --get --data-urlencode 'artist=Gustavo Lima.' http://localhost:8080/chat/prompt/songs
curl --get 'http://localhost:8080/chat/prompt/author/Paulo%20Coelho'
```

## TODO 

- Configuration: https://github.com/rd-1-2022/ai-openai-helloworld/blob/main/src/main/java/org/springframework/ai/openai/samples/helloworld/Config.java

