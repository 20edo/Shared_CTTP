np=4	# Number of processors

cp -r 0 process*
mpirun -np $np pimpleFoam -parallel 	2>&1	| tee	log/simpleFoam.log
recontructPar				2>&1	| tee	log/recontructPar.log
