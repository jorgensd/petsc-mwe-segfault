# petsc-mwe-segfault

Code producing a segfault in setup when using petsc>3.16.4

Code runs in serial and with two processes using `mpirun -n 2 python3 mwe.py` with petsc4py==3.16.4
but segfaults with `petsc4py==3.17.0`.

