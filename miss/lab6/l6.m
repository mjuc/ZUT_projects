clc
clear
close all

out=sim('lab6.slx');

h1=out.h1;
h2=out.h2;

S1=str2num(get_param('lab6/Subsystem','S1'));
S2=str2num(get_param('lab6/Subsystem','S2'));
Swy1=str2num(get_param('lab6/Subsystem','Swy1'));
Swy2=str2num(get_param('lab6/Subsystem','Swy2'));

maxH1=max(h1+1);
maxH2=max(h2+1);

for i=1:length(h1)
    plot([0,0],[0,maxH1],'Color','green','LineWidth',4)
    hold on
    
    plot([S1,S1],[Swy1,maxH1],'Color','green','LineWidth',4)
    plot([S1,S1+0.5],[Swy1,Swy1],'Color','green','LineWidth',4)
    plot([S1+0.5,S1+0.5],[Swy1,maxH2],'Color','green','LineWidth',4)
    plot([S1+S2+0.5,S1+S2+0.5],[Swy2,maxH2],'Color','green','LineWidth',4)
    plot([S1+S2+0.5,S1+S2+0.5],[Swy2,Swy2],'Color','green','LineWidth',4)
    
    fill([0 S1 S1 0],[0 0 h1(i) h1(i)],[0.3 0.3 0.3],'EdgeColor','None')
    fill([S1 S1+0.5 S1+0.5 S1],[0 0 Swy1 Swy1],[0.3 0.3 0.3],'EdgeColor','None')
    fill([S1+S2+0.5 S1+0.5+S1+0.5 S1+S2+1 S1+0.5+S2],[0 0 Swy2 Swy2],[0.3 0.3 0.3],'EdgeColor','None')
    fill([S1+0.5 S1+S2+0.5 S1+0.5+S2 S1+0.5],[0 0 h2(i) h2(i)],[0.3 0.3 0.3],'EdgeColor','None')
    hold off
    
    axis([0 5 0 max(maxH1,maxH2)+1])
    
    set(gca,'DataAspectRatio',[1,1,1])
    pause(t)
end