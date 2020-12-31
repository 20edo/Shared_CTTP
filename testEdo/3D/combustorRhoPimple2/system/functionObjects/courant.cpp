Co1
{
    // Mandatory entries (unmodifiable)
    type            CourantNo;
    libs            ("libfieldFunctionObjects.so");
    enabled		true;
    log             false;
    timeStart       0;
    timeEnd         1000;
    executeControl  writeTime;
    executeInterval 1;
    writeControl	writeTime;
    writeInterval	1;
}

