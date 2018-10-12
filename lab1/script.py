from mpi4py import MPI
from random import random

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

i = 0
j = 3

if rank == i:
	data = 42
	comm.send(data, dest=j)
	print("I am {0} send {1}".format(i, data))
elif rank == j:
	data = comm.recv(source=i)
	print("I am {0} receive {1}".format(j, data))

for r in range(size):
	secret = None
	if rank == r:
		secret = rank
		print("I am {0}. My secret: {1}".format(rank, secret))

	secret = comm.bcast(secret, root=r) #send everyone
	
	if rank != r:
		print("I am {0}. I received secret: {1}".format(rank, secret))
#mpiexec -n 4 python script.py