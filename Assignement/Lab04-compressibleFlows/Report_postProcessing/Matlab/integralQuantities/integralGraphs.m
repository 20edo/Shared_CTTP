clear
close all
clc

%% combustor2D_RPF

pInlet = load('pInlet.txt');
pOutlet = load('pOutlet.txt');
TOutlet = load('TOutlet.txt');
TWalls = load('TouterWalls.txt');

t = pInlet(:,1);
pInlet = pInlet(:,2);
pOutlet = pOutlet(:,2);
TOutlet = TOutlet(:,2);
TWalls = TWalls(:,2);

% plot
figure()
hold on
yyaxis left
plot(t,pOutlet-pInlet)
ylabel('pressure drop $[Pa]$','Interpreter','Latex')
yyaxis right
plot(t,TOutlet,t,TWalls,'m-')
xlabel('time $[s]$','Interpreter','Latex')
ylabel('temperatures $[K]$','Interpreter','Latex')
legend('Pressure drop','$T_{avg,outlet}$','max $T_{walls}$','Location','Best','Interpreter','Latex')

%% combustor2D_highRe

pInlet_hl = load('pInlet_highRe.txt');
pOutlet_hl = load('pOutlet_highRe.txt');
TOutlet_hl = load('TOutlet_highRe.txt');
TWalls_hl = load('TouterWalls_highRe.txt');

t_hl = pInlet_hl(:,1);
pInlet_hl = pInlet_hl(:,2);
pOutlet_hl = pOutlet_hl(:,2);
TOutlet_hl = TOutlet_hl(:,2);
TWalls_hl = TWalls_hl(:,2);

% plot
figure()
hold on
yyaxis left
plot(t_hl,pOutlet_hl-pInlet_hl)
ylabel('pressure drop $[Pa]$','Interpreter','Latex')
yyaxis right
plot(t_hl,TOutlet_hl,t_hl,TWalls_hl,'m-')
xlabel('time $[s]$','Interpreter','Latex')
ylabel('temperatures $[K]$','Interpreter','Latex')
legend('Pressure drop','$T_{avg,outlet}$','max $T_{walls}$','Location','Best','Interpreter','Latex')

%% combustor2D_highRe_highT

pInlet_hh = load('pInlet_highRehighT.txt');
pOutlet_hh = load('pOutlet_highRehighT.txt');
TOutlet_hh = load('TOutlet_highRehighT.txt');
heatFlux_hh = load('heatFlux_highRehighT.txt');

t_hh = pInlet_hh(:,1);
pInlet_hh = pInlet_hh(:,2);
pOutlet_hh = pOutlet_hh(:,2);
TOutlet_hh = TOutlet_hh(:,2);
heatFlux_hh = heatFlux_hh(:,2);

% plot
figure()
plot(t_hh,pOutlet_hh-pInlet_hh)
ylabel('pressure drop $[Pa]$','Interpreter','Latex')
xlabel('time $[s]$','Interpreter','Latex')
legend('Pressure drop','Location','Best','Interpreter','Latex')

figure()
hold on
yyaxis left
plot(t_hh,TOutlet_hh)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(t_hh,heatFlux_hh)
xlabel('time $[s]$','Interpreter','Latex')
ylabel('heat flux $[W/m^2]$','Interpreter','Latex')
legend('$T_{avg,outlet}$','$\dot{q}_{avg,walls}$','Location','Best','Interpreter','Latex')

%% combustor2D_RPF_lowRe_highT

pInlet_lh = load('pInlet_lowRehighT.txt');
pOutlet_lh = load('pOutlet_lowRehighT.txt');
TOutlet_lh = load('TOutlet_lowRehighT.txt');
heatFlux_lh = load('heatFlux_lowRehighT.txt');

t_lh = pInlet_lh(:,1);
pInlet_lh = pInlet_lh(:,2);
pOutlet_lh = pOutlet_lh(:,2);
TOutlet_lh = TOutlet_lh(:,2);
heatFlux_lh = heatFlux_lh(:,2);

% plot
figure()
plot(t_lh,pOutlet_lh-pInlet_lh)
ylabel('pressure drop $[Pa]$','Interpreter','Latex')
xlabel('time $[s]$','Interpreter','Latex')
legend('Pressure drop','Location','Best','Interpreter','Latex')

figure()
hold on
yyaxis left
plot(t_lh,TOutlet_lh)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(t_lh,heatFlux_lh)
xlabel('time $[s]$','Interpreter','Latex')
ylabel('heat flux $[W/m^2]$','Interpreter','Latex')
legend('$T_{outlet}$','$\dot{q}_{avg,walls}$','Location','Best','Interpreter','Latex')