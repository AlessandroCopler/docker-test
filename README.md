# docker-test

## Useful commands

To clear everything:

```
docker system prune -a
```

To build (using another dockerfile):

```
docker build ./ --file DockerfileFlask -t alessa90/public:x
```

To see listed builded images:

```
docker image ls
```

To push:

```
docker push alessa90/public:x
```

To run (mapping docker port 80 to local port 8080)

```
docker run -p 8080:80 alessa90/public:x
```