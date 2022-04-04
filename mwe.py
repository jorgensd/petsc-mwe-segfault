from petsc4py import PETSc
from mpi4py import MPI

petsc_options = {"ksp_rtol": 1.0e-8,
                 "ksp_type": "cg",
                 "pc_type": "gamg",
                 "pc_gamg_type": "agg",
                 "pc_gamg_coarse_eq_limit": 1000,
                 "pc_gamg_sym_graph": True,
                 "pc_gamg_square_graph": 2,
                 "pc_gamg_threshold": 0.02,
                 "mg_levels_ksp_type": "chebyshev",
                 "mg_levels_pc_type": "jacobi",
                 "mg_levels_esteig_ksp_type": "cg",
                 "ksp_view": None,
                 "help": None,
                 "ksp_monitor": None
                 }

viewer_A = PETSc.Viewer().createBinary('matrix-A.dat', 'r')
viewer_b = PETSc.Viewer().createBinary('vector-b.dat', 'r')


A = PETSc.Mat().load(viewer_A)
b = PETSc.Vec().load(viewer_b)

ksp = PETSc.KSP().create(MPI.COMM_WORLD)
ksp.setOperators(A)


solver_prefix = "test_solver"
ksp.setOptionsPrefix(solver_prefix)

opts = PETSc.Options()
opts.prefixPush(solver_prefix)
if petsc_options is not None:
    for k, v in petsc_options.items():
        opts[k] = v
opts.prefixPop()
ksp.setFromOptions()


uh = b.copy()

ksp.setUp()
print(f"Setup complete: {MPI.COMM_WORLD.rank}", flush=True)
MPI.COMM_WORLD.Barrier()

ksp.solve(b, uh)

print(f"Local solution {uh.array}")
