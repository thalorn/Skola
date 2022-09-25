%计算每一个个体的适应度，并利用罚函数计算目标函数
%利用罚函数法计算目标函数及其适应度

function [fitvalue]=calobjvalue(pop,V,W,CW)

[popsize,individual]=size(pop);

sumV=zeros(1,1000);
sumW=zeros(1,1000);
fitvalue=zeros(1,1000);

for i=1:popsize

    for j=1:individual
       
          sumV(i)=sumV(i)+V(j)*pop(i,j);   %计算个体的value和，作为适应度
          
          sumW(i)=sumW(i)+W(j)*pop(i,j);   %计算个体的weight和，作为罚函数
                                           %不超过边界为其本身，超过边界无穷大
    end
    
    if sumW(i)>CW
          sumV(i)=0;
    else 
       sumV(i)=sumV(i);
          
    end
 
  fitvalue(i)=sumV(i);
  
end
