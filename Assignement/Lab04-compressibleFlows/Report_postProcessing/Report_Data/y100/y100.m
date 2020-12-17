clear
close all
clc

%% combustor2D_RPF

data = load('RPF.txt');

x = data(:,29);
T = data(:,1);
Ux = data(:,4);
Uy = data(:,5);
rho = data(:,25);
p = data(:,22);

% plot
figure()
hold on, grid on
plot(x,Ux)
plot(x,Uy)
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
ylabel('flow velocity $[m/s]$','Interpreter','Latex')
legend('Ux','Uy','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,rho)
ylabel('density $[kg/m^3]$','Interpreter','Latex')
legend('T','rho','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,p)
ylabel('pressure $[N/m^2]$','Interpreter','Latex')
legend('T','pressure','Location','Best','Interpreter','Latex')

%% combustor2D_highRe

data = load('RPF-highRe.txt');

x = data(:,30);
T = data(:,2);
Ux = data(:,5);
Uy = data(:,6);
rho = data(:,26);
p = data(:,23);

% plot
figure()
hold on, grid on
plot(x,Ux)
plot(x,Uy)
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
ylabel('flow velocity $[m/s]$','Interpreter','Latex')
legend('Ux','Uy','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,rho)
ylabel('density $[kg/m^3]$','Interpreter','Latex')
legend('T','rho','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,p)
ylabel('pressure $[N/m^2]$','Interpreter','Latex')
legend('T','pressure','Location','Best','Interpreter','Latex')

%% combustor2D_highRe_highT

data = load('RPF-highRe-highT.txt');

x = data(:,31);
T = data(:,2);
Ux = data(:,5);
Uy = data(:,6);
rho = data(:,26);
p = data(:,23);

% plot
figure()
hold on, grid on
plot(x,Ux)
plot(x,Uy)
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
ylabel('flow velocity $[m/s]$','Interpreter','Latex')
legend('Ux','Uy','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,rho)
ylabel('density $[kg/m^3]$','Interpreter','Latex')
legend('T','rho','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,p)
ylabel('pressure $[N/m^2]$','Interpreter','Latex')
legend('T','pressure','Location','Best','Interpreter','Latex')

%% combustor2D_RPF_lowRe_highT

data = load('RPF-lowRe-highT.txt');

x = data(:,31);
T = data(:,2);
Ux = data(:,5);
Uy = data(:,6);
rho = data(:,26);
p = data(:,23);

% plot
figure()
hold on, grid on
plot(x,Ux)
plot(x,Uy)
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
ylabel('flow velocity $[m/s]$','Interpreter','Latex')
legend('Ux','Uy','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,rho)
ylabel('density $[kg/m^3]$','Interpreter','Latex')
legend('T','rho','Location','Best','Interpreter','Latex')

figure()
hold on, grid on
xlim([-0.12 0.12])
xlabel('x $[m]$','Interpreter','Latex')
yyaxis left
plot(x,T)
ylabel('temperature $[K]$','Interpreter','Latex')
yyaxis right
plot(x,p)
ylabel('pressure $[N/m^2]$','Interpreter','Latex')
legend('T','pressure','Location','Best','Interpreter','Latex')