#!/usr/bin/env python
"""This script loads the FPE with 'San Diego' version 6.1 of the Wrapper.  
It also performs basic housekeeping voltage measurements to verify functionality."""

if __name__ == "__main__":
    from tessfpe.dhu.fpe import FPE
    from tessfpe.dhu.unit_tests import check_house_keeping_voltages
    
    fpe1 = FPE(1, debug=False, preload=False)
    print fpe1.version
    
    if check_house_keeping_voltages(fpe1):
        print "Wrapper load complete. Interface voltages OK."
    else: print "Load failure." # Need more info here.
