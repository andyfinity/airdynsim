from sympy import *
from numpy import *
from scipy import *

#from variables import *
#from equations import *

#   ****    First Matrix    ****

##alpha = matrix(identity(12))

##alpha[0,0] = 1-B['x,muprime']
##alpha[0,2] = -B['x,alphaprime']
##alpha[2,0] = -B['z,muprime']
##alpha[2,2] = 1-B['z,alphaprime']
##alpha[3,4] = -i['xy']
##alpha[3,5] = -i['xz']
##alpha[4,0] = -B['m,muprime']
##alpha[4,2] = -B['m,alphaprime']
##alpha[4,3] = -i['yx']
##alpha[4,5] = -i['yz']
##alpha[5,3] = -i['zx']
##alpha[5,4] = -i['zy']

##alphaInv = linalg.inv(alpha)
#   ****    Second Matrix   ****

##answer = MatrixSymbol(array([[deltamuprime],
##                             [deltadetaprime],
##                             [deltaalphaprime],
##                             [deltapbarprime],
##                             [deltaqbarprime],
##                             [deltarbarprime],
##                             [deltazeta_xprime],
##                             [deltazeta_yprime],
##                             [deltazeta_zprime],
##                             [deltaphiprime],
##                             [deltathetaprime],
##                             [deltapsiprime]]),1,12)

#   ****    Third Matrix    ****

##bravo = matrix(zeros([12,3]))
##
##bravo[0,1] = D['x,delta_a']
##bravo[1,0] = D['y,delta_a']
##bravo[1,2] = D['y,delta_r']
##bravo[3,1] = D['z,delta_e']
##bravo[4,0] = D['l,delta_a']
##bravo[4,2] = D['l,delta_r']
##bravo[5,1] = D['m,detla_e']
##bravo[6,0] = D['n,delta_a']
##bravo[6,2] = D['n,delta_r']

#   ****    Fourth Matrix   ****

##charle = MatrixSymbol(array([[deltadelta_a],[deltadelta_e],[deltadelta_r]]),3,12)
    
#   ****    Fifth Matrix    ****

##delta = matrix(([A['x,mu'],A['g']*S['phi_0']*C['theta_0'],1,0,1,0,0,0,0,0,1,0],
##               [1,1,1,1,0,1,0,0,0,1,1,0]))

##delta[0,0]  = 
##delta[0,1]  = 
##delta[0,2]  = 
##delta[0,4]  = 
##delta[0,10] = 
##delta[1,0]  = 
##delta[1,1]  = 
##delta[1,2]  = 
##delta[1,3]  = 
##delta[1,5]  = 
##delta[1,9]  = 
##delta[1,10] = 
##delta[2,0]  = 
##delta[2,1]  = 
##delta[2,2]  = 
##delta[2,4]  = 
##delta[2,9]  = 
##delta[2,10] = 
##delta[3,1]  = 
##delta[3,2]  = 
##delta[3,3]  = 
##delta[3,4]  = 
##delta[3,5]  = 
##delta[4,0]  = 
##delta[4,1]  = 
##delta[4,2]  = 
##delta[4,3]  = 
##delta[4,4]  = 
##delta[4,5]  = 
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[
##delta[















#   ****    Sixth Matrix    ****

##echo = MatrixSymbol(array([[deltamu],
##                             [deltadeta],
##                             [deltaalpha],
##                             [deltapbar],
##                             [deltaqbar],
##                             [deltarbar],
##                             [deltazeta_x],
##                             [deltazeta_y],
##                             [deltazeta_z],
##                             [deltaphi],
##                             [deltatheta],
##                             [deltapsi]])1,12)


#beta = array([9,8,5,8,4,2,6,8,5,4,0,1])
#charle = array([2,6,7,8,4,2,4,5,6,7,0,1])
#delta = array([a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2])
#x = linalg.solve(alpha,beta)
#y = x+charle
#z = delta + alpha


