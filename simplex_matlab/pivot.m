function [m,a,c,p,i,j,ind]=pivot(matrix,array,coeff,indexes,nv)
    [nl nc]=size(matrix); 
    tcoeff=coeff(1:end-nv);

    for j=1:nc
        col=matrix(:,j);
        col = transpose(col(1:end-2,:));
        matrix(nl-1,j)=dot(tcoeff,col);
    end;

    for i=1:nc-1
        matrix(nl,i)=array(i)-matrix(nl-1,i);
    end;

    indexj=0;
    x=max(matrix(nl,:));
    for i=1:nc-1
        if (matrix(nl,i)==x)
            indexj=i;
            break;
        end;
    end;

    col=matrix(:,indexj);
    col = transpose(col(1:end-2,:));
    for i=1:nl-2
        if ((col(i)==0)||(col(i)<0))
            d(i)=999999;
        else
            d(i)=matrix(i,nc)/col(i);
        end;
    end;

    indexi=0;
    x=min(d);
    for i=1:nc-2
        if (d(i)==x)
            indexi=i;
            break;
        end;
    end;
    
    coeff(indexi)=array(indexj);
    indexes{indexj}=indexi;
    pivot=matrix(indexi,indexj);
    p=pivot;
    m=matrix;
    c=coeff;
    a=array;
    ind=indexes;
    i=indexi;
    j=indexj;
end