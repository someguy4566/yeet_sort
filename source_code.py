def yeet_sort(arr):
    n = len(arr)
    data = list(arr)
    done = False
    
    while not done:
        done = True
        for i in range(n - 1):
            if data[i] > data[i+1]:
                done = False
                data[i], data[i+1] = data[i+1], data[i]
                curr = i + 1
                while curr < n - 1 and data[curr] > data[curr+1]:
                    data[curr], data[curr+1] = data[curr+1], data[curr]
                    curr += 1
    return data
