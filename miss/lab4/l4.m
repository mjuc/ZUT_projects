clc
close all
clear all

out=sim('lab4');
x=out.x;
y=out.y;

Rs = str2num(get_param('lab4/Subsystem', 'Rs'));
R = str2num(get_param('lab4/Subsystem', 'R'));

for i=1:length(x)
    plot(x(1:i),y(1:i))
    axis([-8 8 -8 8])
    daspect([1 1 1])
    hold on
    rectangle('Position',[x(i)-Rs,y(i)-Rs,2*Rs,2*Rs],'Curvature',[1 1])
    rectangle('Position',[-R,-R,2*R,2*R],'Curvature',[1 1]);
    hold off
    pause(2^-7)
end