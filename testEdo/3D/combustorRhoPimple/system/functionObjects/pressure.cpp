pInlet
{
	type		surfaceFieldValue;
	enabled		yes;
	log		false;
	
	    
        executeControl  timeStep;
        executeInterval 1;
        graphFormat     raw;

	writeControl	timeStep;
	writeInterval	1;

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
	

        executeControl  timeStep;
        executeInterval 1;
        graphFormat     raw;

	writeControl	timeStep;
	writeInterval	1;

	regionType	patch;
	writeFields	no;
	name		outlet;
	operation	average;
	fields		(p);
	libs		("libfieldFunctionObjects.so");
}

