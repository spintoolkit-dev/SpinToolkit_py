[ Purpose ]
This folder includes a few hand-made lattices for use.
Put it more precisely, regular lattices with special "magnetic unit cell".

You can also use these examples to help design lattices for your special needs.

The purpose of having these examples is self-clear from the following example:

Consider having a nearest neighbor AFM Heisenberg model on triangular lattice.
The ground state is the conventional 120 degree order.
To obtain this state, you should use a unit cell that is compatible with this structure.
An obvious choice is to use a 3x3 cell, however it is not the minimal one.
While 3x3 can still give you a lot of useful information, e.g.
1. The correct ground state,
2. The correct diffraction and inelastic neutron spectrum.
It has a few drawbacks:
1. Computational speed is slower compared to using the true minimal cell
2. The choice of large cell creates extra BZ folding. As a result,
   the number of excitation branches may not be easily counted.
These problems can be avoided if we use a minimal, special cell, spanned by the super-cell basis:
A0 = 2 * a0 + 1 * a1,
A1 = 1 * a0 + 2 * a1,
where a0 = [1, 0], a1 = [-1/2, sqrt(3)/2].
Here by "special" we meant that A0 (A1) is not parallel to a0 (a1).


[ How to use ]
For example, to use the lattice defined in "xxx.toml", simply call:
```
auto latt = sptl::lattice("triangular_K.toml");     // c++
```

or

```
latt = sptk.lattice(filename = "triangular_K.toml") # python
```
