# Python Docker Container for RWD scripts

This repository contains a [Docker](docker.com) container designed as sandboxes for Remote WebDriver
clients written in Python.

# Building and Running locally
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
git submodule update --init
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
going on and debug the image. Use the following command to start a container in interactive mode:
```
docker run -i -t IMAGE_NAME /bin/bash
```

# Running on AWS
## Requirements

### Python
Install the python requirements:
```
pip install --no-cache-dir -r requirements-aws.txt
```

### AWS
Setup the AWS by downloading the Amazon AWS Command Line Interface tools and
configuring it as explained [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).

You'll need an AWS account. Currently, the AWS runner script assumes that you
have an ECS cluster named 'sum-dev' and an ECS task named 'rwd-python'.
TODO: describe the configuration of the AWS task and add parameters to specify
different cluster and task names


