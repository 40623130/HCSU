clear,clear all,clc,clf;
%f(0.2L) = 355,f(0.02L) = 255
L = 1000;
Bdist = 0.2*L ; Adist = 0.02*L;
Bsp = 255; Asp = 355;
x = [0:1:Bdist];
C = ((Asp-Bsp)/(Bdist-Adist))*x + (Bsp-Adist*((Asp-Bsp)/(Bdist-Adist)));
plot(C),grid;

%200a+b = 355
%20a+b = 255s
%a=100/180 
%b=255-(100/180)*20