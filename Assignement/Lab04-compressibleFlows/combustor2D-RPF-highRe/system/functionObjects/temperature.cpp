TInlet
{
	type		surfaceFieldValue;
	enabled		yes;
	log		true;
			
	writeControl	writeTime;
	writeInterval	1;

	regionType	patch;
	writeFields	no;
	name		inlet;
	operation	average;
	fields		(T);
	libs		("libfieldFunctionObjects.so");
}

TOutlet
{
	type		surfaceFieldValue;
	enabled		yes;
	log		true;
			
	writeControl	writeTime;
	writeInterval	1;

	regionType	patch;
	writeFields	no;
	name		outlet;
	operation	average;
	fields		(T);
	libs		("libfieldFunctionObjects.so");
}

