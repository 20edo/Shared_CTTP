np=4	# Number of processors

mkdir log

surfaceCheck	constant/triSurface/combustor.stl	2>&1 | tee log/surfaceCheck.log
mv problemFaces *.obj constant/triSurface
blockMesh						2>&1 | tee log/blockMesh.log
rotateMesh '(0 0 1)' '(0 1 0)' -noZero  		2>&1 | tee log/rotateMesh.log
surfaceFeatures						2>&1 | tee log/surfaceFeatures.log
decomposePar						2>&1 | tee log/decomposePar.log
mpirun -np $np	snappyHexMesh	-parallel		2>&1 | tee log/snappyHexMesh.log
mpirun -np $np	checkMesh	-parallel		2>&1 | tee log/checkMesh.log

touch	combustor.foam

# paraview combustor.foam &
