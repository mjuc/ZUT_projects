X=[-3,-2.5,-2,-1.5,-1.0,-0.5,0,0.5,1,1.5,2,2.5,3];
Y=[-0.19,-0.05,0.6,1,0.4,-0.22,0,0.22,-0.4,-0.98,-0.6,-0.1,0.19];
x=-3:0.01:3;
%zadanie 1
% wartoœci: -0.19,-0.05,0.6,1,0.4,-0.22,0,0.22,-0.4,-0.98,-0.6,-0.1,0.19

%zadanie 2
xq=0.25;

r0=interp1(X,Y,0.25);
r1=interp1(X,Y,0.25,'nearest');
r2=interp1(X,Y,0.25,'linear');
r3=interp1(X,Y,0.25,'spline');
r4=interp1(X,Y,0.25,'cubic');


% wyniki 0.22 0.11 0.1888 0.1375 0.11

%zadanie 3
%figure
rs1=interp1(X,Y,x,'nearest');
%plot(X,Y,'o',x,rs1,':.');
%xlim([-3 3]);
%title('nearest');

%figure
rs2=interp1(X,Y,x,'linear');
%plot(X,Y,'o',x,rs2,':.');
%xlim([-3 3]);
%title('linear');

%figure
rs3=interp1(X,Y,x,'spline');
%plot(X,Y,'o',x,rs2,':.');
%xlim([-3 3]);
%title('spline');

%figure
rs4=interp1(X,Y,x,'cubic');
%plot(X,Y,'o',x,rs2,':.');
%xlim([-3 3]);
%title('cubic');

%cubic

%zadanie 4

p=polyfit(X,Y,12);
y=polyval(p,x);
%plot(X,Y,'o',x,y)

%12

res=polyval(p,xq);

%0.1957 wartoœæ minimalnie wiêksza ni¿ uzyskane w wyniku interpolacji