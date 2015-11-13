#!/usr/bin/env python

if __name__ == '__main__':
    from tessfpe.dhu.fpe import FPE
    from sys import argv
    assert argv[1] in ['6.1.1', '6.0.5772', '6.1t.1']
    FPE(1, debug=True, preload=True, FPE_Wrapper_version=argv[1])
