TouterWalls
{
	type		surfaceFieldValue;
	enabled		yes;
	log		false;
	executeControl	timeStep;
	executeInterval	1;
	graphFormat	raw;
	
	executeControl	timeStep;
	executeInterval	1;
	writeControl	timeStep;
	writeInterval	1;

	regionType	patch;
	writeFields	no;
	name		region0_to_wallFilmRegion_wallFilmFaces;
	operation	max;
	fields		(T);
	libs		("libfieldFunctionObjects.so");
}
