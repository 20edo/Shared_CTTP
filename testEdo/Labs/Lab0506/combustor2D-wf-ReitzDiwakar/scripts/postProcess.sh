# Reconstruct case
reconstructPar	2>&1	| tee log/reconstructPar.log
reconstructPar 	-region	wallFilmRegion	2>&1	| tee log/reconstructPar_wallFilmRegion.log

# To VTK
foamToVTK	2>&1	| tee log/foamToVTK.log
foamToVTK	-region 	wallFilmRegion | tee log/foamToVTK_wallFilmRegion.log

# Prepare folders
mkdir paraviewPostProcessing
mkdir paraviewPostProcessing/Data
mkdir paraviewPostProcessing/Images

# paraview postProcessing
#pvpython	scripts/paraviewPostProcessing.py 

# Create penetration folder in postProcessing
mkdir postProcessing/penetration
cd log
grep -w 	Time 		sprayFoam.log > ../postProcessing/penetration/Time
grep -ri 	penetration	sprayFoam.log > ../postProcessing/penetration/penetration
