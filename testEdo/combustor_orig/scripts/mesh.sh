# This contains the commands needed to mesh the combustor

# Define variables
np='4'	# Number of processors

# Lauch routine

mkdir log

blockMesh 2>&1 | tee log/blockMesh.log

rotateMesh '(0 0 1)' '(0 1 0)' -noZero  2>&1 | tee log/rotateMesh.log


surfaceCheck constant/triSurface/combustor_mm.stl 2>&1 | tee log/surfaceCheck.log

surfaceFeatures -dict system/surfaceFeaturesDict 2>& tee log/surfaceFeatures.log

decomposePar 2>&1 | tee log/decomposePar.log


mpirun -np $np snappyHexMesh -parallel 2>&1 | tee log/snappyHexMesh.log

mpirun -np $np checkMesh -parallel 2>&1 | tee log/checkMesh.log

