fib_array =[0,1]

def fab_dp (n):
    if n < len(fib_array) :
        return fib_array[n]
    else :
        fib = fab_dp(n-1) + fab_dp(n-2)
        fib_array.append(fib)
        return fib

n = int(input())
print(fab_dp(n))