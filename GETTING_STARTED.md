# Getting Started

This guide walks you through setting up SpinToolkit and running your first spin-wave calculation.

---

## Step 1 — Prerequisites

Install one of the following container engines (only one is needed):

| Platform | Recommended Engine |
|---|---|
| Local (Linux/macOS/Windows) | [Docker](https://www.docker.com) or [Podman](https://podman.io) |
| HPC cluster | [Apptainer](https://apptainer.org) |

> **Podman users**: Podman supports standard Docker commands. To use them, you can create an alias (`alias docker=podman`) or, on Linux, install the `podman-docker` package to emulate the Docker CLI.

---

## Step 2 — Pull the Image

``` shell
docker pull ghcr.io/spintoolkit-dev/spintoolkit:1.6.0
```

Optionally, create a shorter tag:

``` shell
# Create the short alias
docker tag ghcr.io/spintoolkit-dev/spintoolkit:1.6.0 spintoolkit:1.6.0

# Remove the reference to the long name to clean up list
docker rmi ghcr.io/spintoolkit-dev/spintoolkit:1.6.0
```

> **Note 1**: The image is based on [Linux](https://en.wikipedia.org/wiki/Linux). To use SpinToolkit, some basic knowledge of [Linux Command-Line Tools](https://tldp.org/LDP/GNU-Linux-Tools-Summary/html/index.html) certainly helps.
> 
> **Note 2**: Older versions of SpinToolkit are also available at the [packages page](https://github.com/orgs/spintoolkit-dev/packages).
> 
> **Note 3**: If you find the download speed to be low, turning on proxy/vpn should help.
>
> **Note 4**: To download to Apptainer: `apptainer pull docker://ghcr.io/spintoolkit-dev/spintoolkit:1.6.0`


---

## Step 3 — Get the Tutorials

Through Git:
```shell
git clone https://github.com/spintoolkit-dev/SpinToolkit_py.git
```
or download the [zip file](https://github.com/spintoolkit-dev/SpinToolkit_py/archive/refs/heads/main.zip) and unzip it to your local machine.

---

## Step 4 — Run Your First Example

The fastest way to get started is via **Jupyter Notebook**. From the repo root:

```bash  
docker run --rm -it \
       -p 8880:8880 \
       -v ${PWD}/tutorials:/home/ubuntu/tutorials:z \
       -w /home/ubuntu/tutorials \
       spintoolkit:1.6.0 \
       jupyter-notebook --no-browser --ip=0.0.0.0 --port=8880 --allow-root  
```

> **Windows users**: Replace `<local_dir>:<container_dir>:z` with `<local_dir>:<container_dir>` (no `:z` flag).

Copy the printed URL (starting with `http://127.0.0.1:8880/...`) into your browser and open any tutorial notebook.

---

## Available Tutorials

| Tutorial                         | Topic                                                                                  |
|----------------------------------|----------------------------------------------------------------------------------------|
| `tutorial1_LSW_TL.ipynb`         | LSW for triangular lattice XXZ model with spin-1/2                                     |
| `tutorial2_GLSW_TL.ipynb`        | GLSW for triangular lattice XXZ+D model with spin-1                                    |
| `tutorial3_LSW_EOM_kagome.ipynb` | Spin wave of kagome lattice Heisenberg model with classical spin                       |
| `tutorial4_MC_honeycomb.ipynb`   | MC simulation of Ising model on honeycomb lattice                                      |
| `tutorial4_MC_honeycomb.py`      | MC simulation of Ising model on honeycomb lattice                                      |
| `tutorial5_MC_SUN_TL.ipynb`      | MC simulation with SU(N) coherent states on triangular lattice XXZ+D model with spin-1 |


---

## What's Next?

- 🐳 [Container Reference](CONTAINER_REF.md)
- 📖 [API Docs](https://spintoolkit-py.readthedocs.io/stable/)
- 💬 [Open an Issue](https://github.com/spintoolkit-dev/SpinToolkit_py/issues)