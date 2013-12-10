from scipy import *
from numpy import *
from sumpy import *

from equations import *
from variables import *

 ##answer = MatrixSymbol(array([[deltamuprime],
 ##                             [deltadetaprime],
 ##                             [deltaalphaprime],
##                             [deltapswooshprime],
##                             [deltaqswooshprime],
##                             [deltarswooshprime],
 ##                             [deltazeta_xprime],
 ##                             [deltazeta_yprime],
 ##                             [deltazeta_zprime],
-##                             [deltaphiprime],
-##                             [deltathetaprime],
+##                             [deltaphi_0prime],
+##                             [deltatheta_0prime],
 ##                             [deltapsiprime]]),1,12)
 
 #   ****    Third Matrix    ****
@@ -58,78 +58,18 @@ from scipy import *
     
 #   ****    Fifth Matrix    ****
 
-##delta = matrix(([A['x,mu'],A['g']*S['phi_0']*C['theta_0'],1,0,1,0,0,0,0,0,1,0],
-##               [1,1,1,1,0,1,0,0,0,1,1,0]))
-
-##delta[0,0]  = 
-##delta[0,1]  = 
-##delta[0,2]  = 
-##delta[0,4]  = 
-##delta[0,10] = 
-##delta[1,0]  = 
-##delta[1,1]  = 
-##delta[1,2]  = 
-##delta[1,3]  = 
-##delta[1,5]  = 
-##delta[1,9]  = 
-##delta[1,10] = 
-##delta[2,0]  = 
-##delta[2,1]  = 
-##delta[2,2]  = 
-##delta[2,4]  = 
-##delta[2,9]  = 
-##delta[2,10] = 
-##delta[3,1]  = 
-##delta[3,2]  = 
-##delta[3,3]  = 
-##delta[3,4]  = 
-##delta[3,5]  = 
-##delta[4,0]  = 
-##delta[4,1]  = 
-##delta[4,2]  = 
-##delta[4,3]  = 
-##delta[4,4]  = 
-##delta[4,5]  = 
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-##delta[
-
-
-
-
-
-
-
-
-
-
-
-
-
+##delta = matrix(([A['x,mu'],A['g']*sin(phi_0)*cos(theta_0),A['x,alpha']-A['g']*tan(phi_0)*sin(phi_0)*cos(theta_0),0,A['x,qswoosh'],0,0,0,0,0,-A['g']*cos(theda_0),0],
+##                [-A['g']*sin(phi_0)*cos(theta),A['y,beta'],-A['g']*tan(phi)*sin(theta),A['y,pswoosh'],0,A['y,rswoosh']-1,0,0,0,A['g']*cos(phi_0)*cos(theta_0),-A['g']*sin(phi_0)*sin(theta_0),0],
+##                [A['z,mu']+A['g']*tan(phi_0)*sin(phi_0)*cos(theta_0),A['g']*tan(phi_0)*sin(theta_0),A['z,alpha'],0,A['z,qswoosh']+1,0,0,0,0,-A['g']*sin(phi_0)*cos(theta_0),-A['g']*cos(phi_0)*sin(theta_0),0],
+##                [0,A['l,beta'],A['l,alpha'],A['l,pswoosh']+eta['xx'],-eta['x,y'],A['l,rswoosh'],0,0,0,0,0,0],
+##                [A['m,mu'],A['m,beta'],A['m,alpha'],eta{'y,x'],A['m,qswoosh']+eta['yy'],-eta['y,z'],0,0,0,0,0,0],
+##                [0,A['n,beta'],A['n,alpha'],A['n,pswoosh']-eta['z,x'],eta['z,y'],A['n,rswoosh'],0,0,0,0,0,0],
+##                [cos(theta_0),sin(phi_0)*sin(theta_0),cos(phi_0)*sin(theta_0),0,0,0,0,0,0,0,-sin(theta_0),0],
+##                [0,cos(phi_0),-sin(phi_0),0,0,0,0,0,0,0,0,cos(theta_0)],
+##                [-sin(theta_0),sin(phi_0)*cos(theta_0),cos(phi_0)*cos(theta_0),0,0,0,0,0,0,0,-cos(theta_0),0],
+##                [0,0,0,1,sin(phi_0)*tan(theta_0),cos(phi_0)*tan(theta_0),0,0,0,0,A['g']*tan(phi_0)/cos(theta_0),0],
+##                [0,0,0,0,cos(phi_0),-sin(phi_0),0,0,0,-A['g']*tan(phi_0)*cos(theta_0),0,0],
+##                [0,0,0,0,sin(phi_0)/cos(theta_0),cos(phi_0)*cos(theta_0),0,0,0,0,A['g']*tan(phi_0)*tan(theta_0),0]))
 
 
 #   ****    Sixth Matrix    ****
@@ -137,22 +77,24 @@ from scipy import *
 ##echo = MatrixSymbol(array([[deltamu],
 ##                             [deltadeta],
 ##                             [deltaalpha],
-##                             [deltapbar],
-##                             [deltaqbar],
-##                             [deltarbar],
+##                             [deltapswoosh],
+##                             [deltaqswoosh],
+##                             [deltarswoosh],
 ##                             [deltazeta_x],
 ##                             [deltazeta_y],
 ##                             [deltazeta_z],
-##                             [deltaphi],
-##                             [deltatheta],
+##                             [deltaphi_0],
+##                             [deltatheta_0],
 ##                             [deltapsi]])1,12)
 
 
-#beta = array([9,8,5,8,4,2,6,8,5,4,0,1])
-#charle = array([2,6,7,8,4,2,4,5,6,7,0,1])
-#delta = array([a2,b2,c2,d2,e2,f2,g2,h2,i2,j2,k2,l2])
-#x = linalg.solve(alpha,beta)
-#y = x+charle
-#z = delta + alpha
+a = bravo * charle
+
+b = delta * echo
+
+c = a + b
+
+ans = alphaInv * c
+
 
 
