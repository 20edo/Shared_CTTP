# Reconstruct case
reconstructPar	2>&1	| tee log/reconstructPar.log
reconstructPar 	-region	wallFilmRegion	2>&1	| tee log/reconstructPar_wallFilmRegion.log

# To VTK
foamToVTK
