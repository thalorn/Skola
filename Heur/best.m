function [bestweight,bestvalue,bestpop]=best(newpop,fitvalue,w)
%Ñ°ÕÒ×îÓÅ¸öÌå£¬°üÀ¨ÆäÖØÁ¿ºÍ¼ÛÖµ¡£

[popsize,individual]=size(newpop);
bestvalue=fitvalue(1);

for i=2:popsize
    if fitvalue(i)>bestvalue
        bestvalue=fitvalue(i);
        
    end
   
end

[~,index]=max(fitvalue);%¼ÆËã×îÓÅ¼ÛÖµ£¬ºÍ×îÓÅÖØÁ¿¡£

bestweight=0;
bestpop=zeros(1,individual);
i=index;
for j=1:individual
    bestweight=w(j)*newpop(i,j)+bestweight;
    bestpop(1,j)= newpop (i,j);
end


end

