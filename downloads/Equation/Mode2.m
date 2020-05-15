clear,clear all,clc;
%f(0.6L) = 355, f(0.2L) = 135, f(0.02L) = 255
L = 1000;
Cdist = 0.6*L; Bdist = 0.2*L ; Adist = 0.02*L;
Csp = 135; Bsp = 255; Asp = 355; 
x = [0:1:0.6*L];
a = ((Adist-Cdist)*(Csp-Asp)-(Bdist-Cdist)*(Bsp-Asp))/(((Adist-Cdist)*(Bdist-Cdist)*Bdist)-((Bdist-Cdist)*(Adist-Cdist)*Adist));
b = ((Adist-Cdist)*Adist*(Csp-Asp)-(Bdist-Cdist)*Bdist*(Bsp-Asp))/((Adist-Bdist)*(Bdist-Cdist)*(Adist-Cdist));
B = (a*x+b).*(x-Cdist)+Asp;
plot(B),grid;
%將解聯立的數值全轉成參數
%f(200) = (200*a+b)*(-400) = 135-355
%(Bdist*a+b)*(Bdist-Cdist) = Csp-Asp
%%(Bdist-Cdist)*Bdist*a+(Bdist-Cdist)*b = Csp-Asp
%
%(Adist-Cdist)*(Bdist-Cdist)*Bdist*a+(Adist-Cdist)*(Bdist-Cdist)*b = (Adist-Cdist)*(Csp-Asp)
%(Bdist-Adist)*(Bdist-Cdist)*(Adist-Cdist)*a = (Adist-Cdist)*(Csp-Asp)-(Bdist-Cdist)*(Bsp-Asp)%
%a = ((Adist-Cdist)*(Csp-Asp)-(Bdist-Cdist)*(Bsp-Asp))/(((Adist-Cdist)*(Bdist-Cdist)*Bdist)-((Bdist-Cdist)*(Adist-Cdist)*Adist))
%
%(Adist-Cdist)*Adist*(Bdist-Cdist)*Bdist*a+ (Adist-Cdist)*Adist*(Bdist-Cdist)*b = (Adist-Cdist)*Adist*(Csp-Asp)
%(Adist-Bdist)*(Bdist-Cdist)*(Adist-Cdist)*b = (Adist-Cdist)*Adist*(Csp-Asp)-(Bdist-Cdist)*Bdist*(Bsp-Asp)%
%b = ((Adist-Cdist)*Adist*(Csp-Asp)-(Bdist-Cdist)*Bdist*(Bsp-Asp))/((Adist-Bdist)*(Bdist-Cdist)*(Adist-Cdist))
%
%f(20) = (20*a+b)*(-580) = 255-355
%(Adist*a+b)*(Adist-Cdist) = Bsp-Asp
%%(Adist-Cdist)*Adist*a+(Adist-Cdist)*b = Bsp-Asp
%
%(Bdist-Cdist)*(Adist-Cdist)*Adist*a+(Bdist-Cdist)*(Adist-Cdist)*b = (Bdist-Cdist)*(Bsp-Asp)
%
%(Bdist-Cdist)*Bdist*(Adist-Cdist)*Adist*a+ (Bdist-Cdist)*Bdist*(Adist-Cdist)*b = (Bdist-Cdist)*Bdist*(Bsp-Asp)