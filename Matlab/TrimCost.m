	function J = TrimCost(OptParam)
%	FLIGHT Cost Function for Longitudinal Trim in Steady Level Flight

%	September 1, 2006   
%	===============================================================
%	Copyright 2006 by ROBERT F. STENGEL.  All rights reserved.

	global TrimHist x u V

	R	=	[1 0 0
			0 1 0
			0 0 1];

% Optimization Vector:
%	1 = Stabilator, rad
%	2 = Throttle, %
%	3 = Pitch Angle, rad
	OptParam;
		
	u	=	[u(1)
			u(2)
			u(3)
			OptParam(2)
			u(5)
			u(6)
			OptParam(1)];
				
	x	=	[V * cos(OptParam(3))
			x(2)
			V * sin(OptParam(3))
			x(4)
			x(5)
			x(6)
			x(7)
			x(8)
			x(9)
			x(10)
			OptParam(3)
			x(12)];
	
	xdot	=	EoM(x,1);
	xCost	=	[xdot(1)
				xdot(3)
				xdot(8)];
	J		=	xCost' * R * xCost;
	ParamCost	=	[OptParam;J];
	TrimHist	=	[TrimHist ParamCost];