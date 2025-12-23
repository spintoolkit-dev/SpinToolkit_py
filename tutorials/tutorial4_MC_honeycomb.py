# Tutorial-4: Monte Carlo simulation of Ising model on honeycomb lattice

import numpy as np
import os
import shutil
import argparse
import spintoolkit_py as sptk

sptk.print_system_info()


# Add arguments
parser = argparse.ArgumentParser(description="Monte Carlo simulation of the Ising model on a honeycomb lattice.")

parser.add_argument('--l',               type = int,   default = 30,     help = 'Linear dimension of honeycomb lattice')
parser.add_argument('--J1',              type = float, default = -1.0,   help = 'J1 interaction')
parser.add_argument('--J2',              type = float, default = 1.5,    help = 'J2 interaction')
parser.add_argument('--J3',              type = float, default = 0.5,    help = 'J3 interaction')
parser.add_argument('--seed',            type = int,   default = 0,      help = 'Random seed for the simulation.')
parser.add_argument('--T',               type = float, default = 0.4,    help = 'Final temperature (in units of J).')
parser.add_argument('--T0',              type = float, default = 1.0,    help = 'Initial temperature for annealing.')
parser.add_argument('--max_sweeps',      type = int,   default = 200000, help = 'Total number of Monte Carlo sweeps.')
parser.add_argument('--log_interval',    type = int,   default = 50,     help = 'Frequency of measurements.')
parser.add_argument('--sweeps_per_dump', type = int,   default = 10000,  help = 'Frequency of taking snapshots.')

args = parser.parse_args()

# Print all arguments
print("Command line arguments:")
for arg, value in vars(args).items():
    print(f"{arg:18}: {value}")
print()


# Define a honeycomb lattice to be used
l = args.l
latt = sptk.lattice(name = "honeycomb", l = [l, l])


# Define the model and include magnetic couplings
J1 = args.J1
J2 = args.J2
J3 = args.J3

hamiltonian = sptk.model_spin(S = 0.5, mode = "dipole", lattice = latt)
print()

L = latt.total_sites()
for site_i in range(L):
    coor_i, sub_i = latt.site2coor(site = site_i)
    coor0_i, Mi   = latt.coor2supercell0(coor = coor_i)
    xi = coor_i[0]
    yi = coor_i[1]

    # J1 terms
    if sub_i == 0:
        coor_j      = [xi, yi]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J1),
                                  site_i = site_i, site_j = site_j,
                                  Mi = Mi, Mj = Mj)

        coor_j      = [xi - 1, yi]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J1),
                                  site_i = site_i, site_j = site_j,
                                  Mi = Mi, Mj = Mj)

        coor_j      = [xi - 1, yi - 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J1),
                                  site_i = site_i, site_j = site_j,
                                  Mi = Mi, Mj = Mj)

    # J2 terms
    coor_j      = [xi + 1, yi]
    coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
    site_j      = latt.coor2site(coor = coor_j, sub = sub_i)
    hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J2),
                              site_i = site_i, site_j = site_j,
                              Mi = Mi, Mj = Mj)

    coor_j      = [xi + 1, yi + 1]
    coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
    site_j      = latt.coor2site(coor = coor_j, sub = sub_i)
    hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J2),
                              site_i = site_i, site_j = site_j,
                              Mi = Mi, Mj = Mj)

    coor_j      = [xi, yi + 1]
    coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
    site_j      = latt.coor2site(coor = coor_j, sub = sub_i)
    hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J2),
                              site_i = site_i, site_j = site_j,
                              Mi = Mi, Mj = Mj)

    # J3 terms
    if sub_i == 0:
        coor_j      = [xi, yi - 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J3),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

        coor_j      = [xi, yi + 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J3),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

        coor_j      = [xi - 2, yi - 1]
        coor0_j, Mj = latt.coor2supercell0(coor = coor_j)
        site_j      = latt.coor2site(coor = coor_j, sub = 1)
        hamiltonian.add_2spin_XYZ(J = sptk.Vec3(0.0, 0.0, J3),
                                          site_i = site_i, site_j = site_j,
                                          Mi = Mi, Mj = Mj)

hamiltonian.simplify().build_mc_list()
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

with open(os.path.join(dump_dir, "total_sites.dat"), "w") as foutL:
    foutL.write(f"{L}\n")
foutL.close()


# Monte Carlo parameters
seed = args.seed                        # random seed
T    = args.T                           # final temperature
T0   = args.T0                          # initial temperature of annealing

max_sweeps      = args.max_sweeps
sweeps_anneal   = max_sweeps // 4
log_interval    = args.log_interval     # frequency of doing measurements
sweeps_per_dump = args.sweeps_per_dump  # frequency of taking snapshots

alpha_anneal = np.exp(np.log(T / T0) / sweeps_anneal)
if alpha_anneal < 0.5 or alpha_anneal >= 1.0:
    raise ValueError("alpha_anneal should be in the range of [0.5, 1.0)!")

print("seed                             ", seed)
print("Total sweeps:                    ", max_sweeps)
print("Sweeps used for annealing:       ", sweeps_anneal)
print("alpha (T_{n} = alpha * T_{n-1}): ", alpha_anneal)
print("Intervals of logging energy:     ", log_interval, " sweeps")
print("Intervals of taking snapshots:   ", sweeps_per_dump, " sweeps")


# Perform Monte Carlo
# In serious MC, should do a few independent MC's to estimate average and error;
# here we only perform one MC run for the purpose of demonstration.
mc = sptk.mc_Ising(seed_global = seed, seed_local = 0, Ti = T0, dump_dir = dump_dir)

s = sptk.Vec3List(L, sptk.Vec3(0.0, 0.0, 1.0))         # array of spins aligned along Z-axis
mc.set_random(model = hamiltonian, s = s)              # randomize initial spins

n_sweeps = 0
while n_sweeps < max_sweeps:
    # logging
    if n_sweeps % log_interval == 0:
        mx, my, mz = sptk.spins_magnetization(s = s, S = hamiltonian.S)
        with open(os.path.join(mc.dump_dir, "energy.dat"), "a") as foutE:
            foutE.write(f"{n_sweeps:20d}{mc.Energy():20.7e}{mz:20.7e}\n")
        foutE.close()
    if n_sweeps % sweeps_per_dump == 0:
        mc.save_state_dipole(lattice = latt, s = s, n_sweeps = n_sweeps, sweeps_per_dump = sweeps_per_dump)

    # metropolis update
    mc.update_metropolis(model = hamiltonian, s = s)
    if n_sweeps % sweeps_per_dump == 0:
        print(f"{'n_sweeps: '}{n_sweeps:15d}{', T: '}{1.0 / mc.beta:20.7e}{', acceptance ratio: '}{mc.ratio_accept:20.7f}\n")
    n_sweeps += 1

    # change the temperature according to the annealing schedule
    if n_sweeps < sweeps_anneal:
        mc.change_beta(1.0 / (T0 * np.power(alpha_anneal, n_sweeps)), log = False)
    elif n_sweeps == sweeps_anneal:
        mc.change_beta(1.0 / T, log = False)

# ensure temperature is logged in dump
mc.change_beta(1.0 / T, log = True)
