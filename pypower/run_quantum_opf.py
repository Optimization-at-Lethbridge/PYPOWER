# Copyright (c) 1996-2015 PSERC. All rights reserved.
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.

"""Runs an optimal power flow.
"""

from os.path import dirname, join
from sys import stdout, stderr

from pypower.case118 import case118
from pypower.case14 import case14
from pypower.case24_ieee_rts import case24_ieee_rts
from pypower.case30 import case30
from pypower.case300 import case300
from pypower.case39 import case39
from pypower.case57 import case57
from pypower.case9 import case9
from pypower.case3 import case3
from pypower.case5 import case5
from pypower.case6ww import case6ww

from pypower.opf import opf
from pypower.ppoption import ppoption
from pypower.printpf import printpf
from pypower.savecase import savecase


def run_quantum_opf(casedata=None, ppopt=None, fname='', solvedcase=''):
    """Runs an optimal power flow.

    @see: L{rundcopf}, L{runuopf}

    @author: Ray Zimmerman (PSERC Cornell)
    @author: Md Mohsin Uddin (University of Lethbridge, AB)
    """
    ## default arguments
    if casedata is None:
        casedata = join(dirname(__file__), 'case9')
    ppopt = ppoption(ppopt)
    is_quantum = ppopt["IS_QUANTUM"]  ## Is classical or quantum approaches to solve linear systems
    quantum_alg = ppopt["QUANTUM_ALG"]  ## Quantum Algorithm; 1 for HHL; 2 for VQLS
    if is_quantum:
        stdout.write('Solving systems of linear equations by quantum method\n')
        if quantum_alg == 1:
            stdout.write('Applying HHL quantum algorithm.\n')
        else:
            stdout.write('Applying VQLS hybrid quantum-classical algorithm.\n')
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
    ppopt = ppoption(PF_ALG=1, PF_DC=False, VERBOSE=2, IS_QUANTUM=False)

    # QUANTUM_ALG = 1 for HHL and QUANTUM_ALG = 2 for VQLS
    #ppopt = ppoption(PF_ALG=1, PF_DC=False, VERBOSE=2, IS_QUANTUM=True, QUANTUM_ALG=2)

    ppc = case3()
    run_quantum_opf(ppc, ppopt)

    ppc = case5()
    #run_quantum_opf(ppc, ppopt)

    ppc = case6ww()
    #run_quantum_opf(ppc, ppopt)

    ppc = case9()
    #run_quantum_opf(ppc, ppopt)

    ppc = case14()
    #run_quantum_opf(ppc, ppopt)

    #ppc = case24_ieee_rts()
    #run_quantum_opf(ppc, ppopt)

    #ppc = case30()
    #run_quantum_opf(ppc, ppopt)

    ppc = case39()
    #run_quantum_opf(ppc)

    ppc = case57()
    #run_quantum_opf(ppc)

    ppc = case118()
    #run_quantum_opf(ppc)

    ppc = case300()
    #run_quantum_opf(ppc)