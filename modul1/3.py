def jumlahhurufvokal(input):
    total = 0
    vokal =['a','i','u','e','o']
    for i in input:
        if i in vokal:
            total+=1
    return [len(input),total]
    
v = jumlahhurufvokal("Surakarta")
print(v)

def jumlahhurufvokal(input):
    total = 0
    vokal =['a','i','u','e','o']
    for i in input:
        if i in vokal:
            total+=1
    return [len(input),len(input)-total]

k = jumlahhurufvokal("Surakarta")
print(k)
