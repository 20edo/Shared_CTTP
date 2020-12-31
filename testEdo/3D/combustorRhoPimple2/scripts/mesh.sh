np=4	# Number of processors

mkdir log
touch combustor.foam

surfaceCheck	constant/triSurface/combustor.stl	2>&1 | tee log/surfaceCheck.log
mv problemFaces *.obj constant/triSurface
blockMesh						2>&1 | tee log/blockMesh.log
rotateMesh '(0 0 1)' '(0 1 0)' -noZero				2>&1 | tee log/rotateMesh.log
surfaceFeatures						2>&1 | tee log/surfaceFeatures.log
decomposePar						2>&1 | tee log/decomposePar.log
echo '##################### SNAPPYHEXMESH BEGUN HERE ####################'
mpirun 	-np $np		snappyHexMesh 	-parallel	-overwrite		2>&1 > log/snappyHexMesh.log 
mpirun 	-np $np		checkMesh	-parallel	2>&1 | tee log/checkMesh.log
mpirun	-np $np		renumberMesh	-parallel	-overwrite	2>&1	| tee log/renumberMesh.log	
reconstructParMesh	-mergeTol	1e-10 -constant		2>&1 | tee log/reconstructParMesh.log

touch	combustor.foam

# paraview combustor.foam &
