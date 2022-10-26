import sys


def SRT(procs):
    m = len(procs)
    wait_t = [0 for _ in range(m)]
    ret_t = [0 for _ in range(m)]
    exit_t = [0 for _ in range(m)]
    resp_t = [0 for _ in range(m)]
    cpu_req = []
    for i in range(m):
        cpu_req.append(procs[i][1])
    counter = 0
    t = 0
    minm = sys.maxsize
    short = 0

    while counter != m:
        last_short = short
        for j in range(m):
            if t != 0 and t == procs[j][0] and resp_t[last_short] == 0:
                resp_t[last_short] = t - procs[last_short][0]
            if procs[j][0] <= t and minm > cpu_req[j] > 0:
                minm = cpu_req[j]
                short = j
        cpu_req[short] -= 1
        minm = cpu_req[short]
        if cpu_req[short] == 0:
            minm = sys.maxsize
            counter += 1
            exit_t[short] = t + 1
            ret_t[short] = t + 1 - procs[short][0]
            wait_t[short] = t + 1 - procs[short][1] - procs[short][0]
            if resp_t[short] == 0:
                resp_t[short] = t + 1 - procs[short][0]
        t += 1

    print("\nPi    exit return wait response")
    print("--------------------------------")
    for i in range(m):
        print(f"p{procs[i][2] : <5} {exit_t[i] : <5} {ret_t[i] : <5} {wait_t[i] : <5} {resp_t[i] : <5} ")

    print(f"\nexit average: {sum(exit_t) / m : .3f}")
    print(f"return average: {sum(ret_t) / m : .3f}")
    print(f"wait average: {sum(wait_t) / m : .3f}")
    print(f"response average: {sum(resp_t) / m : .3f}")


n = int(input("Enter count of process: "))

process = []

print("P  | in  cpu ")
print("------------------")
i = 0
while i < n:
    try:
        p = list(map(int, input(f"P{i + 1} : ").split()))
        if len(p) != 2:
            print("input is wrong!!")
            continue
        i += 1
        p.append(i)
        process.append(p)

    except:
        print("input is wrong!!")

SRT(process)

# sample
# 0 8
# 1 4
# 2 9
# 3 5

# 2 6
# 5 2
# 1 8
# 0 3
# 4 4

# 1 6
# 1 8
# 2 7
# 3 3

# 2 6
# 5 2
# 1 8
# 0 3
# 4 4
