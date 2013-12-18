% FLIGHT --  6-DOF Trim, Linear Model, and Flight Path Simulation
% Businesss Jet Aerodynamic Model

% October 21, 2012  
% ===============================================================
% Copyright 2012 by ROBERT F. STENGEL.  All rights reserved.

clear all
close all

function r = is_octave() 
    r = exist('OCTAVE_VERSION'); 
end 

global GEAR CONHIS SPOIL u x V tuHis deluHis uInc TrimHist SMI MODEL

% This is the SCRIPT FILE.  It contains the Main Program, which:
%    Defines initial conditions
%    Contains aerodynamic data tables (if required)
%    Calculates longitudinal trim condition
%    Calculates stability-and-control derivatives
%    Simulates flight path using nonlinear equations of motion
        
% Functions used by FLIGHT:
%    AeroModel.m    Aerodynamic coefficients of the aircraft, thrust model, and geometric and inertial properties
%    DataTable.m    Tables for AeroModelAlpha.m
%    Atmos.m        Air density, sound speed
%    DCM.m        Direction-cosine matrix
%    EoM.m        Equations of motion for integration
%    LinModel.m    Equations of motion for linear model definition
%    TrimCost.m    Cost function for trim solution
%    WindField.m    Wind velocity components

%    DEFINITION OF THE STATE VECTOR
%        x(1)    = Body-axis x inertial velocity, ub, m/s
%        x(2)    = Body-axis y inertial velocity, vb, m/s
%        x(3)    = Body-axis z inertial velocity, wb, m/s
%        x(4)    = North position of center of mass WRT Earth, xe, m
%        x(5)    = East position of center of mass WRT Earth, ye, m
%        x(6)    = Negative of c.m. altitude WRT Earth, ze = -h, m
%        x(7)    = Body-axis roll rate, pr, rad/s
%        x(8)    = Body-axis pitch rate, qr, rad/s
%        x(9)    = Body-axis yaw rate, rr,rad/s
%        x(10)   = Roll angle of body WRT Earth, phir, rad
%        x(11)   = Pitch angle of body WRT Earth, thetar, rad
%        x(12)   = Yaw angle of body WRT Earth, psir, rad
    
%    DEFINITION OF THE CONTROL VECTOR
%        u(1)    = Elevator, dEr, rad
%        u(2)    = Aileron, dAr, rad
%        u(3)    = Rudder, dRr, rad
%        u(4)    = Throttle, dT, %
%        u(5)    = Asymmetric Spoiler, dASr, rad
%        u(6)    = Flap, dFr, rad
%        u(7)    = Stabilator, dSr, rad

% BEGINNING of MAIN PROGRAM
% =========================

    disp('** FLIGHT **')
                    
    % FLIGHT Flags (1 = ON, 0 = OFF)
    MODEL   = 1;    % Aerodynamic model selection
                % 0: Incompressible flow, high angle of attack
                % 1: Compressible flow, low angle of attack
    TRIM    = 0;    % Trim flag (= 1 to calculate trim)
    LINEAR  = 0;    % Linear model flag (= 1 to calculate and store F and G)
    SIMUL   = 1;    % Flight path flag (= 1 for nonlinear simulation)
    GEAR    = 0;    % Landing gear DOWN (= 1) or UP (= 0)
    SPOIL   = 0;    % Symmetric Spoiler DEPLOYED (= 1) or CLOSED (= 0)
    CONHIS  = 1;    % Control history ON (= 1) or OFF (= 0)
    dF      = 0;    % Flap setting, deg
    
%    Altitude (ft), Indicated Airspeed (kt), Dynamic Pressure (N/m^2), and True Airspeed (m/s) for Trim Condition to be chosen by the User

    hft         =   31000;                      % Altitude above Sea Level, ft
    hm          =   hft * 0.3048;                % Altitude above Sea Level, m
    
    VKIAS       =   115;                         % Indicated Airspeed, kt
    VmsIAS      =   VKIAS * 0.5154;              % Indicated Airspeed, m/s
    
    [airDens,airPres,temp,soundSpeed] = Atmos(hm);
    
    qBarFixed   =   0.5*1.225*VmsIAS^2;          % Dynamic Pressure at sea level, N/m^2
    
    V           =   sqrt(2*qBarFixed/airDens);    % True Airspeed, TAS, m/s    (relative to air mass)
    TASms       =   V;


%    Alphabetical List of Initial Conditions

    alpha   =    0.0719*57.29578;    % Angle of attack, deg    (relative to air mass)
    beta    =    0;                  % Sideslip angle, deg    (relative to air mass)
    dA      =    0;                  % Aileron angle, deg
    dAS     =    0;                  % Asymmetric spoiler angle, deg
    dE      =    -10;                  % Elevator angle, deg
    dR      =    0;                  % Rudder angle, deg
    dS      =    -0.0342*57.29578;   % Stabilator setting, deg
    dT      =    0.8;             % Throttle setting, % / 100
    hdot    =    0;                  % Altitude rate, m/s [Inertial vertical flight path angle = 0 if hdot = 0]
    p       =    0;                  % Body-axis roll rate, deg/s
    phi     =    0;                  % Body roll angle wrt earth, deg
    psi     =    0;                  % Body yaw angle wrt earth, deg
    q       =    0;                  % Body-axis pitch rate, deg/sec
    r       =    0;                  % Body-axis yaw rate, deg/s
    SMI     =    0;                  % Static margin increment due to 
                                     % center-of-mass variation from reference, %/100
    tf      =    90;                 % Final time, sec
    ti      =    0;                  % Initial time, sec
    theta   =    alpha;              % Body pitch angle wrt earth, deg [theta = alpha if hdot = 0]
    xe      =    0;                  % Initial longitudinal position, m
    ye      =    0;                  % Initial lateral position, m
    ze      =    -hm;                % Initial vertical position, m [h is positive up, z is positive down]
    
    if MODEL == 0
        disp('Using model: Business Jet High-Alpha Aerodynamics')
    else
        disp('Using model: Business Jet High-Mach Aerodynamics')
    end
    

% Initial Conditions Depending on Prior Initial Conditions

    gamma   =    57.29578 * atan(hdot / sqrt(V^2 - hdot^2)); % Inertial Vertical Flight Path Angle, deg
    qbar    =    0.5 * airDens * V^2;                        % Dynamic Pressure, N/m^2
    IAS     =    sqrt(2 * qbar / 1.225);                     % Indicated Air Speed, m/s
    Mach    =    V / soundSpeed;                             % Mach Number
                                            
% Initial-Condition Perturbation (Test Inputs)

    delx    =  [0;0;0
                0;0;0
                0;0;0
                0;0;0];
                
    delu    =  [0;0;0;0;0;0;0];
    
% Control History Perturbation (Test Inputs) to be chosen by the User
% ===================================================================
% Each control effector represented by a column.
% Each row contains control increment delta-u(t) at time t.
% See section DEFINITION OF THE CONTROL VECTOR above to determine column meanings.

    ndeg    = 1;
    tuHis   = [0 4.99 5 10 10.01 100];
    deluHis = [0 0 0 0 0 0 0
               0 0 0 0 0 0 0
               0 0 0 0 0 0 0
               0 0 0 0 0 0 0
               0 0 0 0 0 0 0
               0 0 0 0 0 0 0];
    uInc    =    [];

% State Vector and Control Initialization
    phir    =    phi * .01745329;
    thetar  =    theta * .01745329;
    psir    =    psi * .01745329;

    windb    =    WindField(-ze,phir,thetar,psir);
    alphar   =    alpha * .01745329;
    betar    =    beta * .01745329;

    x    = [V * cos(alphar) * cos(betar) - windb(1)
            V * sin(betar) - windb(2)
            V * sin(alphar) * cos(betar) - windb(3)
            xe
            ye
            ze
            p * .01745329
            q * .01745329
            r * .01745329
            phir
            thetar
            psir];
    
    u    = [dE * .01745329
            dA * .01745329
            dR * .01745329
            dT
            dAS * .01745329
            dF * .01745329
            dS * .01745329];

% Trim Calculation (for Steady Level Flight at Initial V and h)
%    Optimization Vector (OptParam):
%        1 = Stabilator, rad
%        2 = Throttle, %
%        3 = Pitch Angle, rad

    if TRIM >= 1
        disp('Calculate TRIM Stabilator, Thrust, and Pitch Angle')
        OptParam = [];
        TrimHist = [];
        InitParam = [0.0369;0.1892;0.0986];
        if(is_octave)
            OptParam = fminsearch('TrimCost',InitParam);
        else
            [OptParam,J,ExitFlag,Output]  = fminsearch('TrimCost',InitParam);
        end

        % Optimizing Trim Error Cost with respect to dSr, dT, and Theta
        TrimHist;
        Index = [1:length(TrimHist)];
        TrimStabDeg = 57.295*OptParam(1);
        TrimThrusPer = 100*OptParam(2);
        TrimPitchDeg = 57.295*OptParam(3);
        TrimAlphaDeg = TrimPitchDeg - gamma;
        
        % Insert trim values in nominal control and state vectors
        disp('Incorporate trim values in control and state vectors')
        u    = [u(1)
                u(2)
                u(3)
                OptParam(2)
                u(5)
                u(6)
                OptParam(1)];
        format long            
        x    = [V * cos(OptParam(3))
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
        format short
    
        figure
        subplot(1,2,1)
        plot(Index,TrimHist(1,:),Index,TrimHist(2,:),Index,TrimHist(3,:)), legend('Stabilator', 'Thrust', 'Pitch Angle')
        xlabel('Iterations'), ylabel('Stabilator(blue), Thrust(green), Pitch Angle(red)'), grid
        title('Trim Parameters')
        subplot(1,2,2)
        semilogy(Index,TrimHist(4,:))
        xlabel('Iterations'), ylabel('Trim Cost'), grid
        title('Trim Cost')
    end
        
% Stability-and-Control Derivative Calculation
% TODO: BROKEN IN OCTAVE

    if LINEAR >= 1
        if is_octave
            disp('WARN: numjac not implemented in Octave. Please use Matlab or disable LINEAR calculation.')
        else
            disp('Generate and Save LINEAR MODEL')
            thresh    =    [.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1;.1];
            xj        =    [x;u];
            xdotj        =    LinModel(ti,xj);
            [dFdX,fac]    =    numjac('LinModel',ti,xj,xdotj,thresh,[],0);
            Fmodel        =    dFdX(1:12,1:12)
            Gmodel        =    dFdX(1:12,13:19)
            save ('Fmodel','Fmodel')
            save ('Gmodel','Gmodel')
        end
    end

% Flight Path Calculation

    if SIMUL >= 1
        disp('Performing simulation by solving differential equations')
        xo  = x + delx;
        u   = u + delu;
        t   = [];
        %x   = [];
        if is_octave
            t   = linspace(ti,tf,100);
            x   = lsode('EoM',xo,t);
        else
            tspan = [ti, tf];
            [t,x] = ode15s('EoM',tspan,xo);
        end
        kHis    =    length(t);
        
        disp('Writing results to plots')

        % Plot Control History
        figure
        subplot(2,2,1)
        plot(tuHis, 57.29578*deluHis(:,1), tuHis, 57.29578*deluHis(:,7))    
        xlabel('Time, s'), ylabel('Elevator (blue), Stabilator (green), deg'), grid
        title('Pitch Test Inputs')
        subplot(2,2,2)
        plot(tuHis, 57.29578*deluHis(:,2), tuHis, 57.29578*deluHis(:,3), tuHis, 57.29578*deluHis(:,5))    
        xlabel('Time, s'), ylabel('Aileron (blue), Rudder (green), Asymmetric Spoiler (red), deg'), grid
        title('Lateral-Directional Test Inputs')
        subplot(2,2,3)
        plot(tuHis, deluHis(:,4))    
        xlabel('Time, s'), ylabel('Thrust, %'), grid
        title('Thrust Test Inputs')
        subplot(2,2,4)
        plot(tuHis, 57.29578*deluHis(:,6))    
        xlabel('Time, s'), ylabel('Flap, deg'), grid
        title('Flap Test Inputs')
        
        % Plot State History
        figure
        subplot(2,2,1)
        plot(t,x(:,1))
        xlabel('Time, s'), ylabel('Axial Velocity (u), m/s'), grid
        title('Body-Axis Component of Inertial Velocity')
        subplot(2,2,2)
        plot(t,x(:,2))
        xlabel('Time, s'), ylabel('Side Velocity (v), m/s'), grid
        title('Body-Axis Component of Inertial Velocity')
        subplot(2,2,3)
        plot(t,x(:,3))
        xlabel('Time, s'), ylabel('Normal Velocity (w), m/s'), grid
        title('Body-Axis Component of Inertial Velocity')
        subplot(2,2,4)
        plot(t,x(:,1),t,x(:,2),t,x(:,3))
        xlabel('Time, s'), ylabel('u (blue), v (green), w (red), m/s'), grid
        title('Body-Axis Component of Inertial Velocity')
        
        figure
        subplot(2,2,1)
        plot(t,x(:,4))
        xlabel('Time, s'), ylabel('North, m'), grid
        title('Earth-Relative Aircraft Location')
        
        subplot(2,2,2)
        plot(t,x(:,5))
        xlabel('Time, s'), ylabel('East, m'), grid
        title('Earth-Relative Aircraft Location')
        
        subplot(2,2,3)
        plot(x(:,5),x(:,4))
        xlabel('East, m'), ylabel('North, m'), grid
        title('Earth-Relative Aircraft Location')
        
        subplot(2,2,4)
        plot((sqrt(x(:,4).*x(:,4) + x(:,5).*x(:,5))),-x(:,6))
        xlabel('Range, m'), ylabel('Altitude, m'), grid
        title('Earth-Relative Aircraft Location')
        
        figure
        subplot(2,2,1)
        plot(t,x(:,7) * 57.29578)
        xlabel('Time, s'), ylabel('Roll Rate (p), deg/s'), grid
        title('Body-Axis Component of Inertial Rate')
        subplot(2,2,2)
        plot(t,x(:,8) * 57.29578)
        xlabel('Time, s'), ylabel('Pitch Rate (q), deg/s'), grid
        title('Body-Axis Component of Inertial Rate')
        subplot(2,2,3)
        plot(t,x(:,9) * 57.29578)
        xlabel('Time, s'), ylabel('Yaw Rate (r), deg/s'), grid
        title('Body-Axis Component of Inertial Rate')
        subplot(2,2,4)
        plot(t,x(:,7) * 57.29578,t,x(:,8) * 57.29578,t,x(:,9) * 57.29578)
        xlabel('Time, s'), ylabel('p (blue), q (green), r (red), deg/s'), grid
        title('Body-Axis Component of Inertial Rate')
        
        figure
        subplot(2,2,1)
        plot(t,x(:,10) * 57.29578)
        xlabel('Time, s'), ylabel('Roll Angle (phi), deg'), grid
        title('Earth-Relative Aircraft Attitude')
        subplot(2,2,2)
        plot(t,x(:,11) * 57.29578)
        xlabel('Time, s'), ylabel('Pitch Angle (theta), deg'), grid
        title('Earth-Relative Aircraft Attitude')
        subplot(2,2,3)
        plot(t,x(:,12) * 57.29578)
        xlabel('Time, s'), ylabel('Yaw Angle (psi, deg'), grid
        title('Earth-Relative Aircraft Attitude')
        subplot(2,2,4)
        plot(t,x(:,10) * 57.29578,t,x(:,11) * 57.29578,t,x(:,12) * 57.29578)
        xlabel('Time, s'), ylabel('phi (blue), theta (green), psi (red), deg'), grid
        title('Earth-Relative Aircraft Attitude')
        
        VAirRel         =   [];
        vEarth          =   [];
        AlphaAR         =   [];
        BetaAR          =   [];
        windBody        =   [];
        airDensHis      =   [];
        soundSpeedHis   =   [];
        qbarHis         =   [];
        GammaHis        =   [];
        XiHis           =   [];
        
        for i = 1:kHis
            windb           =   WindField(-x(i,6),x(i,10),x(i,11),x(i,12));
            windBody        =   [windBody windb];
            [airDens,airPres,temp,soundSpeed] = Atmos(-x(i,6));
            airDensHis      =   [airDensHis airDens];
            soundSpeedHis   =   [soundSpeedHis soundSpeed];
        end
        
        vBody           =   [x(:,1) x(:,2) x(:,3)]';
        vBodyAir        =   vBody + windBody;

        for i = 1:kHis
            vE          =   DCM(x(i,10),x(i,11),x(i,12))' * [vBody(1,i);vBody(2,i);vBody(3,i)];
            VER         =   sqrt(vE(1)^2 + vE(2)^2 + vE(3)^2);
            VAR         =   sqrt(vBodyAir(1,i)^2 + vBodyAir(2,i)^2 + vBodyAir(3,i)^2);
            Alphar      =   atan(vBodyAir(3,i) / vBodyAir(1,i));
            AlphaAR     =   [AlphaAR Alphar];
            Betar       =   asin(vBodyAir(2,i) / VAR);
            BetaAR      =   [BetaAR Betar];
            vEarth      =   [vEarth vE];
            Gammar      =   asin(-vEarth(3,i) / VER);
            GammaHis    =   [GammaHis Gammar];
            Xir         =   asin(vEarth(2,i) / sqrt((vEarth(1,i))^2 + (vEarth(2,i))^2));
            XiHis       =   [XiHis Xir];
            VAirRel     =   [VAirRel VAR];
        end

        MachHis         =   VAirRel ./ soundSpeedHis;
        AlphaDegHis     =   57.29578 * AlphaAR;
        BetaDegHis      =   57.29578 * BetaAR;
        qbarHis         =   0.5 * airDensHis .* VAirRel.*VAirRel;
        GammaDegHis     =   57.29578 * GammaHis;
        XiDegHis        =   57.29578 * XiHis;
        
        figure
        subplot(3,1,1)
        plot(t, VAirRel')    
        xlabel('Time, s'), ylabel('Air-relative Speed, m/s'), grid
        title('True AirSpeed')
        subplot(3,1,2)
        plot(t, MachHis')    
        xlabel('Time, s'), ylabel('M'), grid
        title('Mach Number')
        subplot(3,1,3)
        plot(t, qbarHis')    
        xlabel('Time, s'), ylabel('qbar, N/m^2'), grid
        title('Dynamic Pressure')
        
        figure
        subplot(2,1,1)
        plot(t, AlphaDegHis', t, BetaDegHis')    
        xlabel('Time, s'), ylabel('Angle of Attack, deg (blue), Sideslip Angle, deg (green)'), grid
        title('Aerodynamic Angles')
        subplot(2,1,2)
        plot(t, GammaDegHis', t, XiDegHis')    
        xlabel('Time, s'), ylabel('Vertical, deg (blue), Horizontal, deg (green)'), grid
        title('Flight Path Angles')
        
        disp('End of FLIGHT Simulation')
    end