function simplex()
    [m,a,c,nc,indexes,nv]=init();
    [m,a,c,p,pivi,pivj,indexes]=pivot(m,a,c,indexes,nv);
    posit=verify(m);
    x=0;

    while (posit==1)
        [m]=calculate(p,pivi,pivj,m,nc);
        [m,a,c,p,pivi,pivj,indexes]=pivot(m,a,c,indexes,nv);
        posit=verify(m);
    end;
    
    [m]=result(m,indexes,nv);
end
