wallHeatFlux1
{
    // Mandatory entries (unmodifiable)
    type            wallHeatFlux;
    libs            ("libfieldFunctionObjects.so");

    // Optional entries (runtime modifiable)
    patches     (sides); // default is all  // (wall1 "(wall2|wall3)");

    // Optional (inherited) entries
    writePrecision  8;
    writeToFile     false;
    useUserTime     true;
    region          region0;
    enabled         true;
    log             false;
    timeStart       0;
    timeEnd         1000;
    executeControl  timeStep;
    executeInterval 1;
    writeControl    writeTime;
    writeInterval   1;
    graphFormat     raw;
}

SpaceAverageHeatFlux
{
        type            surfaceFieldValue;
        enabled         yes;
        log             false;
    
    
        executeControl  timeStep;
        executeInterval 1;
        graphFormat     raw;

        writeControl    timeStep;
        writeInterval   1;  

        regionType      patch;
        writeFields     no; 
        name            sides;
        operation       average;
        fields          (wallHeatFlux);
        libs            ("libfieldFunctionObjects.so");
}
