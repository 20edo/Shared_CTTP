fieldAverage1
{
    // Mandatory entries (unmodifiable)
    type            fieldAverage;
    libs            ("libfieldFunctionObjects.so");

    // Mandatory entries (runtime modifiable)
    fields
    (	
        U
        {
            mean     		true;
            prime2Mean  	true;
            base        	time;
	    windowType  	exact;
	    allowRestart 	true;
        }
        k
        {
            	mean        	true;
            	prime2Mean  	true;
            	base        	time;
            	windowType	exact;
            	allowRestart    true;

       	}
	p
	{
		mean		true;
		prime2Mean	true;
		base		time;
            	windowType      exact;
            	allowRestart    true;

	}

	T
	{
		mean		true;
		prime2Mean	true;
		base		time;
            	windowType      exact;
            	allowRestart    true;

	}


    	);
	
	window			0.05;

    	// Optional entries (runtime modifiable)
    	restartOnRestart    false;
    	restartOnOutput     false;
    	periodicRestart     false;
    	restartPeriod       0.002;

    	// Optional (inherited) entries
    	enabled         true;
    	log             false;
    	timeStart       0;
    	timeEnd         1.0;
    	writeControl    writeTime;
    	writeInterval   1;
 	}


