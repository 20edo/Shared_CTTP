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
        type                    surfaces;
        enabled                 yes;
        log                     false;

        writeControl            adjustableRunTime;
        writeInterval           0.002;

        fields                  (T);
        interpolationScheme     cellPoint;
        surfaceFormat           vtk;
        surfaces
        (
                isoT600
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        600;
                        interpolate     true;
                }
                isoT700
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        700;
                        interpolate     true;
                }
                isoT800
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        800;
                        interpolate     true;
                }
                isoT900
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        900;
                        interpolate     true;
                }
                isoT1000
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1000;
                        interpolate     true;
                }
                isoT1100
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1100;
                        interpolate     true;
                }
                isoT1200
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1200;
                        interpolate     true;
                }
                isoT1300
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1300;
                        interpolate     true;
                }
                isoT1400
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1400;
                        interpolate     true;
                }
        );
}

