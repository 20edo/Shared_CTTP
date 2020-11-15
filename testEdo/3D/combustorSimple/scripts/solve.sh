np=4	# Number of processors

mpirun -np $np simpleFoam -parallel 	2>&1	| tee	log/simpleFoam.log
