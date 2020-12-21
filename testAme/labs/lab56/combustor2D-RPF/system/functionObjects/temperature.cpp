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
	name		sides;
	operation	max;
	fields		(T);
	libs		("libfieldFunctionObjects.so");
}

