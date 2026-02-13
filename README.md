# SpinToolkit

SpinToolkit is a high-performance toolkit for simulating spin systems, including the following key functionalities:

- Linear spin wave (LSW) calculations based on Holstein-Primakoff bosons
- Generalized linear spin wave (GLSW) calculations based on SU(<i>N</i>) coherent state and Schwinger bosons
- Monte-Carlo sampling of spin dipoles or SU(<i>N</i>) coherent states
- Landau-Lifshitz dynamics
- Linear spin wave (LSW) based on Monte-Carlo sampling + Equation of motion approach
- ...

## Documentation and Tutorials

- The Python API documentation for SpinToolkit can be found at the [Documentation Website](https://spintoolkit-py.readthedocs.io/stable/).


- Tutorials are available in the `tutorials` folder. To try out these examples, you can 
    ``` shell
    git clone git@github.com:spintoolkit-dev/SpinToolkit_py.git
    ```
    or download the [zip file](https://github.com/spintoolkit-dev/SpinToolkit_py/archive/refs/heads/main.zip) and unzip it to your local machine.

## Download

1. **Prerequisite**: Install [Docker](https://www.docker.com) **or** [Podman](https://podman.io) (on local computer); or use [Apptainer](https://apptainer.org) (on HPC).

   These containerization tools offer convenient ways to run SpinToolkit on different operating systems (Linux/Mac/Win), and they share very similar usages. 

   > **Note to Podman users**: Podman supports standard Docker commands. To use them, you can create an alias (`alias docker=podman`) or, on Linux, install the `podman-docker` package to emulate the Docker CLI.

2. **Download Image**: Pull the SpinToolkit image from the command line.

    ``` shell
    docker pull ghcr.io/spintoolkit-dev/spintoolkit:<image_tag>
    #e.g., docker pull ghcr.io/spintoolkit-dev/spintoolkit:1.6.0
    ```

   > **Note 1**: Older versions of SpinToolkit are also available at the [packages page](https://github.com/orgs/spintoolkit-dev/packages).
   > 
   > **Note 2**: If you find the download speed to be low, turning on proxy/vpn should help.
   >
   > **Note 3**: To download to Apptainer: `apptainer pull docker://ghcr.io/spintoolkit-dev/spintoolkit:<image_tag>`

3. **Shorten Image Name (Optional)**: The default image name is long. You can create a shorter alias (tag) to make future commands easier to type.

    ``` shell
    # Create the short alias
    docker tag ghcr.io/spintoolkit-dev/spintoolkit:<image_tag> spintoolkit:<image_tag>
    # e.g., docker tag ghcr.io/spintoolkit-dev/spintoolkit:1.6.0 spintoolkit:1.6.0

    # (Optional) Remove the reference to the long name to clean up list
    docker rmi ghcr.io/spintoolkit-dev/spintoolkit:<image_tag>
    # e.g., docker rmi ghcr.io/spintoolkit-dev/spintoolkit:1.6.0
    ```

## Docker/Podman/Apptainer Reference

### Management Commands

For a full list of commands, see the [Docker Docs](https://docs.docker.com/reference/cli/docker/), [Podman Commands](https://docs.podman.io/en/latest/Commands.html), and [Apptainer Documentation](https://apptainer.org/documentation).

**Commonly used commands:**

- `docker images`: List all local images
- `docker rmi <image_id>`: Delete a specific image
- `docker ps -a`: List all containers (running and stopped)
- `docker rm <container_id>`: Delete a specific container
- `docker stop` or `docker start <container_name>`: Stop or start an existing container


### Running SpinToolkit

There are two ways to run SpinToolkit: keeping a container running in the background (Interactive Mode) or running a single script and exiting (Batch Mode).

#### Method A: Interactive Mode (Recommended)

First, start a container in the background. This shares your local folder with the container so you can save your work.

``` shell
docker run --name <container_name> -p <port>:<port> -it -d -v <local_dir>:<container_dir>:z <image_name>
# e.g., docker run --name sptk_tutorials -p 8880:8880 -it -d -v ${PWD}/tutorials:/home/ubuntu/tutorials:z spintoolkit:1.6.0
```
> **Note 1**: The `<local_dir>` should exist in your local machine (e.g., `tutorials` that was downloaded from this repo).
> 
> **Note 2**: On Windows host, use `<local_dir>:<container_dir>` instead of `<local_dir>:<container_dir>:z` as the `:z` flag is for SELinux (Security Enhanced Linux).

Once the container is running, you can use one of the workflows below:

- Workflow-A1: Jupyter Notebook

    1. **Enter the container**:

        ``` shell
        docker exec -it <container_name> /bin/bash
        # e.g., docker exec -it sptk_tutorials /bin/bash
        ```

    2. **Start Jupyter**:

        ``` shell
        jupyter-notebook --allow-root --port=<port> --ip=<ip>
        # e.g., jupyter-notebook --allow-root --port=8880 --ip=0.0.0.0
        ```

    3. **Access**: Copy the generated URL into your host machine's browser.

    4. **Exit**: When finished, stop Jupyter (Ctrl+C) and type `exit` to leave the container.


- Workflow-A2: Run Python Scripts via Shell

    1. **Enter the container**:

        ``` shell
        docker exec -it <container_name> /bin/bash
        # e.g., docker exec -it sptk_tutorials /bin/bash
        ```

    2. **Run your script**:

        ``` shell
        python3 <script_name> <input_arguments>
        # e.g., python3 tutorial4_MC_honeycomb.py --l 30 --J1 -1.0 --J2 1.5 --J3 0.5 --seed 0 --T 0.4 --T0 1.0 --max_sweeps 200000 --log_interval 50 --sweeps_per_dump 10000
        ```

    3. **Exit**: Type `exit` to leave the container.

#### Method B: Batch Mode (Run once and exit)

If you do not want to maintain a running container, you can use `docker run --rm`. This creates a temporary container, runs your script, and deletes the container immediately after the script finishes.

``` shell
docker run --rm \
       -v <local_dir>:<container_dir>:z \
       -w <container_workdir> <image_name> \
       python3 <python_script> \
       <input_arguments>
# e.g., docker run --rm -v ./tutorials:/home/ubuntu/tutorials:z -w /home/ubuntu/tutorials spintoolkit:1.6.0 python3 /home/ubuntu/tutorials/tutorial4_MC_honeycomb.py --l 30 --J1 -1.0 --J2 1.5 --J3 0.5 --seed 0 --T 0.4 --T0 1.0 --max_sweeps 200000 --log_interval 50 --sweeps_per_dump 10000
```

> **Note**: On Windows host, use `<local_dir>:<container_dir>` instead of `<local_dir>:<container_dir>:z` as the `:z` flag is for SELinux (Security Enhanced Linux).

## Changelog

- **v1.6.0** (02/03/2026)

    - **BREAKING**: Multiply prefactor 1/2π in definition of DSSF to be more consistent with classical inelastic neutron scattering textbooks.
    - **BREAKING**: Change type of `basis_a` and `pos_sub` in `Crystal` class to be more consistent with `lattice` class.
    - Include linear equation solver for self-adjoint matrices. 
    - Various minor improvements.

- **v1.5.1** (01/12/2026)

    Improve numerical stability of Stevens matrices generation.

- **v1.5.0** (01/07/2026)

    - **BREAKING**: Rename `coor2supercell0` to `r2superlattice`.
    - **BREAKING**: Rename `k2superBZ` to `k2superlattice`.
    - **BREAKING**: Change key `Mi` to `rtilde_i`, and `Mj` to `rtilde_j` in `add_2spin_Jmatrix`, `add_2spin_XYZ`, `add_2spin_DM`, `add_biquadratic`.
    - **BREAKING**: Change key `k_tilde` to `ktilde` in `generate_lsw_mat` and `generate_glsw_mat`.
    - **BREAKING**: Change key `Hmat` to `H_ktilde` in `Bogoliubov`.

- **v1.4.2** (01/02/2026)

    Initial release of Docker image.

## Citing

If you find SpinToolkit useful, please cite this paper:

```bibtex
@misc{sptk,
author = {Xu, L. and Shi, X. and Jiao, Y. and Yang, J. and Yang, L. and Wang, Z.},
title = {In preparation},
year = {2026}
}
```
