# This scripts makes all the required pre-processing to run the case

mkdir log

# Save the path of the current directory
cwd=$(pwd)

pwd

# Compile the solver
cd ../applications/solvers/lagrangian/sprayFilmFoam
wmake	2>&1	| tee $cwd/log/wmake.log
cd $cwd
pwd
# Initialize opportunely all the fields
rm -r 0
cp -r 0.bak 0

# Generate mesh
blockMesh	2>&1	| tee log/blockMesh.log
# Map fields from previous case
mapFields	../combustor2D-RPF -case . -sourceTime latestTime 2>&1	| tee log/mapFields.log

# Set the coupling bc for the wall film (based on the splitter bcs used before)
for i in 0/*; do
    if [ -f $i ]; then
        sed -i s/sides/region0_to_wallFilmRegion_wallFilmFaces/g $i
    fi
done

# Generate faceZones and faceSets and extrude to create the wallFilm region
topoSet		2>&1	| tee log/topoSet.log
extrudeToRegionMesh	-overwrite	2>&1	| tee log/extrudeToRegion.log

# Generate thermo files 
chemkinToFoam	chemkin/chem.inp	chemkin/therm.dat	chemkin/transportProperties	constant/reactions	constant/spieciesThermo 2>&1	| tee log/chemkinToFoam.log

# Generate foam file
touch combustor.foam

# Decompose Mesh
decomposePar	2>&1	| tee log/decomposePar.log
# cp system/decomposeParDict system/wallFilmRegion/decomposeParDict
decomposePar -region wallFilmRegion	| tee log/decomposePar_wallFilmRegion.log
# Check the two meshes
checkMesh	2>&1	| tee log/checkMesh.log
