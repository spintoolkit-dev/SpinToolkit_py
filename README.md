# SpinToolkit

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18948515.svg)](https://doi.org/10.5281/zenodo.18948515)
[![License](https://img.shields.io/badge/license-BSD--3--Clause-blue)](https://opensource.org/licenses/BSD-3-Clause)
[![Docs](https://readthedocs.org/projects/spintoolkit-py/badge/?version=stable)](https://spintoolkit-py.readthedocs.io/stable/)

SpinToolkit is a high-performance toolkit for simulating spin systems, including the following key functionalities:

- Linear spin wave (LSW) calculations based on Holstein-Primakoff bosons
- Generalized linear spin wave (GLSW) calculations based on SU(<i>N</i>) coherent state and Schwinger bosons
- Monte-Carlo sampling of spin dipoles or SU(<i>N</i>) coherent states
- Landau-Lifshitz dynamics
- Linear spin wave (LSW) based on Monte-Carlo sampling + Equation of motion approach
- ...

## Documentation

- 🚀 [Getting Started](GETTING_STARTED.md)
- 🐳 [Container Reference](CONTAINER_REF.md)
- 📖 [API Docs](https://spintoolkit-py.readthedocs.io/stable/)

**Quick example — launch a Jupyter Notebook session:**

```bash  
docker run --rm -it \
       -p 8880:8880 \
       -v ${PWD}/tutorials:/home/ubuntu/tutorials:z \
       -w /home/ubuntu/tutorials \
       spintoolkit:1.6.0 \
       jupyter-notebook --no-browser --ip=0.0.0.0 --port=8880 --allow-root
```

Copy the printed URL into your browser to access the notebook. See the [Getting Started](GETTING_STARTED.md) for a full walkthrough.


## Citing

If you used SpinToolkit in your research, please cite us:

```bibtex
@misc{sptk,
  author = {{SpinToolkit Developers}},
  title  = {{SpinToolkit}},
  year   = {2026},
  doi    = {10.5281/zenodo.18948515},
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
