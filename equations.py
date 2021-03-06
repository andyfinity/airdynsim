"""
equations

You should not edit this file unless there is an equation error.  This file 
contains all of the equations that make solver.py work.
"""
from std_includes import *
from variables import *

i["xy"] = (I["xy_b"]/I["xx_b"])
i["xz"] = (I["xz_b"]/I["xx_b"])
i["yx"] = (I["xy_b"]/I["yy_b"])
i["yz"] = (I["yz_b"]/I["yy_b"])
i["zx"] = (I["xz_b"]/I["zz_b"])
i["zy"] = (I["yz_b"]/I["zz_b"])


C['L0'] = (W / (1/2 * rho * V_0 ** 2 * S_w))
C['L'] = (W * cos(theta_0) / (1/2 * rho * V_0 ** 2 * S_w * cos(phi_0)))
C['D'] = C['D0'] + (C['D,alpha'] * C['L0'] / (2 * C['L,alpha'])) * ((C['L'] / C['L0']) ** 2 - 1)
C['D,alpha'] = C['D,alpha'] * C['L'] / C['L0']
C['X,alpha'] = C['L'] - C['D,alpha']
C['Z,alpha'] = - C['L,alpha'] - C['D']

deltaalpha = (C['L'] - C['L0']) / C['L,alpha']
phi = -deltaalpha

C['X,alpha'] = C['L'] - C['D,alpha']
C['Z,alpha'] = C['L,alpha'] - C['D']

B['x,muprime'] = (rho * S_w * cbar_w * C['X,muhat'] / (4 * W / g))
B['z,muprime'] = (rho * S_w * cbar_w * C['Z,muhat'] / (4 * W / g))
B['m,muprime'] = (rho * S_w * cbar_w ** 2 * l_ref * C['m,muhat'] / (4 * I['yy_b']))
B['x,alphaprime'] = (rho * S_w * cbar_w * C['X,alphahat'] / (4 * W / g))
B['z,alphaprime'] = (rho * S_w * cbar_w * C['Z,alphahat'] / (4 * W / g))
B['m,alphaprime'] = (rho * S_w * cbar_w ** 2 * l_ref * C['m,alphahat'] / (4 * I['yy_b']))

A['g'] = (g * l_ref / V_0 ** 2)
A['x,mu'] = (rho * S_w * l_ref / (2 * W / g)) * (-(2-M**2)/(1-M**2) * C['D'] + (T[',V'] * cos(alpha_T0)) / (0.5 * rho * V_0 * S_w))
A['z,mu'] = (rho * S_w * l_ref / (2 * W / g)) * (-(2-M**2)/(1-M**2) * C['L'] + (T[',V'] * sin(alpha_T0)) / (0.5 * rho * V_0 * S_w))
A['m,mu'] = (rho * S_w * cbar_w * l_ref** 2 / (2 * I['yy_b'])) * ((2-M**2)/(1-M**2) * C['m'] + (T[',V'] * (z_T * cos(alpha_T0) + x_T * sin(alpha_T0))) / (0.5 * rho * V_0 * S_w * cbar_w))

A['x,alpha'] = ((rho * S_w * l_ref)/(2*W/g)*C['X,alpha'])
A['z,alpha'] = ((rho * S_w * l_ref)/(2*W/g)*C['Z,alpha'])
A['m,alpha'] = ((rho * S_w * l_ref)/(2*W/g)*C['m,alpha'])

A['y,beta'] = ((rho * S_w * l_ref)/(2*W/g)*C['Y,beta'])
A['l,beta'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,beta'])
A['n,beta'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,beta'])

A['l,alpha'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,alpha'])
A['m,beta'] = ((rho * S_w * cbar_w * l_ref ** 2)/(2*I['yy_b'])*C['m,beta'])
A['n,alpha'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,alpha'])

A['y,pswoosh'] = ((rho * S_w * b_w)/(4*W/g)*C['Y,pbar'])
A['l,pswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['xx_b'])*C['l,pbar'])
A['n,pswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['zz_b'])*C['n,pbar'])

A['x,qswoosh'] = ((rho * S_w * cbar_w)/(4*W/g)*C['X,qbar'])
A['z,qswoosh'] = ((rho * S_w * cbar_w)/(4*W/g)*C['Z,qbar'])
A['m,qswoosh'] = ((rho * S_w * cbar_w ** 2 * l_ref)/(4*I['yy_b'])*C['m,qbar'])

A['y,rswoosh'] = ((rho * S_w * b_w)/(4*W/g)*C['Y,rbar'])
A['l,rswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['xx_b'])*C['l,rbar'])
A['n,rswoosh'] = ((rho * S_w * b_w ** 2 * l_ref)/(4*I['zz_b'])*C['n,rbar'])

D['y,delta_a'] = ((rho * S_w * l_ref)/(2*W/g)*C['Y,delta_a'])
D['l,delta_a'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,delta_a'])
D['n,delta_a'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,delta_a'])

D['x,delta_e'] = ((rho * S_w * l_ref)/(2*W/g)*C['X,delta_e'])
D['z,delta_e'] = ((rho * S_w * l_ref)/(2*W/g)*C['Z,delta_e'])
D['m,delta_e'] = ((rho * S_w * cbar_w * l_ref ** 2)/(2*I['yy_b'])*C['m,delta_e'])

D['y,delta_r'] = ((rho * S_w * l_ref)/(2*W/g)*C['Y,delta_r'])
D['l,delta_r'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['xx_b'])*C['l,delta_r'])
D['n,delta_r'] = ((rho * S_w * b_w * l_ref ** 2)/(2*I['zz_b'])*C['n,delta_r'])

eta['xx'] = (A['g'] * (I['xz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0) - I['xy_b'] * sin(phi_0) * cos(theta_0)) / I['xx_b'])
eta['xy'] = (h['z_b'] * l_ref / (I['xx_b'] * V_0)) + (A['g'] * ((I['zz_b'] - I['yy_b']) * sin(phi_0) * cos(theta_0) - 2 * I['yz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0) + I['xz_b'] * tan(phi_0) * sin(theta_0)) / I['xx_b'])
eta['xz'] = (h['y_b'] * l_ref / (I['xx_b'] * V_0)) + (A['g'] * ((I['yy_b'] - I['zz_b']) * tan(phi_0) * sin(phi_0) * cos(theta_0) - 2 * I['yz_b'] * sin(phi_0) * cos(theta_0) + I['xy_b'] * tan(phi_0) * sin(theta_0)) / I['xx_b'])
eta['yx'] = (h['z_b'] * l_ref / (I['yy_b'] * V_0)) + (A['g'] * ((I['zz_b'] - I['xx_b']) * sin(phi_0) * cos(theta_0) - 2 * I['xz_b'] * tan(phi_0) * sin(theta_0) + I['xz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0)) / I['yy_b']) 
eta['yy'] = (A['g'] * (I['xy_b'] * sin(phi_0) * cos(theta_0) - I['xz_b'] * tan(phi_0) * sin(theta_0)) / I['yy_b'])
eta['yz'] = (h['x_b'] * l_ref / (I['yy_b'] * V_0)) + (A['g'] * ((I['zz_b'] - I['xx_b']) * tan(phi_0) * sin(theta_0) - 2 * I['yz_b'] * sin(phi_0) * cos(theta_0) + I['xy_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0)) / I['yy_b']) 
eta['zx'] = (h['y_b'] * l_ref / (I['zz_b'] * V_0)) + (A['g'] * ((I['yy_b'] - I['xx_b']) * tan(phi_0) * sin(phi_0) * cos(theta_0) - 2 * I['xy_b'] * tan(phi_0) * sin(theta_0) + I['yz_b'] * sin(phi_0) * cos(theta_0)) / I['zz_b'])
eta['zy'] = (h['x_b'] * l_ref / (I['zz_b'] * V_0)) + (A['g'] * ((I['yy_b'] - I['xx_b']) * tan(phi_0) * sin(theta_0) - 2 * I['xy_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0) + I['xz_b'] * sin(phi_0) * cos(theta_0)) / I['zz_b'])
eta['zz'] = (A['g'] * (-I['yz_b'] * tan(phi_0) * sin(theta_0) - I['xz_b'] * tan(phi_0) * sin(phi_0) * cos(theta_0)) / I['zz_b'])



