facePostProcessing
	{
		type		facePostProcessing;
		surfaceFormat	vtk;
		resetOnWrite	false;
		log		yes;
		writeFile	yes;
		faceZones	("wallFilmFaces|region0_to_wallFilmRegion_wallFilmFaces");
		writeControl	writeTime;
		writeInterval	1;

	};
