# Python Docker Container for RWD scripts

This repository contains a [Docker](docker.com) container designed as sandboxes for Remote WebDriver
clients written in Python.

## Requirements
Docker installation instructions depend on your system, see [docs.docker.com](docs.docker.com).

Mac users may want to use [Kitematic](kitematic.com), which is the simplest way to install and setup Boot2Docker. 
Boot2Docker uses VirtualBox to host a Linux VM for your docker containers (which itself will be used to host your running containers).

Since Kitematic is wrapping up Boot2Docker, you will need to add the following lines to your ```.profile``` in order to use the ```docker``` command line tools:
```
# Boot2Docker configuration
eval "$(docker-machine env dev)"
```

## Building
```
git submodule init
docker build -t appdynamics/rwd-python .
```

## Running
Setup your environment as defined in ```client/README.md```, then use the
```run.sh``` wrapper script to execute the client within Docker:

```
./run python singleurl.py chrome http://appdynamics.com
```

## Debugging
It is sometimes necessary to log-in to the container in order to see what's
going on and debug the image. Use the folloing command to start a container in interactive mode:
```
docker run -i -t IMAGE_NAME /bin/bash
```
