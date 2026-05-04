import pint
import numpy as np
from scipy import constants

si = pint.UnitRegistry()

def equilibrium_vapour_pressure(si, T):
    """ Teten's formula (https://en.wikipedia.org/wiki/Tetens_equation) """
    TC = T - constants.zero_Celsius * si.K
    return .61078 * si.kPa * np.exp(17.27 * TC / (237.3 * si.K + TC))

