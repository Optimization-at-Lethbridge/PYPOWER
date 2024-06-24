# Copyright (c) 1996-2015 PSERC. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Runs an optimal power flow.
"""

from os.path import dirname, join
from sys import stdout, stderr

from pypower.case3 import case3
from pypower.case5 import case5
from pypower.case6ww import case6ww
from pypower.case9 import case9
from pypower.case14 import case14
from pypower.case24_ieee_rts import case24_ieee_rts
from pypower.case30 import case30
from pypower.case39 import case39
from pypower.case57 import case57
from pypower.case118 import case118
from pypower.case300 import case300

from pypower.opf import opf
from pypower.ppoption import ppoption
from pypower.printpf import printpf
from pypower.savecase import savecase


def runopf(casedata=None, ppopt=None, fname='', solvedcase=''):
    """Runs an optimal power flow.

    @see: L{rundcopf}, L{runuopf}

    @author: Ray Zimmerman (PSERC Cornell)
    """
    ## default arguments
    if casedata is None:
        casedata = join(dirname(__file__), 'case9')
    ppopt = ppoption(ppopt)

    ##-----  run the optimal power flow  -----
    r = opf(casedata, ppopt)

    ##-----  output results  -----
    if fname:
        fd = None
        try:
            fd = open(fname, "a")
        except IOError as detail:
            stderr.write("Error opening %s: %s.\n" % (fname, detail))
        finally:
            if fd is not None:
                printpf(r, fd, ppopt)
                fd.close()

    else:
        printpf(r, stdout, ppopt)

    ## save solved case
    if solvedcase:
        savecase(solvedcase, r)

    return r


if __name__ == '__main__':

    ppopt = ppoption(OPF_ALG=560, VERBOSE=2, PF_DC=True)

    print('Case 3,  OPF, DC...................')
    ppc = case3()
    runopf(ppc, ppopt)

    #print('Case 4gs,  OPF, DC...................')
    #ppc = case4gs()
    #runopf(ppc, ppopt)

    print('Case 5,  OPF, DC...................')
    ppc = case5()
    runopf(ppc, ppopt)

    print('Case 6ww, OPF, DC...................')
    ppc = case6ww()
    runopf(ppc, ppopt)

    print('Case 9,  OPF, DC...................')
    ppc = case9()
    runopf(ppc, ppopt)

    print('Case 14,  OPF, DC...................')
    ppc = case14()
    runopf(ppc, ppopt)

    print('Case 24 IEEE RTS,  OPF, DC...................')
    ppc = case24_ieee_rts()
    runopf(ppc, ppopt)

    print('Case 30,  OPF, DC...................')
    ppc = case30()
    runopf(ppc, ppopt)


    #print('Case 39...................')
    #ppc = case39()
    #runopf(ppc, ppopt)

    #print('Case 57...................')
    #ppc = case57()
    #runopf(ppc, ppopt)

    #print('Case 118...................')
    #ppc = case118()
    #runopf(ppc, ppopt)

    #print('Case 300...................')
    #ppc = case300()
    #runopf(ppc, ppopt)


