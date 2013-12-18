	function [CD,CL,CY,Cl,Cm,Cn,Thrust]	=	AeroModelAlpha(x,u,Mach,alphar,betar,V)
%	FLIGHT Aerodynamic Coefficients of the Aircraft, Thrust Model,
%	and Geometric and Inertial Properties

%	September 1, 2006   
%	===============================================================
%	Copyright 2006 by ROBERT F. STENGEL.  All rights reserved.

%	Business Jet -- High-Angle-of-Attack, Mach-Independent Model
%	Landing Gear: Up (GEAR = 0)
%	Flap Setting, u(6): 0 deg
%	Symmetric Spoiler: Closed (SPOIL = 0)

	global m Ixx Iyy Izz Ixz S b c GEAR CONHIS SPOIL SMI
 
%	Typical Mass and Inertial Properties
	m		=	4536;				% Mass, kg
	Ixx		=	35926.5;			% Roll Moment of Inertia, kg-m^2
	Iyy		=	33940.7;			% Pitch Moment of Inertia, kg-m^2
	Izz		=	67085.5;			% Yaw Moment of Inertia, kg-m^2
	Ixz		=	3418.17;			% Nose-high(low) Product of Inertia, kg-m^2
	
%	Geometric Properties
	c		=	2.14;				% Mean Aerodynamic Chord, m
	b		=	10.4;				% Wing Span, m
	S		=	21.5;				% Reference Area, m^2
	ARw		=	5.02;				% Wing Aspect Ratio
	taperw	=	0.507;				% Wing Taper Ratio
	sweepw	=	13 * .01745329;		% Wing 1/4-chord sweep angle, rad
	ARh		=	4;					% Horizontal Tail Aspect Ratio
	sweeph	=	25 * .01745329;		% Horiz Tail 1/4-chord sweep angle, rad
	ARv		=	0.64;				% Vertical Tail Aspect Ratio
	sweepv	=	40 * .01745329;		% Vert Tail 1/4-chord sweep angle, rad
	lvt		=	4.72;				% Vert Tail Length, m
    
%	Aerodynamic Data Tables for Business Jet Aircraft 
    [AlphaTable,CLTable,CDTable,CmTable,CmdETable,CYBetaTable,ClBetaTable, ...
		CnBetaTable,CldATable,CndATable,CldRTable,CndRTable] = DataTable;
	
%	Thrust Properties
	StaticThrust	=	26243.2;	% Static Thrust @ Sea Level, N

	alphadeg	=	57.29578 * alphar;
	
%	Current Thrust
	[airDens,airPres,temp,soundSpeed] = Atmos(-x(6));
	Thrust			=	u(4) * StaticThrust * (airDens / 1.225)^0.7 ...
						* (1 - exp((-x(6) - 17000) / 2000));
									% Thrust at Altitude, N
	
%	Current Longitudinal Characteristics
%	====================================

%	Lift Coefficient
	CLStatic	=	interp1(AlphaTable,CLTable,alphadeg);
									% Static Lift Coefficient

	CLqr	=	4.231 * c / (2 * V);
									% Pitch-Rate Effect, per rad/s
	
	CLdSr	=	1.08;				% Stabilator Effect, per rad
	
	CLdEr	=	0.5774;				% Elevator Effect, per rad

	CL	=	CLStatic + CLqr*x(8) + CLdSr*u(7) + CLdEr*u(1);
									% Total Lift Coefficient
	
%	Drag Coefficient
	CDStatic	=	interp1(AlphaTable,CDTable,alphadeg);
									% Static Drag Coefficient

	CD	=	CDStatic;				% Total Drag Coefficient
	
%	Pitching Moment Coefficient
	CmStatic	=	interp1(AlphaTable,CmTable,alphadeg);
									% Static Pitching Moment Coefficient
	CmdEr		=	interp1(AlphaTable,CmdETable,alphadeg);
									% Elevator Effect, per rad

	Cmqr	=	 -18.8 * c / (2 * V);
									% Pitch-Rate + Alpha-Rate Effect, per rad/s
	
	CmdSr	=	-2.291;				% Stabilator Effect, per rad
				

	Cm	=	CmStatic - CL*SMI + Cmqr*x(8) + CmdSr*u(7) + CmdEr*u(1);
									% Total Pitching Moment Coefficient
	
%	Current Lateral-Directional Characteristics
%	===========================================

%	Side-Force Coefficient
	CYBr	=	interp1(AlphaTable,CYBetaTable,alphadeg);
									% Side-Force Slope, per rad

	CYdAr	=	-0.00699;			% Aileron Effect, per rad
	
	CYdRr	=	0.1574;				% Rudder Effect, per rad
	
	CYdASr	=	0.0264;				% Asymmetric Spoiler Effect, per rad

	CY	=	(CYBr*betar + CYdRr*u(3)) + (CYdAr*u(2) + CYdASr*u(5));
									% Total Side-Force Coefficient

%	Yawing Moment Coefficient
	CnBr	=	interp1(AlphaTable,CnBetaTable,alphadeg);
									% Directional Stability, per rad

	Cnpr	=	CL * (1 + 3 * taperw)/(12 * (1 + taperw)) * (b / (2 * V));				
									% Roll-Rate Effect, per rad/s
	
	Cnrr	=	(-2 * (lvt / b) * CnBr - 0.1 * CL^2) * (b / (2 * V));				
									% Yaw-Rate Effect, per rad/s

	CndAr	=	interp1(AlphaTable,CndATable,alphadeg);
									% Aileron Effect, per rad
	
	CndRr	=	interp1(AlphaTable,CndRTable,alphadeg);
									% Rudder Effect, per rad
	
	CndASr	=	-0.0088;			% Asymmetric Spoiler Effect, per rad

	Cn	=	(CnBr*betar + CndRr*u(3)) + Cnrr * x(9) + Cnpr * x(7) ...
			+ (CndAr*u(2) + CndASr*u(5));
									% Total Yawing-Moment Coefficient

%	Rolling Moment Coefficient
	ClBr	=	interp1(AlphaTable,ClBetaTable,alphadeg);
									% Dihedral Effect, per rad
	CLar	=	5.6575;
	Clpr	=	-CLar * (1 + 3 * taperw)/(12 * (1 + taperw)) * (b / (2 * V));				
									% Roll-Rate Effect, per rad/s
	
	Clrr	=	CL * (1 + 3 * taperw)/(12 * (1 + taperw)) * (b / (2 * V));				
									% Yaw-Rate Effect, per rad/s

	CldAr	=	interp1(AlphaTable,CldATable,alphadeg);
									% Aileron Effect, per rad
	
	CldRr	=	interp1(AlphaTable,CldRTable,alphadeg);
									% Rudder Effect, per rad
	
	CldASr	=	-0.01496;			% Asymmetric Spoiler Effect, per rad

	Cl	=	(ClBr*betar + CldRr*u(3)) + Clrr * x(9) + Clpr * x(7) ...
			+ (CldAr*u(2) + CldASr*u(5));
									% Total Rolling-Moment Coefficient