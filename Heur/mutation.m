function [newpop2]=mutation(newpop1,pm) %pm±äÒìÂÊ
% ±äÒì µ¥µã0-1±äÒì
%Name: mutation.m

[popsize,individual]=size(newpop1);

for i=1:popsize
    ps=rand;
    
    if ps<pm %±äÒì
        mpoint=round(rand*individual);
        if mpoint<=0
            mpoint=1;
        end
        if newpop1(i,mpoint)==0
            newpop1(i,mpoint)=1;
        else
            newpop1(i,mpoint)=0;
        end
    else
        %²»±äÒì
    end
end
newpop2=newpop1;
