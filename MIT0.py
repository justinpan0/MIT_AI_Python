#define cube function
def cube(n):
        res = n * n * n;
        print (res)
        return

cube(3)

#define factorial function
def factorial(n):
    if n == 0:
        print ("1");
    else:
        res = 1
        
        for num in range(1,n+1):
            res = res * num;
        print (res)

factorial(5)

#define depth function for depth of difficulty represented as parenthesis.
def depth(expr,n):
        for i in expr:
                if isinstance(i, (list, tuple)):
                        n += 1
                        depth(i,n)
        return n+1

def runDepth(expr):
        res = [0]
        if isinstance(expr,(list,tuple)):
                res.append(1)
                
        for item in expr:
                if isinstance(item,(list,tuple)):
                        res.append(depth(item,1))
        return max(res)

print (runDepth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2),1), ('/', 5, 2)))))
