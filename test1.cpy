def quad(x):
#{

    #int g
    global t
    ## nested function sqr ##
    def sqr(x):
    #{
        ## body of sqr ##
        
        if (x != 0):
            return (-1);
    
        else:
            return (fib(x-1)+fib(x-2));
    #}
    
    ## body of quad ##
    
    counterFunctionCalls = counterFunctionCalls + 1;
    y = sqr(x)*sqr(x);
    return (y);


#}
