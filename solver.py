from std_includes import *
from sympy import Matrix,MatrixSymbol,Identity
#from scipy import zeros,array
from numpy import * #linalg,zeros,array

from variables import *
from equations import *

from time import sleep,time

deltamuprime = 0.0
deltabetaprime = 0.0
deltaalphaprime = 0.0
deltapswooshprime = 0.0
deltaqswooshprime = 0.0
deltarswooshprime = 0.0
deltazeta_xprime = 0.0
deltazeta_yprime = 0.0
deltazeta_zprime = 0.0
deltaphi_0prime = 0.0
deltatheta_0prime = 0.0
deltapsiprime = 0.0

deltadelta_a = 0.1
deltadelta_e = 0.1
deltadelta_r = 0.1

deltamu = 0.001   
deltabeta = 0.0  
deltaalpha = 0.0
deltapswoosh = 0.0
deltaqswoosh = 0.0
deltarswoosh = 0.0
deltazeta_x = 1.0
deltazeta_y = 0.0
deltazeta_z = 0.0
deltaphi_0 = 0.0
deltatheta_0 = 0.0
deltapsi = 0.0

tau = lambda t: (V_0 * t / l_ref).magnitude


#   ****    First Matrix    ****

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

charlie = array(([[deltadelta_a],
                [deltadelta_e],
                [deltadelta_r]]),dtype=float)
    
#   ****    Fifth Matrix    ****

delta = array(([[A['x,mu'],A['g']*sin(phi_0)*cos(theta_0),A['x,alpha']-A['g']*(tan(phi_0)*sin(phi_0)*cos(theta_0)).magnitude,0,A['x,qswoosh'],0,0,0,0,0,-A['g']*cos(theta_0),0],
               [-A['g']*sin(phi_0)*cos(theta_0),A['y,beta'],-A['g']*tan(phi_0)*sin(theta_0),A['y,pswoosh'],0,A['y,rswoosh']-1,0,0,0,A['g']*cos(phi_0)*cos(theta_0),-A['g']*sin(phi_0)*sin(theta_0),0],
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

#     answer = array(([[deltamuprime],
#                     [deltabetaprime],
#                     [deltaalphaprime],
#                     [deltapswooshprime],
#                     [deltaqswooshprime],
#                     [deltarswooshprime],
#                     [deltazeta_xprime],
#                     [deltazeta_yprime],
#                     [deltazeta_zprime],
#                     [deltaphi_0prime],
#                     [deltatheta_0prime],
#                     [deltapsiprime]]),dtype=float)


start = time()

while(True):
#   ****    Sixth Matrix    ****
    echo = array(([[deltamu],
                  [deltabeta],
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
    a = Matrix(bravo) * Matrix(charlie) # control surfaces
    b = Matrix(delta) * Matrix(echo) # model
    c = a + b
     
    ans = alphaInv * c
    
    print(ans)
    end = time()
    timestep = end - start
    start = time()
    tau_0 = tau(timestep)
    
    deltamu += ans[0] * tau_0 
    deltabeta += ans[1] * tau_0
    deltaalpha += ans[2] * tau_0
    deltapswoosh += ans[3] * tau_0
    deltaqswoosh += ans[4] * tau_0
    deltarswoosh += ans[5] * tau_0
    deltazeta_x += ans[6] * tau_0
    deltazeta_y += ans[7] * tau_0
    deltazeta_z += ans[8] * tau_0
    deltaphi_0 += ans[9] * tau_0
    deltatheta_0 += ans[10] * tau_0
    deltapsi += ans[11] * tau_0
