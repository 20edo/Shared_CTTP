yPlanes
{
	type surfaces;
	enabled 	yes;
	writeControl 	adjustableRunTime;
	writeInterval 	0.002;

	fields 		(p 	U	T	C7H16	O2	N2	H2O	CO2);
	interpolationScheme cellPoint;
	surfaceFormat vtk;

	surfaces
		(
                 y_50
                 {   
                        type            cuttingPlane;
                        planeType       pointAndNormal;
                        pointAndNormalDict
                        {   
                                point   (0      -0.05     1e-4);
                                normal  (0      1       0);
                        }   
                        interpolate     true;
                 }

		 y100
		 {
		 	type 		cuttingPlane;
		 	planeType 	pointAndNormal;
		 	pointAndNormalDict
		 	{
		 		point 	(0 	0.1 	1e-4);
		 		normal 	(0 	1 	0);
		 	}
		 	interpolate	true;
		 }
		 outletPlane
		 {
		 	type 		cuttingPlane;
		 	planeType 	pointAndNormal;
		 	pointAndNormalDict
		 	{
		 		point 	(0 	0.1 	1e-4);
		 		normal 	(0 	1 	0);
		 	}
		 	interpolate true;
		 }
		);
}
