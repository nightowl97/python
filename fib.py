import time
'''
Dynamic programming algorithm for fibonacci with subproblem reuse from memory
'''


def answer(n):
    def fib(num):
        if mem[num] != -1:
            return mem[num]
        if num <= 2:
            return 1
        else:
            f = fib(num - 1) + fib(num - 2)
            mem[num] = f
            return f

    mem = [-1 for i in range(n + 1)]
    return fib(n)


start_time = time.time()
print answer(500)
print("--- %s seconds ---" % (time.time() - start_time))
