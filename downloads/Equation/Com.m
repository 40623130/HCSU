clear,clear all,clc;
L = 600;
Ddist = L; Cdist = 0.6*L; Bdist = 0.2*L ; Adist = 0.02*L;
Dsp = 200; Csp = 135; Bsp = 255; Asp = 355;
x = [0:1:L];
s = [0:1:1023];

%Mode_1  Range:L~0.6L  %f(L) = 355, f(0.2L) = 135, f(0.02L) = 200
a = ((Adist-Ddist)*(Csp-Asp)-(Bdist-Ddist)*(Dsp-Asp))/(((Adist-Ddist)*(Bdist-Ddist)*Bdist)-((Bdist-Ddist)*(Adist-Ddist)*Adist));
b = ((Adist-Ddist)*Adist*(Csp-Asp)-(Bdist-Ddist)*Bdist*(Dsp-Asp))/((Adist-Bdist)*(Bdist-Ddist)*(Adist-Ddist));
A = (a*x+b).*(x-Ddist)+Asp;
figure(1);plot(A),grid;

%Mode_2  Range:0.6~0.2L  %f(0.6L) = 355, f(0.2L) = 135, f(0.02L) = 255
c = ((Adist-Cdist)*(Csp-Asp)-(Bdist-Cdist)*(Bsp-Asp))/(((Adist-Cdist)*(Bdist-Cdist)*Bdist)-((Bdist-Cdist)*(Adist-Cdist)*Adist));
d = ((Adist-Cdist)*Adist*(Csp-Asp)-(Bdist-Cdist)*Bdist*(Bsp-Asp))/((Adist-Bdist)*(Bdist-Cdist)*(Adist-Cdist));
B = (c*x+d).*(x-Cdist)+Asp;
figure(2);plot(B),grid;

%Mode_3  Range:0.2~0.02L  %f(0.2L) = 355,f(0.02L) = 255
C = ((Asp-Bsp)/(Bdist-Adist))*x + (Bsp-Adist*((Asp-Bsp)/(Bdist-Adist)));
figure(3);plot(C),grid;

%Handle
HA = [-133114800 -251160;-124090824 -251196];
HB = [200;200];
HC = GaussNaive(HA,HB);
D = (HC(1).*s + HC(2)).*(s-1013).*(s-10) + 125 ;
DD = 100000*(1./D);
figure(4);plot(DD),grid;
%{
Explain:
Mode_1  Range:L~0.6L & Mode_2  Range:0.6~0.2L
將解聯立的數值全轉成參數，兩種模式的解法一樣
f(200) = (200*a+b)*(-400) = 135-355
(Bdist*a+b)*(Bdist-Cdist) = Csp-Asp
(Bdist-Cdist)*Bdist*a+(Bdist-Cdist)*b = Csp-Asp

(Adist-Cdist)*(Bdist-Cdist)*Bdist*a+(Adist-Cdist)*(Bdist-Cdist)*b = (Adist-Cdist)*(Csp-Asp)
(Bdist-Adist)*(Bdist-Cdist)*(Adist-Cdist)*a = (Adist-Cdist)*(Csp-Asp)-(Bdist-Cdist)*(Bsp-Asp)%
a = ((Adist-Cdist)*(Csp-Asp)-(Bdist-Cdist)*(Bsp-Asp))/(((Adist-Cdist)*(Bdist-Cdist)*Bdist)-((Bdist-Cdist)*(Adist-Cdist)*Adist))

(Adist-Cdist)*Adist*(Bdist-Cdist)*Bdist*a+ (Adist-Cdist)*Adist*(Bdist-Cdist)*b = (Adist-Cdist)*Adist*(Csp-Asp)
(Adist-Bdist)*(Bdist-Cdist)*(Adist-Cdist)*b = (Adist-Cdist)*Adist*(Csp-Asp)-(Bdist-Cdist)*Bdist*(Bsp-Asp)%
b = ((Adist-Cdist)*Adist*(Csp-Asp)-(Bdist-Cdist)*Bdist*(Bsp-Asp))/((Adist-Bdist)*(Bdist-Cdist)*(Adist-Cdist))

f(20) = (20*a+b)*(-580) = 255-355
(Adist*a+b)*(Adist-Cdist) = Bsp-Asp
(Adist-Cdist)*Adist*a+(Adist-Cdist)*b = Bsp-Asp

(Bdist-Cdist)*(Adist-Cdist)*Adist*a+(Bdist-Cdist)*(Adist-Cdist)*b = (Bdist-Cdist)*(Bsp-Asp)

(Bdist-Cdist)*Bdist*(Adist-Cdist)*Adist*a+ (Bdist-Cdist)*Bdist*(Adist-Cdist)*b = (Bdist-Cdist)*Bdist*(Bsp-Asp)
--------
Mode_3  Range:0.2~0.02L
簡單的聯立方成就能解，並替換成參數
200a+b = 355
20a+b = 255s
a=100/180 
b=255-(100/180)*20
--------
Handle
f(1013) = f(10) = 125,f(530) = f(494) = 325
f(x) = (ax+b)*(x-1013)*(x-10) + 125 整理之後
利用GaussNaive找矩陣HA & HB的解HC並帶回原方程式即可
%}

