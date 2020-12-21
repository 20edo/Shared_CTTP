# Reconstruct case
reconstructPar	2>&1	| tee log/reconstructPar.log
reconstructPar 	-region	wallFilmRegion	2>&1	| tee log/reconstructPar_wallFilmRegion.log

# To VTK
foamToVTK	2>&1	| tee log/foamToVTK.log
foamToVTK	-region 	wallFilmRegion | tee log/foamToVTK_wallFilmRegion.log
