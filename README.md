# SpinToolkit

![License](https://img.shields.io/badge/license-BSD--3--Clause-blue)
![Docs](https://readthedocs.org/projects/spintoolkit-py/badge/?version=stable)

SpinToolkit is a high-performance toolkit for simulating spin systems, including the following key functionalities:

- Linear spin wave (LSW) calculations based on Holstein-Primakoff bosons
- Generalized linear spin wave (GLSW) calculations based on SU(<i>N</i>) coherent state and Schwinger bosons
- Monte-Carlo sampling of spin dipoles or SU(<i>N</i>) coherent states
- Landau-Lifshitz dynamics
- Linear spin wave (LSW) based on Monte-Carlo sampling + Equation of motion approach
- ...

## Getting Started

For a step-by-step introduction to SpinToolkit, see the [Getting Started Guide](GETTING_STARTED.md).

## Documentation

The Python API documentation for SpinToolkit can be found at the [Documentation Website](https://spintoolkit-py.readthedocs.io/stable/).

## Container Reference

SpinToolkit runs inside a Docker/Podman/Apptainer container. For the full list of 
workflows, see the 
[Container Reference](CONTAINER_REF.md).

**Quick example** (Batch mode, Jupyter):
```bash  
docker run --rm -it \
       -p 8880:8880 \
       -v ${PWD}/tutorials:/home/ubuntu/tutorials:z \
       -w /home/ubuntu/tutorials \
       spintoolkit:1.6.0 \
       jupyter-notebook --no-browser --ip=0.0.0.0 --port=8880 --allow-root
```


## Citing

If you used SpinToolkit in your research, please cite us:

```bibtex
@misc{sptk,
  author = {{SpinToolkit Developers}},
  title  = {SpinToolkit},
  year   = {2026},
  url    = {https://github.com/spintoolkit-dev/SpinToolkit_py}
}
```

To reference the LSW/GLSW calculations, please also include:

```bibtex
@article{XuL2026,
  author = {Xu, L. and Shi, X. and Jiao, Y. and Yang, J. and Yang, L. and Wang, Z.},
  title  = {In preparation},
  year   = {2026}
}
```
