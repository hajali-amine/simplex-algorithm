function [m,a,co,nc,ind,nv]=init()

    n=input('Votre fonction objective Z est composée de combien de variable? \n');
    
    for i=1:n
        msg=['Inserez le coefficient a',num2str(i),': '];
        array(i)=input(msg);
    end;
    
    msg='';
    for i=1:n
        msg=[msg,num2str(array(i)),'x',num2str(i),'+'];
    end;
    msg =['Z= ' msg(1:end-1)];
    disp(msg);
    
    j=0;
    b_msg=['resultat de equation '];
    c=input('Quel est le nombre de contraintes?: \n');
    matrix=zeros(c+2);
    for i=1:n+c
        coeff(i)=0;
        indexes{i}=0;
    end;
    
    for i=1:c
        for j=1:n
            x=['inserez le coefficient a',num2str(j),': '];
            matrix(i,j)=input(x);
        end;
        matrix(i,n+i)=1;
        matrix(i,n+c+1)=input(b_msg);
    end;
    
    msg='';
    for i=1:c
        for j=1:n
         msg=strcat(msg,num2str(matrix(i,j)),'x',num2str(j),'+');  
        end;
    msg = msg(1:end-1);
    msg=strcat(msg,'<=',num2str(matrix(i,n+c+1)));
    disp(msg);
    msg='';
    end;

    for i=n+1:n+c
        array(i)=0;
    end;
    
    m=matrix;
    a=array;
    co=coeff;
    ind=indexes;
    nc=c;
    nv=n;
end