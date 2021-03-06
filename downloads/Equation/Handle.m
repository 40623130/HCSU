clear,clear all,clc;
%f(1013) = f(10) = 125,f(530) = f(494) = 325
%f(x) = (ax+b)*(x-1013)*(x-10) + 125
HA = [-133114800 -251160;-124090824 -251196];
HB = [200;200];
HC = GaussNaive(HA,HB);
s = [0:1:1023];
D = (HC(1).*s + HC(2)).*(s-1013).*(s-10) + 125 ;
%[-3.170055033245540e-09;-7.946250149636110e-04]125:325
F = 100000*(1./D);
plot(F),grid
