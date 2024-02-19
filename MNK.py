import numpy as np
import sympy as sp

params = [4,4,4, np.radians(90),np.radians(90),np.radians(90)]

a, b, c, alpha, betta, gamma, h, k, l = sp.symbols('a b c alpha betta gamma h k l')
_a = 4
_b = 4
_c = 4
_alpha = np.radians(90)
_betta = np.radians(90)
_gamma = np.radians(90)
# Определение функции---------------------------------------------------------------------------
def calc_theory_d(hkl):
    ksi = 1 - np.cos(_alpha) ** 2 - np.cos(_betta) ** 2 - np.cos(_gamma) ** 2 \
        + 2*np.cos(_alpha)*np.cos(_betta)*np.cos(_gamma)
    denom = (hkl[0] / _a / np.sin(_alpha))**2 + (hkl[1] / _b / np.sin(_betta))**2 + (hkl[2] / _c / np.sin(_gamma))**2 \
    + (2 * hkl[0] * hkl[1] / (_a * _b)) * (np.cos(_alpha) * np.cos(_betta) - np.cos(_gamma)) + \
    + (2 * hkl[2] * hkl[0] / (_c * _a)) * (np.cos(_gamma) * np.cos(_alpha) - np.cos(_betta)) + \
    + (2 * hkl[1] * hkl[2] / (_b * _c)) * (np.cos(_betta) * np.cos(_gamma) - np.cos(_alpha))

    return ksi / np.sqrt(denom)
#символьное определение функции------------------------------------------------------------------
ksi = 1 - sp.cos(alpha)**2 - sp.cos(betta)**2 - sp.cos(gamma)**2 \
      + 2 * sp.cos(alpha) * sp.cos(betta) * sp.cos(gamma)

denom = (h / a / sp.sin(alpha))**2 + (k / b / sp.sin(betta))**2 + (l / c / sp.sin(gamma))**2 \
        + (2 * h * k / (a * b)) * (sp.cos(alpha) * sp.cos(betta) - sp.cos(gamma)) + \
        (2 * l * h / (c * a)) * (sp.cos(gamma) * sp.cos(alpha) - sp.cos(betta)) + \
        (2 * k * l / (b * c)) * (sp.cos(betta) * sp.cos(gamma) - sp.cos(alpha))

theory_d = ksi / sp.sqrt(denom)
#------------------------------------------------------------------------------------------------


#DERIVATIVES IN LIST
d_dp = list(map(lambda x : sp.diff(theory_d, x), params))

hkl_list = [(1, 1, 1), (2,0,0), (2,2,2), (4,0,0)]
d_exp = [2.3330, 2.0207, 1.1665, 1.0103]
d_th = []
for i in hkl_list:
    d_th.append(theory_d.subs)