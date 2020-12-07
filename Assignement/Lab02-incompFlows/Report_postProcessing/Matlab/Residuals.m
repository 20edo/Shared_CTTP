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
hold on, grid on
plot(t,log10(p))
plot(t,log10(Ux))
plot(t,log10(Uy))
plot(t,log10(k))
plot(t,log10(eps))

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
hold on, grid on
plot(t_P,log10(p_P))
plot(t_P,log10(Ux_P))
plot(t_P,log10(Uy_P))
plot(t_P,log10(k_P))
plot(t_P,log10(eps_P))

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
hold on, grid on
plot(t_S,log10(p_S))
plot(t_S,log10(Ux_S))
plot(t_S,log10(Uy_S))
plot(t_S,log10(k_S))
plot(t_S,log10(eps_S))

legend('p','Ux','Uy','k','eps','Location','NorthEast','Interpreter','Latex')
xlabel('iteration number $[-]$','Interpreter','Latex')
ylabel('residuals $[-]$','Interpreter','Latex')