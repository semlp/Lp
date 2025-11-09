def fib_rec(n,call,add):
    call[0]+=1
    if n<=1:
        return n
    else:
        add[0]+=1
        return fib_rec(n-1,call,add)+fib_rec(n-2,call,add)
    
def fib_ite(n,call,add):
    call[0]+=1
    if n<=1:
        return n
    a,b=0,1
    for i in range(2,n+1):
        call[0]+=1
        add[0]+=1
        a,b=b,a+b
    return b

n=int(input("enter position of num for fib num:"))
#rec
rec_call=[0]
rec_add=[0]
fib_re=fib_rec(n,rec_call,rec_add)
#it
ite_call=[0]
ite_add=[0]
fib_it=fib_ite(n,ite_call,ite_add)
print("fib series")
for i in range(n):
    print(fib_rec(i, [0], [0]), end=" ")

print(f" fib num at position {n}:{fib_re}")
print(f"\n\n rec")
print(f" steps(function call):{rec_call[0]}")
print(f" steps(add):{rec_add[0]}")
print(f"\n\n ite")
print(f"steps(fun call):{ite_call[0]} ")
print(f" steps(add):{ite_add[0]}")