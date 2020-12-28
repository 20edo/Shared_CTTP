surfaces
{
	type            surfaces;
	functionObjectLibs ("libsampling.so");
	writeControl   outputTime;

	surfaceFormat   vtk;
	fields          (T A/F);

	interpolationScheme cellPoint;
	surfaces
	(
		isoAF
		{
			type            isoSurface;
			isoField        A/F;
			isoValue        8.58;
			interpolate     true;
		}
	);
}

