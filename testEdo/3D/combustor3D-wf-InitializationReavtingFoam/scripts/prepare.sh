# Save some variables used later
np=4	# Number of processors
cwd=$(pwd) # Current work directory
pwd
# Compile the solver
cd ../applications/solvers/lagrangian/sprayFilmFoam
wmake	2>&1	| tee $cwd/log/wmake.log
cd $cwd
pwd

# Reconstruct Mesh
reconstructParMesh	-latestTime	2>&1	| tee log/reconstructParMesh.log

# Copy the boundary conditions to the folder containing the mesh
#cp -r 0.bak/* 3e-05
mv 3e-05 0
cp -r 3e-05/polyMesh constant
cp -r 0.bak/*	0
rm -r 3e-05

# Set the coupling bc for the wall film (based on the splitter bcs used before)
#for i in 0/*; do
#    if [ -f $i ]; then
#        sed -i s/wall/region0_to_wallFilmRegion_wallFilmFaces/g $i
#    fi
#done

# Generate thermo files 
chemkinToFoam	chemkin/chem.inp	chemkin/therm.dat	chemkin/transportProperties	constant/reactions	constant/speciesThermo 2>&1	| tee log/chemkinToFoam.log

# Generate foam file
touch combustor.foam

# Decompose Mesh
decomposePar	-force	-latestTime	2>&1	| tee log/decomposePar2.log
# Check the two meshes
mpirun	-np	$np	checkMesh	-parallel	-latestTime	2>&1	| tee log/checkMesh2.log
