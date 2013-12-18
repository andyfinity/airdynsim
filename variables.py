"""
variables

This is the file to edit if you want to change the initial flight parameters.
"""
from std_includes import *

theta_0 = 0.0 # degree
phi_0 = 0.0 # degree

l_ref = 13.6 # ft
rho = 0.0023769 # slug * ft ** -3
S_w = 185.0 # ft ** 2
b_w = 33.0 # ft
W = 2800.0 # lbf
V_0 = 180.0 # ft / sec
elevation = 3300.0 # ft
a = 1102.0 # ft / sec 

cbar_w = S_w / b_w
M = V_0 / a

h["x_b"] = 0.0 # slug * ft ** 2
h["y_b"] = 0.0 # slug * ft ** 2
h["z_b"] = 0.0 # slug * ft ** 2

I["xx_b"] = 1000.0 # slug * ft ** 2
I["xy_b"] = 3000.0 # slug * ft ** 2
I["xz_b"] = 30.0 # slug * ft ** 2
I["yx_b"] = 3500.0 # slug * ft ** 2
I["yy_b"] = 3000.0 # slug * ft ** 2
I["yz_b"] = 0.0 # slug * ft ** 2   
I["zx_b"] = 30.0 # slug * ft ** 2  
I["zy_b"] = 0.0 # slug * ft ** 2
I["zz_b"] = 3500.0 # slug * ft ** 2   

# C['L'] = W/(0.5 * rho * V_0 ** 2 * S_w) # as seen on page 794
C['D0'] = 0.050
C['m'] = 0.000
C['L,muhat'] = 0.000
C['D,muhat'] = 0.000
C['L,alphahat'] = 1.600
C['D,alphahat'] = 0.000
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
C['L,qbar'] = 3.800
C['D,qbar'] = 0.000

# Thrust variables
alpha_T0 = 0.0 # degree
T[',V'] = -0.1 
x_T = 0.0 # ft
z_T = 0.0 # ft
T[''] = 250 # lbf # thrust

# All following numbers are from page 938 and should be calculated
# Some can be found on pages 792-794

C['X_0'] = -0.097
C['Z_0'] = -0.786
C['m_0'] = 0.000

C['X,muhat'] = -0.013
C['Z,muhat'] = -0.142
C['m,muhat'] = 0.000

C['X,alphahat'] = -0.142
C['Z,alphahat'] = -1.587
C['m,alphahat'] = -4.350

C['X,mu'] = 0.0
C['Z,mu'] = 0.0
C['m,mu'] = 0.0

C['l,alpha'] = 0.0
C['m,alpha'] = -0.677
C['n,alpha'] = 0.0

C['Y,beta'] = -0.560
C['l,beta'] = -0.0685
C['m,beta'] = 0.0
C['n,beta'] = 0.0764

C['Y,pbar'] = 0.0214
C['l,pbar'] = -0.4035
C['n,pbar'] = -0.0326

C['X,qbar'] = -0.339
C['Z,qbar'] = -3.785
C['m,qbar'] = -9.950

C['Y,rbar'] = 0.239
C['l,rbar'] = 0.130
C['n,rbar'] = -0.131

# TODO: Where are these defined?

#   Changed to 1.0 for testing

C['Y,delta_a'] = 1.0
C['l,delta_a'] = 1.0 # page 568, 5.7.3?
C['n,delta_a'] = 1.0

C['X,delta_e'] = 1.0 # around page 386?
C['Z,delta_e'] = 1.0
C['m,delta_e'] = 1.0

C['Y,delta_r'] = 1.0 # TODO: find equations
C['l,delta_r'] = 1.0
C['n,delta_r'] = 1.0
