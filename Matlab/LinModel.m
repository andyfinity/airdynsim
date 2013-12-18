	function xdotj = LinModel(tj,xj)
%	FLIGHT Equations of Motion for Linear Model (Jacobian) Evaluation,
%	with dummy state elements added for controls

%	September 1, 2006   
%	===============================================================
%	Copyright 2006 by ROBERT F. STENGEL.  All rights reserved.

	global u
	
	x		=	xj(1:12);
	u		=	xj(13:19);

	xdot	=	EoM(tj,x);
	xdotj	=	[xdot;0;0;0;0;0;0;0];