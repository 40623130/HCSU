clear,clear all,clc;
%f(L) = 355, f(0.2L) = 135, f(0.02L) = 200
L = 1000;
Ddist = L; Bdist = 0.2*L ; Adist = 0.02*L;
Csp = 135; Dsp = 200; Asp = 355; 
x = [0:1:L];
a = ((Adist-Ddist)*(Csp-Asp)-(Bdist-Ddist)*(Dsp-Asp))/(((Adist-Ddist)*(Bdist-Ddist)*Bdist)-((Bdist-Ddist)*(Adist-Ddist)*Adist));
b = ((Adist-Ddist)*Adist*(Csp-Asp)-(Bdist-Ddist)*Bdist*(Dsp-Asp))/((Adist-Bdist)*(Bdist-Ddist)*(Adist-Ddist));
A = (a*x+b).*(x-Ddist)+Asp;
plot(A),grid;
