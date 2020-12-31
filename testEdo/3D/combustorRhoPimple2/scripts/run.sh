np=4

mkdir log
touch combustor.foam
decomposePar	-force -latestTime 2>&1	| tee log/decomposePar2.log
mpirun	-np	$np	patchSummary 	-parallel	2>&1	| tee log/patchSummary
mpirun -np $np rhoPimpleFoam -parallel	> log/rhoPimpleFoam.log
reconstructPar	2>&1	| tee log/reconstructPar.log
