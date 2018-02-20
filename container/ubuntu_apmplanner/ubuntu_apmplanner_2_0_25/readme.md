# APM Planner 2.0.25 Container

This container allows to run the APM Planner2.0.25 graphical control software for ArduPilot controllers/ UAV's.

## Build container

Since this container is not available on docker hub it must be build on the local machine:

```
./build_container.sh
```

## Run APM Planner 2

The run script will automatically start the APM planner 2 in a container.
The current GIT repository is automatically mountend as /git-repo/ to allow access to local files.

*Since this container runs in --privileged mode and the run sript enables access to the X-Server please check the source code and only execute if you trust the code*

```
./run_container.sh
```