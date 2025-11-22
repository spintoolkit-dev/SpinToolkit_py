# Tutorial-4: Monte Carlo simulation of Ising model on honeycomb lattice

import numpy as np
import os
import shutil
import SpinToolkit_py as sptk
import argparse

parser = argparse.ArgumentParser(description="Monte Carlo simulation of the Ising model on a honeycomb lattice.")

# Add arguments
parser.add_argument('--L', type=int, default=30, help='Lattice size')

parser.add_argument('--J1', type=float, default=-1.0, help='J1 interaction')
parser.add_argument('--J2', type=float, default=1.5, help='J2 interaction')
parser.add_argument('--J3', type=float, default=0.5, help='J3 interaction')


parser.add_argument('--seed', type=int, default=0, help='Random seed for the simulation.')
parser.add_argument('--kT', type=float, default=0.4, help='Final temperature (in units of J).')
parser.add_argument('--kT0', type=float, default=1.0, help='Initial temperature for annealing.')

parser.add_argument('--max_sweeps', type=int, default=200000, help='Total number of Monte Carlo sweeps.')
parser.add_argument('--log_interval', type=int, default=50, help='Frequency of measurements.')
parser.add_argument('--sweeps_per_dump', type=int, default=10000, help='Frequency of taking snapshots.')

args = parser.parse_args()


# Define a honeycomb lattice to be used

L = args.L
sptk.print_system_info()
latt = sptk.lattice(name = "honeycomb", L = [L, L])

# Define the model and include magnetic couplings

J1 = args.J1
J2 = args.J2
J3 = args.J3

hamiltonian = sptk.model_spin(S = 0.5, mode = "dipole", lattice = latt)
print()

Nsites = latt.Nsites()
for site_i in range(Nsites):
    coor_i, sub_i = latt.site2coor(site = site_i)
    coor0_i, Mi   = latt.coor2supercell0(coor = coor_i)
    xi = coor_i[0]
    yi = coor_i[1]

    # J1 terms
    if sub_i == 0:
        coor_j      = [xi, yi]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J1),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

        coor_j      = [xi - 1, yi]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J1),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

        coor_j      = [xi - 1, yi - 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J1),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

    # J2 terms
    coor_j      = [xi + 1, yi]
    coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
    site_j      = latt.coor2site(coor = coor_j, sub = sub_i)
    hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J2),
                                      site_i = site_i, site_j = site_j,
                                      Mi = Mi, Mj = Mj)

    coor_j      = [xi + 1, yi + 1]
    coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
    site_j      = latt.coor2site(coor = coor_j, sub = sub_i)
    hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J2),
                                      site_i = site_i, site_j = site_j,
                                      Mi = Mi, Mj = Mj)

    coor_j      = [xi, yi + 1]
    coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
    site_j      = latt.coor2site(coor = coor_j, sub = sub_i)
    hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J2),
                                      site_i = site_i, site_j = site_j,
                                      Mi = Mi, Mj = Mj)

    # J3 terms
    if sub_i == 0:
        coor_j      = [xi, yi - 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J3),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

        coor_j      = [xi, yi + 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J3),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

        coor_j      = [xi - 2, yi - 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_Jmatrix_XXZ(J = sptk.Vec3(0.0, 0.0, J3),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

hamiltonian.simplify()
print()
hamiltonian.build_mc_list()
print()

# Create a folder *dump* for logging the results

dump_dir = "dump"
if os.path.exists(dump_dir):
    shutil.rmtree(dump_dir)
os.makedirs(dump_dir)

with open(os.path.join(dump_dir, "energy.dat"), "w") as foutE:
    foutE.write(f"{'#(1)':>20}{'(2)':>20}{'(3)':>20}\n")
    foutE.write(f"{'time':>20}{'E':>20}{'mz':>20}\n")
foutE.close()

with open(os.path.join(dump_dir, "Nsites.dat"), "w") as foutN:
    foutN.write(f"{Nsites}\n")
foutN.close()

# Monte Carlo parameters

seed = args.seed                            # random seed
kT   = args.kT                          # final temperature
kT0  = args.kT0                          # initial temperature of annealing

max_sweeps      = args.max_sweeps
sweeps_anneal   = max_sweeps // 4
log_interval    = args.log_interval                # frequency of doing measurements
sweeps_per_dump = args.sweeps_per_dump             # frequency of taking snapshots

alpha_anneal = np.exp(np.log(kT / kT0) / sweeps_anneal)
if alpha_anneal < 0.5 or alpha_anneal >= 1.0:
    raise ValueError("alpha_anneal should be in the range of [0.5, 1.0)!")

print("seed                         ", seed)
print("Total sweeps:                ", max_sweeps)
print("Sweeps used for annealing:   ", sweeps_anneal)
print("alpha (T_{n} = alpha * T_{n-1}): ", alpha_anneal)
print("Intervals of logging energy:   ", log_interval, " sweeps")
print("Intervals of taking snapshots: ", sweeps_per_dump, " sweeps")

# Perform Monte Carlo (in serious MC, should do a few independent MC's to estimate average and error; here we only perform one MC run for the purpose of demonstration)

mc = sptk.mc_Ising(seed_global = seed, seed_local = 0, kT = kT0, Energy_initial = 0.0, dump_dir = dump_dir)

s = sptk.Vec3List(Nsites, sptk.Vec3(0.0, 0.0, 1.0))    # array of spins aligned along Z-axis
mc.set_spins_random(s)                                 # randomize initial spins
mc.update_energy(model = hamiltonian, s = s)           # update the initial energy

while mc.n_sweeps < max_sweeps:
    # logging
    if mc.n_sweeps % log_interval == 0:
        mx, my, mz = sptk.spins_magnetization(s, S = hamiltonian.S)
        with open(os.path.join(mc.dump_dir, "energy.dat"), "a") as foutE:
            foutE.write(f"{mc.n_sweeps:20d}{mc.E():20.7e}{mz:20.7e}\n")
        foutE.close()
    if mc.n_sweeps % sweeps_per_dump == 0:
        mc.dump(lattice = latt, s = s, sweeps_per_dump = sweeps_per_dump)

    # metropolis update
    mc.update_metropolis(model = hamiltonian, s = s)

    # change the temperature according to the annealing schedule
    if mc.n_sweeps < sweeps_anneal:
        mc.change_beta(1.0 / (kT0 * np.power(alpha_anneal, mc.n_sweeps)), log = False)
    elif mc.n_sweeps == sweeps_anneal:
        mc.change_beta(1.0 / kT, log = True)

# ensure kT is logged in dump
mc.change_beta(1.0 / kT, log = True)
