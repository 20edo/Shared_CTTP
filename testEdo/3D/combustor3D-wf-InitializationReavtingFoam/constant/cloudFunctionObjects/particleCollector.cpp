particleCollector
	{
		type            particleCollector;

		mode            polygon;
		polygons
			(
			 	(
			 (-0.1	-0.29	-1)
			 (0.1	-0.29	-1)
			 (0.1	-0.29	1)
			 (-0.1	-0.29	1)
			 )
			);

		normal          (0 1 0);

		negateParcelsOppositeNormal no;
		removeCollected no;
		surfaceFormat   vtk;
		resetOnWrite    no;
		log             yes;

		executeControl  timeStep;
		executeInterval 1;
		graphFormat     raw;

		writeControl    timeStep;
		writeInterval   1;


	};

