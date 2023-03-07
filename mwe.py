from petsc4py import PETSc
from mpi4py import MPI
import numpy as np
petsc_options = {"ksp_rtol": 1.0e-8,
                 "ksp_type": "cg",
                 "pc_type": "gamg",
                 # "ksp_view": None,
                 # "help": None,
                 "ksp_monitor": None
                 }

viewer_A = PETSc.Viewer().createBinary('matrix-A.dat', 'r')
viewer_b = PETSc.Viewer().createBinary('vector-b.dat', 'r')


A = PETSc.Mat().load(viewer_A)
b = PETSc.Vec().load(viewer_b)

ksp = PETSc.KSP().create(MPI.COMM_WORLD)
ksp.setOperators(A)


opts = PETSc.Options()
if petsc_options is not None:
    for k, v in petsc_options.items():
        opts[k] = v
ksp.setFromOptions()


uh = b.copy()

ksp.setUp()
print(f"Setup complete: {MPI.COMM_WORLD.rank}", flush=True)
MPI.COMM_WORLD.Barrier()

ksp.solve(b, uh)

print(f"Local solution {np.min(uh.array)=} {np.max(uh.array)=}")
