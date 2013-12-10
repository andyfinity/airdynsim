from std_includes import *
from sympy import *     # matrix, MatrixSymbol
from numpy import *     # sin,cos,tan
from scipy import *     # linalg.inv

from variables import *
from equations import *



#   ****    First Matrix    ****

alpha = matrix(identity(12))

alpha[0,0] = 1-B['x,muprime']
alpha[0,2] = -B['x,alphaprime']
alpha[2,0] = -B['z,muprime']
alpha[2,2] = 1-B['z,alphaprime'] 
alpha[3,4] = -i['xy']
alpha[3,5] = -i['xz']
alpha[4,0] = -B['m,muprime']
alpha[4,2] = -B['m,alphaprime']
alpha[4,3] = -i['yx']
alpha[4,5] = -i['yz']
alpha[5,3] = -i['zx']
alpha[5,4] = -i['zy']

alphaInv = linalg.inv(alpha)


#   ****    Second Matrix   ****

deltamuprime = None
deltabetaprime = None
deltaalphaprime = None
deltapswooshprime = None
deltaqswooshprime = None
deltarswooshprime = None
deltazeta_xprime = None
deltazeta_yprime = None
deltazeta_zprime = None
deltaphi_0prime = None
deltatheta_0prime = None
deltapsiprime = None


answer = MatrixSymbol(array([[deltamuprime],
                             [deltabetaprime],
                             [deltaalphaprime],
                             [deltapswooshprime],
                             [deltaqswooshprime],
                             [deltarswooshprime],
                             [deltazeta_xprime],
                             [deltazeta_yprime],
                             [deltazeta_zprime],
                             [deltaphi_0prime],
                             [deltatheta_0prime],
                             [deltapsiprime]]),1,12)

#   ****    Third Matrix    ****

bravo = matrix(zeros([12,3]))

bravo[0,1] = D['x,delta_a']
bravo[1,0] = D['y,delta_a']
bravo[1,2] = D['y,delta_r']
bravo[3,1] = D['z,delta_e']
bravo[4,0] = D['l,delta_a']
bravo[4,2] = D['l,delta_r']
bravo[5,1] = D['m,detla_e']
bravo[6,0] = D['n,delta_a']
bravo[6,2] = D['n,delta_r']

#   ****    Fourth Matrix   ****

charle = MatrixSymbol(array([[deltadelta_a],[deltadelta_e],[deltadelta_r]]),3,12)
    
#   ****    Fifth Matrix    ****

delta = matrix(([A['x,mu'],A['g']*sin(phi_0)*cos(theta_0),A['x,alpha']-A['g']*tan(phi_0)*sin(phi_0)*cos(theta_0),0,A['x,qswoosh'],0,0,0,0,0,-A['g']*cos(theda_0),0],
                [-A['g']*sin(phi_0)*cos(theta),A['y,beta'],-A['g']*tan(phi)*sin(theta),A['y,pswoosh'],0,A['y,rswoosh']-1,0,0,0,A['g']*cos(phi_0)*cos(theta_0),-A['g']*sin(phi_0)*sin(theta_0),0],
                [A['z,mu']+A['g']*tan(phi_0)*sin(phi_0)*cos(theta_0),A['g']*tan(phi_0)*sin(theta_0),A['z,alpha'],0,A['z,qswoosh']+1,0,0,0,0,-A['g']*sin(phi_0)*cos(theta_0),-A['g']*cos(phi_0)*sin(theta_0),0],
                [0,A['l,beta'],A['l,alpha'],A['l,pswoosh']+eta['xx'],-eta['x,y'],A['l,rswoosh'],0,0,0,0,0,0],
                [A['m,mu'],A['m,beta'],A['m,alpha'],eta['y,x'],A['m,qswoosh']+eta['yy'],-eta['y,z'],0,0,0,0,0,0],
                [0,A['n,beta'],A['n,alpha'],A['n,pswoosh']-eta['z,x'],eta['z,y'],A['n,rswoosh'],0,0,0,0,0,0],
                [cos(theta_0),sin(phi_0)*sin(theta_0),cos(phi_0)*sin(theta_0),0,0,0,0,0,0,0,-sin(theta_0),0],
                [0,cos(phi_0),-sin(phi_0),0,0,0,0,0,0,0,0,cos(theta_0)],
                [-sin(theta_0),sin(phi_0)*cos(theta_0),cos(phi_0)*cos(theta_0),0,0,0,0,0,0,0,-cos(theta_0),0],
                [0,0,0,1,sin(phi_0)*tan(theta_0),cos(phi_0)*tan(theta_0),0,0,0,0,A['g']*tan(phi_0)/cos(theta_0),0],
                [0,0,0,0,cos(phi_0),-sin(phi_0),0,0,0,-A['g']*tan(phi_0)*cos(theta_0),0,0],
                [0,0,0,0,sin(phi_0)/cos(theta_0),cos(phi_0)*cos(theta_0),0,0,0,0,A['g']*tan(phi_0)*tan(theta_0),0]))


#   ****    Sixth Matrix    ****

echo = MatrixSymbol(array([[deltamu],
                             [deltadeta],
                             [deltaalpha],
                             [deltapswoosh],
                             [deltaqswoosh],
                             [deltarswoosh],
                             [deltazeta_x],
                             [deltazeta_y],
                             [deltazeta_z],
                             [deltaphi_0],
                             [deltatheta_0],
                             [deltapsi]]),1,12)

#   ****    Solve   ****

b = delta * echo

c = a + b

ans = alphaInv * c

answer = ans



