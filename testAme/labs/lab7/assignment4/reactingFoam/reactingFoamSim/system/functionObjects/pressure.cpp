pInlet
{
	type		surfaceFieldValue;
	enabled		yes;
	log		false;

        graphFormat     raw;
	writeControl	timeStep;
	writeInterval	10;

	regionType	patch;
	writeFields	no;
	name		inlet;
	operation	average;
	fields		(p);
	libs		("libfieldFunctionObjects.so");
}

pOutlet
{
	type		surfaceFieldValue;
	enabled		yes;
	log		false;
	
        graphFormat     raw;
	writeControl	timeStep;
	writeInterval	10;

	regionType	patch;
	writeFields	no;
	name		outlet;
	operation	average;
	fields		(p);
	libs		("libfieldFunctionObjects.so");
}

