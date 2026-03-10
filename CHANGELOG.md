# Changelog

## **SpinToolkit 1.6**

- v1.6.0 (02/03/2026)

    - **BREAKING**: Multiply prefactor 1/2π in definition of DSSF to be more consistent with classical inelastic neutron scattering textbooks.
    - **BREAKING**: Change type of `basis_a` and `pos_sub` in `Crystal` class to be more consistent with `lattice` class.
    - Include linear equation solver for self-adjoint matrices. 
    - Various minor improvements.

## **SpinToolkit 1.5**

- v1.5.1 (01/12/2026)

    - Improve numerical stability of Stevens matrices generation.

- v1.5.0 (01/07/2026)

    - **BREAKING**: Rename `coor2supercell0` to `r2superlattice`.
    - **BREAKING**: Rename `k2superBZ` to `k2superlattice`.
    - **BREAKING**: Change key `Mi` to `rtilde_i`, and `Mj` to `rtilde_j` in `add_2spin_Jmatrix`, `add_2spin_XYZ`, `add_2spin_DM`, `add_biquadratic`.
    - **BREAKING**: Change key `k_tilde` to `ktilde` in `generate_lsw_mat` and `generate_glsw_mat`.
    - **BREAKING**: Change key `Hmat` to `H_ktilde` in `Bogoliubov`.

## **SpinToolkit 1.4**

- v1.4.2 (01/02/2026)

    Initial release of Docker image.