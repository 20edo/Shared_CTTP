clear 
close all
clc

%% pInletPimple

data = load('pInletPimple.txt');

t = data(:,1);
pInletAvg = data(:,2);

figure()
plot(t,pInletAvg)
xlabel('time $[s]$','Interpreter','Latex')
ylabel('Average Inlet Pressure $[m^2/s^2]$','Interpreter','Latex')

%% pInletPiso

data = load('pInletPiso.txt');

t_P = data(:,1);
pInletAvg_P = data(:,2);

figure()
plot(t_P,pInletAvg_P)
xlabel('time $[s]$','Interpreter','Latex')
ylabel('Average Inlet Pressure $[m^2/s^2]$','Interpreter','Latex')
ylim([-50 150])

%% pInletSimple

data = load('pInletSimple.txt');

t_S = data(:,1);
pInletAvg_S = data(:,2);

figure()
plot(t_S,pInletAvg_S)
xlabel('time $[s]$','Interpreter','Latex')
ylabel('Average Inlet Pressure $[m^2/s^2]$','Interpreter','Latex')