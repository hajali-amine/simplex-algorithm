function [m]=calculate(pivot,pindex1,pindex2,matrix,numcol)
    [nl nc]=size(matrix);

    for j=1:nc
        matrix(pindex1,j)=matrix(pindex1,j)/pivot;
    end;

    for i=1:numcol
        if (i ~= pindex1)
            k=matrix(i,pindex2);
            for j=1:nc
                matrix(i,j)=matrix(i,j)-k*matrix(pindex1,j);
            end;
        end;
    end;
    
    m=matrix;
end