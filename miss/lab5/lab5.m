clc
clear
close all

out=sim('lab5')
phi=out.th;
L = str2num(get_param('lab5/Subsystem,','l'));
m = str2num(get_param('lab5/Subsystem,','m'));
l = 0.01;

for i = 1:length(phi)
    p = line([0 -l*sin(phi(i))],[0 -l*cos(phi(i))],'Color','r','LineWidth',2);
    hold on
    s = plot(-l*sin(phi(i)), -l*cos(phi(i)), 'b.','MarkerSize',5*m);
    hold off
    
    daspect([1,1,1])
    axis([-1.1*l 1.1*l -1.1*l 1.1*l])
end