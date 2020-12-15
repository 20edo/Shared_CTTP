np=2

mkdir log
touch combustor.foam
blockMesh	2>&1	| tee log/blockMesh.log
checkMesh	2>&1	| tee log/checkMesh.log
decomposePar	2>&1	| tee log/decomposePar.log
mpirun -np $np rhoPimpleFoam -parallel	| tee log/rhoPimpleFoam.log
reconstructPar	2>&1	| tee log/reconstructPar.log
