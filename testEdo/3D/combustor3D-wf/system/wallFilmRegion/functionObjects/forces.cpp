force
{
	type		forces;
	enabled		yes;
	libs		("libforces.so");
	log		no;
	patches		"(splitterFront|splitterRear|splitterTop|splitterBottom|splitterLeft|splitterRight)";
	writeControl	timeStep;
	writeInterval	1;

	liftDir		(1 0 0);
	dragDir		(0 1 0);
	CofR		(0 0 0);
}
