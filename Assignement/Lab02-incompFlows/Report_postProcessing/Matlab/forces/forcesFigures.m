clear 
close all
clc

%% pimpleDrag

data = load('forcesPimple.txt');

t = data(:,1);
drag_pres = data(:,3);
drag_tot = data(:,3)+data(:,6);

figure()
hold on
plot(t,drag_pres)
plot(t,drag_tot)
xlabel('Time $[s]$','Interpreter','Latex')
ylabel('Drag $[N]$','Interpreter','Latex')
legend('Drag','Total Force','Location','SouthEast','Interpreter','Latex')

%% pisoDrag

data = load('forcesPiso.txt');

t_P = data(:,1);
drag_pres_P = data(:,3);
drag_tot_P = data(:,3)+data(:,6);

figure()
hold on
plot(t_P,drag_pres_P)
plot(t_P,drag_tot_P)
xlabel('Time $[s]$','Interpreter','Latex')
ylabel('Drag $[N]$','Interpreter','Latex')
legend('Drag','Total Force','Location','SouthEast','Interpreter','Latex')
ylim([-0.04 0.04])

%% simpleDrag

data = load('forcesSimple.txt');

t_S = data(:,1);
drag_pres_S = data(:,3);
drag_tot_S = data(:,3)+data(:,6);

figure()
hold on
plot(t_S,drag_pres_S)
plot(t_S,drag_tot_S)
xlabel('Iteration Number $[-]$','Interpreter','Latex')
ylabel('Drag $[N]$','Interpreter','Latex')
legend('Drag','Total Force','Location','SouthEast','Interpreter','Latex')