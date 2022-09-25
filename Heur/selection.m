function [newpop]=selection(pop,fitvalue)

%Ñ¡Ôñ²Ù×÷£¬°´±ÈÀýµÄÑ¡Ôñ·½·¨,¸÷¸ö¸öÌå±»Ñ¡ÖÐµÄ¸ÅÂÊÓëÆäÊÊÓ¦¶È´óÐ¡³ÉÕý±È£®

    totalfit=sum(fitvalue);             %ÇóÊÊÓ¦¶ÈÖµÖ®ºÍ 
    
    pfitvalue=fitvalue/totalfit;        %µ¥¸ö¸öÌå±»Ñ¡ÔñµÄ¸ÅÂÊ
                                        %µ¥¸ö¸öÌåÊÊÓ¦¶ÈÔ½´ó£¬±»Ñ¡ÔñµÄ¿ÉÄÜÔ½´ó
    
    %cumsumÇóÀÛ¼ÆºÍ Èç fitvalue=[0.1 0.2 0.3 0.4] 
                    %cumsum(fitvalue)=[0.1 0.3 0.6 1] 
    %doc cumsum
    mfitvalue=cumsum(pfitvalue); 
    
    [popsize,~]=size(pop); 
    
    ms=sort(rand(popsize,1)); %rand()Éú³É¾ùÔÈ·Ö²¼µÄËæ»úÊý£¬È»ºó´ÓÐ¡µ½´óÅÅÁÐ
    
    fitin=1; 
    newin=1;
    newpop=zeros(size(pop));
    
    while newin<=popsize
        if mfitvalue(fitin)>ms(newin)
            newpop(newin,:)=pop(fitin,:); 
            newin=newin+1; 
        else 
        fitin=fitin+1; 
        end 
    end
    
    %example  mfitvalue=[0.1 0.3 0.6 1]
    %         ms=[0.25,0.5,0.75,1]
end
