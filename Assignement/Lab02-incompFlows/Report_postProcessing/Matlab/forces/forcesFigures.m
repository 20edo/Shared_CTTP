clear 
close all
clc

%% pimpleDrag

data = load('forcesPimple.txt');

t = data(:,1);
drag = data(:,3);

figure()
plot(t,drag)
xlabel('Time $[s]$','Interpreter','Latex')
ylabel('Drag $[N]$','Interpreter','Latex')

%% pisoDrag

data = load('forcesPiso.txt');

t_P = data(:,1);
drag_P = data(:,3);

figure()
plot(t_P,drag_P)
xlabel('Time $[s]$','Interpreter','Latex')
ylabel('Drag $[N]$','Interpreter','Latex')

%% simpleDrag

data = load('forcesSimple.txt');

t_S = data(:,1);
drag_S = data(:,3);

figure()
plot(t_S,drag_S)
xlabel('Time $[s]$','Interpreter','Latex')
ylabel('Drag $[N]$','Interpreter','Latex')