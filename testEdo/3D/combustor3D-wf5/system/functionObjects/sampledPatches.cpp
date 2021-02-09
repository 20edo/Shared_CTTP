sampled_WallFilmRegionFaces
{
	type 			surfaces;
	enabled 		yes;
	writeControl 		adjustableRunTime;
	writeInterval 		0.002;
	fields 			(p	T);
	interpolationScheme 	cellPoint;
	surfaceFormat		vtk;
	surfaces
		(
		 	sampled_WallFilmRegionFaces
		 	{
		 		type patch;
		 		patches 	("region0_to_wallFilmRegion_wallFilmFaces");
		 		interpolate 	true;
		 	}
		);
}
sampled_Outlet
{
	type 			surfaces;
	enabled 		yes;
	writeControl 		adjustableRunTime;
	writeInterval 		0.002;
	fields 			(p	T);
	interpolationScheme 	cellPoint;
	surfaceFormat		vtk;
	surfaces
		(
		 	walls
		 	{
		 		type patch;
		 		patches 	("outlet");
		 		interpolate 	true;
		 	}
		);
}
