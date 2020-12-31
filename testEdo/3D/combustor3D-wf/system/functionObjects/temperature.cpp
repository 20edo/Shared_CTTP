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
		isoT1500
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1500;
                        interpolate     true;
                }
                isoT1600
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1600;
                        interpolate     true;
                }
                isoT1700
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1700;
                        interpolate     true;
                }
                isoT1800
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1800;
                        interpolate     true;
                }
                isoT1900
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1900;
                        interpolate     true;
                }
                isoT2000
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2000;
                        interpolate     true;
                }
                isoT2100
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2100;
                        interpolate     true;
                }
                isoT2200
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2200;
                        interpolate     true;
                }
                isoT2300
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2300;
                        interpolate     true;
                }
                isoT2400
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2400;
                        interpolate     true;
                }
                isoT2500
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2500;
                        interpolate     true;
                }

        );
}

