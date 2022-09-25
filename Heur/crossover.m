function [newpop1]=crossover(newpop,pc)  %pc ½»²æÂÊ
%½»²æ
%½»²æÂÊ²»ÄÜÌ«´ó Ì«´ó¿ÉÄÜ»á¹ýÓÚËæ»ú£¬Ì«Ð¡»áµ¼ÖÂÊÕÁ²µÄºÜÂý£¬µ±Ç°Ò»°ã»áÉèÖÃÎª×ÔÊÊÓ¦£¬Ëæ×Å´úÊýµÄÔö¼Ó¶øÏÂ½µ
%ÒÅ´«Ëã·¨×Ó³ÌÐò
%Name: crossover.m

[popsize,individual]=size(newpop);
newpop1=zeros(popsize,individual);

for i=1:2:popsize-1  %Ã¿Á½¸ö×÷ÎªÄ¸±¾°´½»²æÂÊ½øÐÐ½»²æ
    
    ps=rand; %Ò»¸ö0-1Ö®¼ä¾ùÔÈ·Ö²¼µÄËæ»úÊý
    
    if ps<pc %½»²æ²úÉúÁ½¸ö×Ó´ú
        cpoint=round(rand*individual);
        
        newpop1(i,:)=[newpop(i,1:cpoint),newpop(i+1,cpoint+1:individual)];
        
        newpop1(i+1,:)=[newpop(i+1,1:cpoint),newpop(i,cpoint+1:individual)];
    else %²»½»²æ£¬×Ó´úºÍ¸¸´úÒ»ÖÂ
        newpop1(i,:)=newpop(i,:);
        newpop1(i+1,:)=newpop(i+1,:);
    end
end
