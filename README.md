# petsc-mwe-segfault

Code producing a segfault in setup when using petsc>=3.17.0

Code runs in serial and with multiple processes using `mpirun -n 3 python3 mwe.py` with `petsc4py==3.16.x`
but segfaults with `petsc4py>=3.17.0`.

