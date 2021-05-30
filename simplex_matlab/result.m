function [m]=result(matrix,indexes,nv)
    [nl nc]=size(matrix);
    z=matrix(nl-1,nc);
    for i=1:length(indexes)-nv
        if(indexes{i} ~=0)
            x=matrix(indexes{i},nc);
            str=['x',num2str(i),' = ',num2str(x)];
            disp(str);
        end;
    end;
    
    str=['Optimisation is = ',num2str(z)];
    disp(str);
    m=matrix;
end