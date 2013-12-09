from std_includes import *

theta_0 = 0 * ur.degree
phi_0 = 60 * ur.degree

l_ref = 13.6 * ur.ft
rho = 0.0023769 * ur.slug * ur.ft ** -3
S_w = 185 * ur.ft ** 2
b_w = 33 * ur.ft
W = 2800 * ur.lbf
V_0 = 180 * ur.ft / ur.sec

cbar_w = S_w / b_w

h["x_b"] = 0 * ur.slug * ur.ft ** 2
h["y_b"] = 0 * ur.slug * ur.ft ** 2
h["z_b"] = 0 * ur.slug * ur.ft ** 2

I["xx_b"] = 1000 * ur.slug * ur.ft ** 2
I["xy_b"] = 3000 * ur.slug * ur.ft ** 2
I["xz_b"] = 30 * ur.slug * ur.ft ** 2
I["yx_b"] = 3500 * ur.slug * ur.ft ** 2
I["yy_b"] = 3000 * ur.slug * ur.ft ** 2
I["yz_b"] = 0 * ur.slug * ur.ft ** 2   
I["zx_b"] = 30 * ur.slug * ur.ft ** 2  
I["zy_b"] = 0 * ur.slug * ur.ft ** 2
I["zz_b"] = 3500 * ur.slug * ur.ft ** 2   

C['L0'] = 0.393
C['D0'] = 0.050
C['m0'] = 0.000
C['L,muhat'] = 0.000
C['D,muhat'] = 0.000
C['m,muhat'] = 0.000
C['X,muhat'] = -0.013
C['Z,muhat'] = -0.142
C['L,alphahat'] = 1.600
C['D,alphahat'] = 0.000
C['m,alphahat'] = -4.350
C['X,alphahat'] = -0.142
C['Z,alphahat'] = -1.587
C['L,M'] = 0.0
C['D,M'] = 0.0
C['m,M'] = 0.0
C['L,alpha'] = 4.400
C['D,alpha'] = 0.350
C['l,alpha'] = 0.0
C['m,alpha'] = -0.680
C['n,alpha'] = 0.0
C['Y,beta'] = -0.560
C['l,beta'] = -0.075
C['m,beta'] = 0.0
C['n,beta'] = 0.070
C['Y,pbar'] = 0.000
C['l,pbar'] = -0.410
C['n,pbar'] = -0.0575
C['L,qbar'] = 3.800
C['D,qbar'] = 0.000
C['m,qbar'] = -9.950
C['Y,rbar'] = 0.240
C['l,rbar'] = 0.105
C['n,rbar'] = -0.125