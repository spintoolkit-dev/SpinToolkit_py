# Container Reference

## Management Commands

For a full list of commands, see the [Docker Docs](https://docs.docker.com/reference/cli/docker/), [Podman Commands](https://docs.podman.io/en/latest/Commands.html), and [Apptainer Documentation](https://apptainer.org/documentation).

**Commonly used commands:**

- `docker images`: List all local images
- `docker rmi <image_id>`: Delete a specific image
- `docker ps -a`: List all containers (running and stopped)
- `docker rm <container_id>`: Delete a specific container
- `docker stop` or `docker start <container_name>`: Stop or start an existing container


## Running SpinToolkit

There are two ways to run SpinToolkit: keeping a container running in the background (Interactive Mode) or running a single script and exiting (Batch Mode).

### Method A: Interactive Mode (Keep an active container in the background)

First, start a container in the background. This shares your local folder with the container so you can save your work.

``` shell
docker run -dit \
       --name <container_name> \
       -p <port>:<port> \
       -v <local_dir>:<container_dir>:z \
       <image_name>
```
e.g.,
``` shell
docker run -dit \
       --name sptk_tutorials \
       -p 8880:8880 \
       -v ${PWD}/tutorials:/home/ubuntu/tutorials:z \
       spintoolkit:1.6.0
```
> **Note**: The `<local_dir>` should exist in your local machine (e.g., `tutorials` that was downloaded from this repo).

Once the container is running, you can use one of the workflows below:

- Workflow-A1: Jupyter Notebook

    1. **Enter the container**:

        ``` shell
        docker exec -it <container_name> /bin/bash
        # e.g., docker exec -it sptk_tutorials /bin/bash
        ```

    2. **Start Jupyter**:

        ``` shell
        jupyter-notebook --no-browser --ip=<ip> --port=<port> --allow-root
        # e.g., jupyter-notebook --no-browser --ip=0.0.0.0 --port=8880 --allow-root
        ```

    3. **Access**: Copy the generated URL into your host machine's browser.

    4. **Exit**: When finished, stop Jupyter (Ctrl+C) and type `exit` to leave the container.


- Workflow-A2: Run python scripts via shell

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

### Method B: Batch Mode (Run once and exit)

If you do not want to maintain a running container, you can use `docker run --rm`. This creates a temporary container, runs your script, and deletes the container immediately after the script finishes.

- Workflow-B1: Jupyter Notebook

    1. **Start Jupyter**:

        ``` shell
        docker run --rm -it \
               -p <port>:<port> \
               -v <local_dir>:<container_dir>:z \
               -w <container_workdir> \
               <image_name> \
               jupyter-notebook --no-browser --ip=<ip> --port=<port> --allow-root
        ```
        e.g.,
        ``` shell
        docker run --rm -it \
               -p 8880:8880 \
               -v ${PWD}/tutorials:/home/ubuntu/tutorials:z \
               -w /home/ubuntu/tutorials \
               spintoolkit:1.6.0 \
               jupyter-notebook --no-browser --ip=0.0.0.0 --port=8880 --allow-root
        ```

    2. **Access**: Copy the generated URL into your host machine's browser.

    3. **Exit**: When finished, stop Jupyter (Ctrl+C).

- Workflow-B2: Run python scripts via shell

    ``` shell
    docker run --rm -d \
           -v <local_dir>:<container_dir>:z \
           -w <container_workdir> \
           <image_name> \
           sh -c 'python3 <python_script> <input_arguments> > output.txt'
    ```
    e.g.,
    ``` shell
    docker run --rm -d \
           -v ${PWD}/tutorials:/home/ubuntu/tutorials:z \
           -w /home/ubuntu/tutorials \
           spintoolkit:1.6.0 \
           sh -c 'python3 /home/ubuntu/tutorials/tutorial4_MC_honeycomb.py --l 30 --J1 -1.0 --J2 1.5 --J3 0.5 --seed 0 --T 0.4 --T0 1.0 --max_sweeps 200000 --log_interval 50 --sweeps_per_dump 10000 > output.txt'
    ```

## Platform-Specific Notes
- **Windows**: 

    On Windows host, use `<local_dir>:<container_dir>` instead of `<local_dir>:<container_dir>:z` as the `:z` flag is for SELinux (Security Enhanced Linux).


- **Remote SSH + Podman**:

    When using Workflow-B2 in a remote Linux SSH session with Podman, make sure lingering is enabled for your user account: `loginctl show-user "$USER" -p Linger`. If the output is `Linger=no`, you should contact the administrator to enable it: `loginctl enable-linger "$USER"`; otherwise, your work will likely be killed when the SSH session is terminated.