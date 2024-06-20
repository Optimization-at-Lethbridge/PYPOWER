from numpy import array

def case3():
    """Power flow data for 3 bus, 2 gen case.
    Please see L{caseformat} for details on the case file format.

    @return: Power flow data for 3 bus, 2 gen case.
    """
    ppc = {"version": '2'}

    ##-----  Power Flow Data  -----##
    ## system MVA base
    ppc["baseMVA"] = 100.0

    ## bus data
    # bus_i type Pd Qd Gs Bs area Vm Va baseKV zone Vmax Vmin
    ppc["bus"] = array([
        [1, 3, 90, 40, 0, 0, 1, 1.02, 0, 250, 1, 1.05, 0.95],
        [2, 2, 0, 0, 0, 0, 1, 1.03, 0, 250, 1, 1.05, 0.95],
        [3, 1, 110, 40, 0, 0, 1, 1, 0, 250, 1, 1.05, 0.95]
    ])

    ## generator data
    # bus, Pg, Qg, Qmax, Qmin, Vg, mBase, status, Pmax, Pmin, Pc1, Pc2,
    # Qc1min, Qc1max, Qc2min, Qc2max, ramp_agc, ramp_10, ramp_30, ramp_q, apf
    ppc["gen"] = array([
        [1, 50, 0, 100, -100, 1.02, 100, 1, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [2, 140, 0, 100, -100, 1.03, 100, 1, 200, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ])

    ## branch data
    # fbus, tbus, r, x, b, rateA, rateB, rateC, ratio, angle, status, angmin, angmax
    ppc["branch"] = array([
        [1, 2, 0.025, 0.1, 0, 100, 100, 100, 0, 0, 1, -360, 360],
        [1, 3, 0.025, 0.1, 0, 100, 100, 100, 0, 0, 1, -360, 360],
        [2, 3, 0.025, 0.1, 0, 100, 100, 100, 0, 0, 1, -360, 360]
    ])

    ##-----  OPF Data  -----##
    ## generator cost data
    # 1 startup shutdown n x1 y1 ... xn yn
    # 2 startup shutdown n c(n-1) ... c0
    ppc["gencost"] = array([
        [2, 0, 0, 3, 0.02, 2, 0],
        [2, 0, 0, 3, 0.0175, 1.75, 0]
    ])

    return ppc
