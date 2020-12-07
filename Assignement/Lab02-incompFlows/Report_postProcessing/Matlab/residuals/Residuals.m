clear
close all
clc 

%% residualsPimple

res = load('residualsPimple.txt');

t = res(:,1);
p = res(:,2);
Ux = res(:,3);
Uy = res(:,4);
k = res(:,5);
eps = res(:,6);

%% plot residualsPimple

figure()
semilogy(t,p,t,Ux,t,Uy,t,k,t,eps)

legend('p','Ux','Uy','k','eps','Location','SouthEast','Interpreter','Latex')
xlabel('time $[s]$','Interpreter','Latex')
ylabel('residuals $[-]$','Interpreter','Latex')

%% residualsPiso

res_P = load('residualsPiso.txt');

t_P = res_P(:,1);
p_P = res_P(:,2);
Ux_P = res_P(:,3);
Uy_P = res_P(:,4);
k_P = res_P(:,5);
eps_P = res_P(:,6);

%% plot residualsPiso

figure()
semilogy(t_P,p_P,t_P,Ux_P,t_P,Uy_P,t_P,k_P,t_P,eps_P)

legend('p','Ux','Uy','k','eps','Location','SouthEast','Interpreter','Latex')
xlabel('time $[s]$','Interpreter','Latex')
ylabel('residuals $[-]$','Interpreter','Latex')

%% residualsSimple

res_S = load('residualsSimple.txt');

t_S = res_S(:,1);
p_S = res_S(:,2);
Ux_S = res_S(:,3);
Uy_S = res_S(:,4);
k_S = res_S(:,5);
eps_S = res_S(:,6);

%% plot residualsSimple

figure()
semilogy(t_S,p_S,t_S,Ux_S,t_S,Uy_S,t_S,k_S,t_S,eps_S)

legend('p','Ux','Uy','k','eps','Location','NorthEast','Interpreter','Latex')
xlabel('iteration number $[-]$','Interpreter','Latex')
ylabel('residuals $[-]$','Interpreter','Latex')