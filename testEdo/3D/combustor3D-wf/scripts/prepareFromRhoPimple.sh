# Save some variables used later
np=4	# Number of processors
cwd=$(pwd) # Current work directory
pwd
sourceCase=../combustorRhoPimpleMidday

# Compile the solver
cd ../applications/solvers/lagrangian/sprayFilmFoam
wmake	2>&1	| tee $cwd/log/wmake.log
cd $cwd
pwd

# Remove 0 folder if present
rm -r 0

# Create the 0 folder
cp -r 0.bak	0

# Copy the mesh
cp -r 	$sourceCase/constant/polyMesh constant
# Copy the log
cp -r 	$sourceCase/log .

# Change write format to ascii to be able to edit boundary patches
sed     -i      s/binary/ascii/g        system/controlDict

# Generate faceZones and faceSets and extrude to create the wallFilm region
topoSet		2>&1	| tee log/topoSet.log
extrudeToRegionMesh	-overwrite	2>&1	| tee log/extrudeToRegion.log

# Set the coupling bc for the wall film (based on the splitter bcs used before)
for i in 0/*; do
    if [ -f $i ]; then
	    sed -i s/outerWalls/region0_to_wallFilmRegion_wallFilmFaces/g $i
	    sed -i s/splitterLeft/region0_to_wallFilmRegion_wallFilmFaces/g $i
	    sed -i s/splitterRight/region0_to_wallFilmRegion_wallFilmFaces/g $i
	    sed -i s/splitterTop/region0_to_wallFilmRegion_wallFilmFaces/g $i
	    sed -i s/splitterBottom/region0_to_wallFilmRegion_wallFilmFaces/g $i
	    sed -i s/splitterFront/region0_to_wallFilmRegion_wallFilmFaces/g $i
	    sed -i s/splitterRear/region0_to_wallFilmRegion_wallFilmFaces/g $i
    fi
done

# Map fields from rhoPimple simulation
mapFields       $sourceCase     -sourceTime     latestTime      2>&1    | tee   log/mapFields.log

rm 0/Co 0/yPlus
# Change writeFormat to binary to save disk space
sed     -i      s/ascii/binary/g        system/controlDict

# Generate thermo files 
chemkinToFoam	chemkin/chem.inp	chemkin/therm.dat	chemkin/transportProperties	constant/reactions	constant/speciesThermo 2>&1	| tee log/chemkinToFoam.log

# Generate foam file
touch combustor.foam

# Decompose Mesh
decomposePar						2>&1	| tee log/decomposePar2.log

# Decompose wall film region
decomposePar 	-region		wallFilmRegion		2>&1    | tee log/decomposePar_wallFilmRegion.log

# Check the two meshes
mpirun	-np	$np	checkMesh	-parallel	2>&1	| tee log/checkMesh2.log

# Print summary of the Patches
mpirun	-np	$np	patchSummary	-parallel	2>&1	| tee log/patchSummary

mpirun  -np     $np     patchSummary    -parallel	-region 	wallFilmRegion       2>&1    | tee log/patchSummary_WallFilmRegion

