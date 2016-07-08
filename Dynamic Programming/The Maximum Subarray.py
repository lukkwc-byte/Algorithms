def main():
    tests = int(input())
    for _ in range(tests):
        size, arr  = int(input()), [int(i) for i in input().split()]
        print(max_subarrays(arr))

def max_subarrays(arr):
    max_cont =  current_cont = arr[0]
    for x in arr[1:]:
        current_cont = max(x, current_cont + x)
        max_cont = max(current_cont, max_cont)
    max_non_cont = 0
    if max(arr) < 0:
        max_non_cont = max(arr)
    else:
        for x in arr:
            if x > 0:
                max_non_cont += x
    return " ".join([str(x) for x in [max_cont, max_non_cont]])
    
main()   