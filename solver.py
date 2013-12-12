from std_includes import *
from sympy import Matrix,MatrixSymbol,Identity
#from scipy import zeros,array
from numpy import * #linalg,zeros,array

from variables import *
from equations import *

#   ****    First Matrix    ****

#alpha = Matrix(Identity(12))

alpha = zeros((12,12), dtype=float)

alpha[0,0] = 1-B['x,muprime']
alpha[0,2] = -B['x,alphaprime']
alpha[1,1] = 1
alpha[2,0] = -B['z,muprime']
alpha[2,2] = 1-B['z,alphaprime']
alpha[3,3] = 1
alpha[3,4] = -i['xy']
alpha[3,5] = -i['xz']
alpha[4,0] = -B['m,muprime']
alpha[4,2] = -B['m,alphaprime']
alpha[4,3] = -i['yx']
alpha[4,5] = -i['yz']
alpha[5,5] = 1
alpha[5,3] = -i['zx']
alpha[5,4] = -i['zy']
alpha[6,6] = 1
alpha[7,7] = 1
alpha[8,8] = 1
alpha[9,9] = 1
alpha[10,10] = 1
alpha[11,11] = 1


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

answer = array(([[deltamuprime],
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
                [deltapsiprime]]),dtype=float)


#   ****    Third Matrix    ****

bravo = array(([[0,D['x,delta_e'],0],
               [D['y,delta_a'],0,D['y,delta_r']],
               [0,D['z,delta_e'],0],
               [D['l,delta_a'],0,D['l,delta_r']],
               [0,D['m,delta_e'],0],
               [D['n,delta_a'],0,D['n,delta_r']],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0],
               [0,0,0]]),dtype=float)

#   ****    Fourth Matrix   ****

deltadelta_a = 0.0
deltadelta_e = 0.0
deltadelta_r = 0.0

charlie = array(([[deltadelta_a],
                [deltadelta_e],
                [deltadelta_r]]),dtype=float)
    
#   ****    Fifth Matrix    ****

delta = array(([[A['x,mu'],A['g']*sin(phi_0)*cos(theta_0),A['x,alpha']-A['g']*(tan(phi_0)*sin(phi_0)*cos(theta_0)).magnitude,0,A['x,qswoosh'],0,0,0,0,0,-A['g']*cos(theta_0),0],
               [-A['g']*sin(phi_0)*cos(theta_0),A['y,beta'],-A['g']*tan(phi)*sin(theta_0),A['y,pswoosh'],0,A['y,rswoosh']-1,0,0,0,A['g']*cos(phi_0)*cos(theta_0),-A['g']*sin(phi_0)*sin(theta_0),0],
               [A['z,mu']+A['g']*(tan(phi_0)*sin(phi_0)*cos(theta_0)).magnitude,A['g']*tan(phi_0)*sin(theta_0),A['z,alpha'],0,A['z,qswoosh']+1,0,0,0,0,-A['g']*sin(phi_0)*cos(theta_0),-A['g']*cos(phi_0)*sin(theta_0),0],
               [0,A['l,beta'],A['l,alpha'],A['l,pswoosh']+eta['xx'],-eta['xy'],A['l,rswoosh'],0,0,0,0,0,0],
               [A['m,mu'],A['m,beta'],A['m,alpha'],eta['yx'],A['m,qswoosh']+eta['yy'],-eta['yz'],0,0,0,0,0,0],
               [0,A['n,beta'],A['n,alpha'],A['n,pswoosh']-eta['zx'],eta['zy'],A['n,rswoosh'],0,0,0,0,0,0],
               [cos(theta_0),sin(phi_0)*sin(theta_0),cos(phi_0)*sin(theta_0),0,0,0,0,0,0,0,-sin(theta_0),0],
               [0,cos(phi_0),-sin(phi_0),0,0,0,0,0,0,0,0,cos(theta_0)],
               [-sin(theta_0),sin(phi_0)*cos(theta_0),cos(phi_0)*cos(theta_0),0,0,0,0,0,0,0,-cos(theta_0),0],
               [0,0,0,1,sin(phi_0)*tan(theta_0),cos(phi_0)*tan(theta_0),0,0,0,0,A['g']*tan(phi_0)/cos(theta_0),0],
               [0,0,0,0,cos(phi_0),-sin(phi_0),0,0,0,-A['g']*tan(phi_0)*cos(theta_0),0,0],
               [0,0,0,0,sin(phi_0)/cos(theta_0),cos(phi_0)*cos(theta_0),0,0,0,0,A['g']*tan(phi_0)*tan(theta_0),0]]),dtype=float)

#   ****    Sixth Matrix    ****
deltamu = 1.0    
deltadeta = 1.0  
deltaalpha = 1.0 
deltapswoosh = 1.0
deltaqswoosh = 1.0
deltarswoosh = 1.0
deltazeta_x = 1.0
deltazeta_y = 1.0
deltazeta_z = 1.0
deltaphi_0 = 1.0
deltatheta_0 = 1.0
deltapsi = 1.0

echo = array(([[deltamu],
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
              [deltapsi]]),dtype=float)

#   ****    Solve   ****

a = Matrix(bravo) * Matrix(charlie)
# print(Matrix(a))
 
b = Matrix(delta) * Matrix(echo)
 
c = a + b
 
ans = alphaInv * c
return ans
print(ans)
##print(alpha)
##print()
##print(delta)

