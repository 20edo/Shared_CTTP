T_averageOutlet
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

T_maxWallFilm
{
        type            surfaceFieldValue;
        enabled         yes;
        log             false;
        executeControl  timeStep;
        executeInterval 1;
        graphFormat     raw;

        executeControl  timeStep;
        executeInterval 1;
        writeControl    timeStep;
        writeInterval   1;

        regionType      patch;
        writeFields     no;
        name            region0_to_wallFilmRegion_wallFilmFaces;
        operation       max;
        fields          (T);
        libs            ("libfieldFunctionObjects.so");
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
                isoT1800
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        1800;
                        interpolate     true;
                }
                isoT2000
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2000;
                        interpolate     true;
                }
                isoT2200
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2200;
                        interpolate     true;
                }
                isoT2400
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2400;
                        interpolate     true;
                }
                isoT2800
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        2800;
                        interpolate     true;
                }
                isoT3000
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        3000;
                        interpolate     true;
                }
                isoT3200
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        3200;
                        interpolate     true;
                }
		isoT3400
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        3400;
                        interpolate     true;
                } 
		isoT3600
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        3600;
                        interpolate     true;
                } 
		isoT3800
                {
                        type            isoSurface;
                        isoField        T;
                        isoValue        3800;
                        interpolate     true;
                }  


 


 



        );
}

