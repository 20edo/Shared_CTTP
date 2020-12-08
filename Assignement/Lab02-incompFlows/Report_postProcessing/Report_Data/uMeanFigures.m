clear 
close all
clc

%% uMeanPimple

data = load('pimple_U-y100_100.csv');

x = data(:,25);
Uy = data(:,3);
Umean = data(:,6);
var = data(:,9);

figure()
hold on, grid on
plot(x,Uy)
plot(x,Umean)
plot(x,var)
xlabel('x $[m]$','Interpreter','Latex')
ylabel('Velocities $[m/s]$','Interpreter','Latex')
legend('Uy','Uy,mean','var','Location','SouthEast')
xlim([-0.12 0.12])

%% uMeanPiso

data = load('piso_U-y100_100.csv');

x_P = data(:,25);
Uy_P = data(:,3);
Umean_P = data(:,6);
var_P = data(:,9);

figure()
hold on, grid on
plot(x_P,Uy_P)
plot(x_P,Umean_P)
plot(x_P,var_P)
xlabel('x $[m]$','Interpreter','Latex')
ylabel('Velocities $[m/s]$','Interpreter','Latex')
legend('Uy','Uy,mean','var','Location','SouthEast')
xlim([-0.12 0.12])

%% uMeanSimple

data = load('simple_U-y100_2000.csv');

x_S = data(:,12);
Uy_S = data(:,3);
var_S = data(:,9);

figure()
hold on, grid on
plot(x_S,Uy_S)
plot(x_S,var_S)
xlabel('x $[m]$','Interpreter','Latex')
ylabel('Velocities $[m/s]$','Interpreter','Latex')
legend('Uy','var','Location','SouthEast')
xlim([-0.12 0.12])