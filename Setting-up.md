This "guide" assumes that you cloned the repository on your machine and that you have Docker, docker-compose and appropriate CUDA drivers installed if you wish to leverage your GPU for inference.

## Linux
1. On the first run, `docker-compose up` should configure the FastAPI app and PostgreSQL. Uvicorn options are set to `reload=True`, so any code changes you make on your host machine will be automatically applied to the container.

**NOTE:** If you have an appropriate NVIDIA GPU that you want to use, run `docker-compose -f docker-compose_nvidia-gpu.yaml up` instead. Remember to [install nvidia-container-runtime](https://docs.docker.com/config/containers/resource_constraints/#gpu) on your host machine.

2. Run `docker-compose run web alembic upgrade head` to create db tables if you're setting up, or to apply migrations if you made any db schema changes.

## Windows
This is assuming that you're using Docker for Desktop Windows.
1. Follow the steps from the Linux guide.
2. Curl up into a ball because you're not using a Unix system.
3. If you want to use your GPU, good luck. Refer to [Docker](https://docs.docker.com/desktop/windows/wsl/#gpu-support) and [NVIDIA's guide](https://docs.nvidia.com/cuda/wsl-user-guide/index.html) to set up CUDA for WSL.