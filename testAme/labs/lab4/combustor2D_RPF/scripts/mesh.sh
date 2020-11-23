np=4	# Number of processors

mkdir log

blockMesh						2>&1 | tee log/blockMesh.log
decomposePar						2>&1 | tee log/decomposePar.log
mpirun -np $np	checkMesh	-parallel		2>&1 | tee log/checkMesh.log

touch	combustor.foam

# paraview combustor.foam &
