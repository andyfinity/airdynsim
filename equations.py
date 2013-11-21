import numpy as np
from variables import * #C,W,rho,V_0,S_w,I_xx_b,I_yy_b,I_zz_b,I_xy_b,I_xz_b,I_xy_b,I_yz_b,I_xz_b,I_yz_b,theta_0,phi_0
from pint import UnitRegistry
ureg = UnitRegistry()

i_xy = I_xy_b/I_xx_b;
i_xz = I_xz_b/I_xx_b;
i_yx = I_xy_b/I_yy_b;
i_yz = I_yz_b/I_yy_b;
i_zx = I_xz_b/I_zz_b;
i_zy = I_yz_b/I_zz_b;

C['L0'] = (W / (1/2 * rho * V_0 ** 2 * S_w)).magnitude
C['L'] = (W * np.cos(theta_0) / (1/2 * rho * V_0 ** 2 * S_w * np.cos(phi_0))).magnitude
C['D'] = C['D0'] + (C['D,alpha'] * C['L0'] / (2 * C['L,alpha'])) * ((C['L'] / C['L0']) ** 2 - 1)
C['D,alpha'] = C['D,alpha'] * C['L'] / C['L0']
C['X,alpha'] = C['L'] - C['D,alpha']
C['Z,alpha'] = - C['L,alpha'] - C['D']
deltaalpha = (((C['L'] - C['L0']) / C['L,alpha']) * ureg.radian).to(ureg.degree)
phi = -deltaalpha

# print(C['L0'])
# print(C['L'])
# print(C['D'])
# print(C['D,alpha'])
# print(C['X,alpha'])
# print(C['Z,alpha'])
# print(deltaalpha)
# print(phi)

B = {}
# I'm not really sure how to proceed... I can't find any definitions for C['X,muhat'], or even what muhat is