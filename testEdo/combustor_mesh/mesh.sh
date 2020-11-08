# This contains the commands needed to mesh the combustor

# Define variables
np='4'	# Number of processors

# Lauch routine

mkdir log

blockMesh >log/bockMesh.log 2>&1 | cat log/blockMesh.log

surfaceCheck constant/triSurface/combustor_mm.stl > log/surfaceCheck.log 2>&1 | cat log/surfaceCheck.log

surfaceFeatures -dict system/surfaceFeaturesDict > log/surface_Features 2>&1 | cat log/surfaceFeatures.log

decomposePar

mpirun -np $np snappyHexMesh -parallel > log/snappyHexMesh.log 2>&1 | cat log/snappyHexMesh.log

checkMesh > log/checkMesh.log 2>&1 | cat log/checkMesh.log

