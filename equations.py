from std_includes import *
from variables import *
import numpy as np

i["xy"] = I["xy_b"]/I["xx_b"]
i["xz"] = I["xz_b"]/I["xx_b"]
i["yx"] = I["xy_b"]/I["yy_b"]
i["yz"] = I["yz_b"]/I["yy_b"]
i["zx"] = I["xz_b"]/I["zz_b"]
i["zy"] = I["yz_b"]/I["zz_b"]

C['L0'] = (W / (1/2 * rho * V_0 ** 2 * S_w)).magnitude
C['L'] = (W * np.cos(theta_0) / (1/2 * rho * V_0 ** 2 * S_w * np.cos(phi_0))).magnitude
C['D'] = C['D0'] + (C['D,alpha'] * C['L0'] / (2 * C['L,alpha'])) * ((C['L'] / C['L0']) ** 2 - 1)
C['D,alpha'] = C['D,alpha'] * C['L'] / C['L0']
C['X,alpha'] = C['L'] - C['D,alpha']
C['Z,alpha'] = - C['L,alpha'] - C['D']
deltaalpha = (((C['L'] - C['L0']) / C['L,alpha']) * ur.radian).to(ur.degree)
phi = -deltaalpha

B['x,muprime'] = (rho * S_w * cbar_w * C['X,muhat'] / (4 * W / g)).magnitude
B['z,muprime'] = (rho * S_w * cbar_w * C['Z,muhat'] / (4 * W / g)).magnitude
B['m,muprime'] = (rho * S_w * cbar_w ** 2 * l_ref * C['m,muhat'] / (4 * I['yy_b'])).magnitude
B['x,alphaprime'] = (rho * S_w * cbar_w * C['X,alphahat'] / (4 * W / g)).magnitude
B['z,alphaprime'] = (rho * S_w * cbar_w * C['Z,alphahat'] / (4 * W / g)).magnitude
B['m,alphaprime'] = (rho * S_w * cbar_w ** 2 * l_ref * C['m,alphahat'] / (4 * I['yy_b'])).magnitude

A['g'] = g * l_ref / V_0 ** 2
# A['x,mu'] = (rho * S_w * l_ref / (2 * W / g) * (2 * C['X'] + C['X,mu'] + T[',V'] * np.cos(alpha_T0) / (0.5 * rho * V_0 * S_w))) # missing variables

A['x,alpha'] = (rho * S_w * l_ref)/(2*W/g)*C['X,aplha']
A['z,alpha'] = (rho * S_w * l_ref)/(2*W/g)*C['Z,aplha']
A['m,alpha'] = (rho * S_w * l_ref)/(2*W/g)*C['m,aplha']

A['y,beta'] = (rho * S_w * l_ref)/(2*W/g)*C['Y,beta']
A['l,beta'] = (rho * S_w * b_w * l_ref^2)/(2*I['xx_b'])*C['l,beta']
A['n,beta'] = (rho * S_w * b_w * l_ref^2)/(2*I['zz_b'])*C['n,beta']

A['l,alpha'] = (rho * S_w * b_w * l_ref^2)/(2*I['xx_b'])*C['l,aplha']
A['m,beta'] = (rho * S_w * cbar_w * l_ref^2)/(2*I['yy_b'])*C['m,beta']
A['n,alpha'] = (rho * S_w * b_w * l_ref^2)/(2*I['zz_b'])*C['n,aplha']

A['y,pswoosh'] = (rho * S_w * b_w)/(4*W/g)*C['Y,pbar']
A['l,pswoosh'] = (rho * S_w * b_w^2 * l_ref)/(4*I['xx_b'])*C['l,pbar']
A['n,pswoosh'] = (rho * S_w * B_w^2 * l_ref)/(4*I['zz_b'])*C['n,pbar']

A['x,qswoosh'] = (rho * S_w * cbar_w)/(4*W/g)*C['X,qbar']
A['z,qswoosh'] = (rho * S_w * cbar_w)/(4*W/g)*C['Z,qbar']
A['m,qswoosh'] = (rho * S_w * cbar_w^2 * l_ref)/(4*I['yy_b'])*C['m,qbar']

A['y,rswoosh'] = (rho * S_w * b_w)/(4*W/g)*C['Y,rbar']
A['l,rswoosh'] = (rho * S_w * b_w^2 * l_ref)/(4*I['xx_b'])*C['l,rbar']
A['n,rswoosh'] = (rho * S_w * b_w^2 * l_ref)/(4*I['zz_b'])*C['n,rbar']

D['y,delta_a'] = (rho * S_w * l_ref)/(2*W/g)*C['Y,delta_a']
D['l,delta_a'] = (rho * S_w * l_ref^2)/(2*I['xx_b'])*C['l,delta_a']
D['n,delta_a'] = (rho * S_w * l_ref^2)/(2*I['zz_b'])*C['n,delta_a']

D['x,delta_e'] = (rho * S_w * l_ref)/(2*W/g)*C['X,delta_e']
D['z,delta_e'] = (rho * S_w * l_ref)/(2*W/g)*C['Z,delta_e']
D['m,delta_e'] = (rho * S_w * cbar_w * l_ref**2)/(2*I['yy_b'])*C['m,delta_e']

D['y,delta_r'] = (rho * S_w * l_ref)/(2*W/g)*C['Y,delta_r']
D['l,delta_r'] = (rho * S_w * b_w * l_ref**2)/(2*I['xx_b'])*C['l,delta_r']
D['n,delta_r'] = (rho * S_w * b_w * l_ref**2)/(2*I['zz_b'])*C['n,delta_r']
