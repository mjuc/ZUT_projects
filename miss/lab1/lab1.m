clc
close all
clear

f1 = @(x) sin(x)+cos(x);
f2 = @(x) exp(x)+log(x);
f3 = @(x,y) sin(x)*cos(y);

x=linspace(0.1,4);

figure()
hold on
plot(x,f1(x))
plot(x,f2(x))
legend(["sin(x) + cos(x)","e^x + log(x)"])

[X,Y] = meshgrid(-2*pi:0.001:2*pi,-2*pi:0.001:2*pi);

surf(X,Y,f3(X,Y))

x = rand(1,7) * 3 +2;
y = rand(1,7) * 4 +3;
l1(x,y)