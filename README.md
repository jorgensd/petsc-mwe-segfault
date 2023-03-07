# petsc-mwe-segfault

Code producing a segfault in setup when using petsc>3.17.5

Code runs in serial and with two processes using `mpirun -n 3 python3 mwe.py` with `petsc4py==3.17.5`
but segfaults with `petsc4py==3.18.5`.

