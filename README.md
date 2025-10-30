# SpinToolkit_py

This repository provides the user-facing documentation and python tutorials of the **SpinToolkit** library.

If you use **SpinToolkit** in your research, please cite our paper: [Super-lattice framework for spin wave theory I: single-particle excitations, multi-magnon continua, and finite-temperature effects](.....)

SpinToolkit is a high-performance **Toolkit for simulating Spin systems**, including

- Linear/Nonlinear spin wave (Holstein-Primakoff approach)
- Generalized Linear/Nonlinear spin wave (SU(N) coherent state approach)
- Linear spin wave (Monte-Carlo + Equation-of-Motion approach)
- Various Monte-Carlo updates
- Landau-Lifshitz dynamics
- Symmetry Analysis of interactions for any given crystal

:tada: :tada: :tada: The Python API of **SpinToolkit** is now available as Docker [images](https://github.com/orgs/spintoolkit-dev/packages) on the [GitHub Container Registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry)!!!

## Docker/Podman (Linux/MacOS/Windows)

Using [Docker](https://www.docker.com/products/docker-hub/) or [Podman](https://podman.io/) is a convenient way to run the _SpinToolkit_ library without spending effort installing all the dependencies, and is recommended to all users. These two softwares share almost identical usage, so converting from one to another is painless. In fact, if you are using Podman in systems like Ubuntu, you can install the tool `podman-docker` and continue to use Docker syntax where `docker` is really `podman` in disguise. Alternatively, you can `alias docker=podman` to use Docker syntax with Podman engine.

**Note** : you will run image as a `root` user with **working directory** set to `/home/ubuntu`

### Installation
1. To start, you should [install Docker](https://docs.docker.com/get-started/get-docker) or [install Podman](https://podman.io/).

2. Download the image on from [packages page](https://github.com/orgs/spintoolkit-dev/packages).

    ``` shell
    docker pull ghcr.io/spintoolkit-dev/spintoolkit:<image_tag>
    #e.g., docker pull ghcr.io/spintoolkit-dev/spintoolkit:1.2.0
    ```

  **Note**: check the version you want to download in the website above.

3. creates a simple alias for easy use, like a shortcut for the image, which do not copy any data or take up extra space

    ``` shell
    docker tag ghcr.io/spintoolkit-dev/spintoolkit:<image_tag> spintoolkit:<image_tag>
    #e.g., docker tag ghcr.io/spintoolkit-dev/spintoolkit:1.2.0 spintoolkit:1.2.0
    ```

### Usage
Full list of docker commands can be found in [Docker Docs](https://docs.docker.com/reference/cli/docker/) or [Podman Commands](https://docs.podman.io/en/latest/Commands.html).

A few commonly used commands to manage images and containers:
- `docker images`: list the images
- `docker rmi <image_id>`: remove the image
- `docker ps -a`: list the containers
- `docker rm <container_id>`: remove the container
- `docker attach <container_name> (or <container_id>)`: attach to (enter) a running container
- `docker stop|start <container_name> (or <container_id>)`: stop or start an existing container

#### general usage
- To run a container in the background, with files shared between a local directory and a container directory:

  ``` shell
  docker run --name <container_name> -p <port>:<port> -it -d -v <local_dir>:<container_dir> <image_name>
  #e.g., docker run --name sptk_tutorials -p 8880:8880 -it -d -v ./tutorials_py:/home/ubuntu/tutorials_py spintoolkit:v1.0.5
  ```

- To exit and stop a container, simply type `exit` inside the terminal of the container.

- To exit without stopping a container, use keyboard shortcut `ctrl+p+q` (hold `ctrl`, then press `p`, then press `q`).

#### running jupyter notebook

- Run jupyter notebook in container:
  ``` shell
  jupyter-notebook --port=<port> --ip=<ip>
  #e.g., jupyter-notebook --port=8880 --ip=0.0.0.0
  ```

- paste the produced url into your host machine's browser.

#### python scripts

- Run python scripts in container is straightforward:

  ``` shell
  python3 <script_name> <input_arguments>
  #e.g., python3 tutorial4_MC_honeycomb.py \
  #              --L 30 --J1 -1.0 --J2 1.5 --J3 0.5 --seed 0 --kT 0.4 \
  #              --kT0 1.0 --max_sweeps 200000 --log_interval 50 \
  #              --sweeps_per_dump 10000
  ```

- Run python scripts without entering a container (No Attach):

  ``` shell
  podman run --rm \
         -v <local_dir>:<container_dir>:z \
         -w <container_workdir> <image_name> \
         python3 <python_script> \
         <input_arguments> &
  #e.g., podman run --rm \
  #             -v ./tutorials_py:/home/ubuntu/tutorials_py:z \
  #             -w /home/ubuntu/tutorials_py spintoolkit:1.2.0 \
  #             python3 /home/ubuntu/tutorials_py/tutorial4_MC_honeycomb.py \
  #             --L 30 --J1 -1.0 --J2 1.5 --J3 0.5 --seed 0 --kT 0.4 \
  #             --kT0 1.0 --max_sweeps 200000 --log_interval 50 \
  #             --sweeps_per_dump 10000 &
  ```

## Version

### v1.2.0

The initial release version of image

## FAQ:

1. **From python, how can I check the definition of a function/class from SpinToolkit?**

    **A**: After importing the library by `import SpinToolkit_py as sptk`, the `help` function can be used to show the full docstring.

   For instance, `help(sptk)` shows all available classes/function, and `help(sptk.date_and_time)` shows the definition of the `date_and_time` function.

   Alternatively, if you are using IPython or Jupyter, `sptk.date_and_time?` should also work.
