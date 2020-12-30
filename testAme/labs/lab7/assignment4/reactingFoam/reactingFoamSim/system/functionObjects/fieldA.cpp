add
{
        type                    add;
        libs                    ("libfieldFunctionObjects.so");
        enabled                 yes;
        log                     false;

        fields                  (O2 N2);
        result                  A;
        
/*	writeControl		timeStep;
	writeInterval		1;*/
	writeControl            adjustableRunTime;
        writeInterval           0.005;
}



/*
isoAoverF
{
        type                    surfaces;
        enabled                 yes;
        log                     false;

        writeControl            adjustableRunTime;
        writeInterval           0.005;

        fields                  (CH4 A);
        interpolationScheme     cellPoint;
        surfaceFormat           vtk;
        surfaces
        (
                 isoAoverF
                 {
                         type            isoSurface;
                         isoField        A/CH4;
                         isoValue        8.58;
                         interpolate     true;
                 }
        );
}*/

