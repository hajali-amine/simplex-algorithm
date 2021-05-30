function a=verify(matrix)
    b=0;
    [nl nc]=size(matrix);
    p=matrix(nl,:);
    for i=1:nc
        if (p(i)>0)
            b=1;
        end;
    end;
    a=b;
end