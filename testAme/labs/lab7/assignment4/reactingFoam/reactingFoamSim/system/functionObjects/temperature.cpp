TOutlet
{
	type		surfaceFieldValue;
	enabled		yes;
	log		false;
		
	executeControl	timeStep;
	executeInterval	1;
	graphFormat	raw;		
	writeControl	timeStep;
	writeInterval	1;

	regionType	patch;
	writeFields	no;
	name		outlet;
	operation	average;
	fields		(T);
	libs		("libfieldFunctionObjects.so");
}

isoT
{
	type 			surfaces;
	enabled 		yes;
	log			false;
	
	writeControl 		timeStep;
	writeInterval 		1;
	
	fields 			(T);
	interpolationScheme 	cellPoint;
	surfaceFormat 		vtk;
	surfaces
	(
		isoT
		{
			type 		isoSurface;
			isoField 	T;
			isoValue 	900;
			interpolate	true;
		}
	);
}
