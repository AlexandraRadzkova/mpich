from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
p = comm.Get_size()

n = 4
m = 3
k = 2
q = 0

matrix = np.array([[x + rank for y in range(n)] for x in range(m)])
row_to_send = [matrix[i][k] for i in range(m)]

received_rows = comm.gather(row_to_send, root=q)

if rank == q:
	print("I am the master process")
	print("received_rows " + str(received_rows))
	final_array = np.concatenate(received_rows)
	print("final_array " + str(final_array))
#mpiexec -n 4 python script.py
