np=4	# Number of processors
reconstructParMesh			2>&1	| tee 	log/reconstructParMesh.log
cp 0.*/* 3
decomposePar	-force	-latestTime	2>&1	| tee	log/decomposePar2.log
mpirun -np $np simpleFoam -parallel 	2>&1	| tee	log/simpleFoam.log
recontructPar				2>&1	| tee	log/recontructPar.log
