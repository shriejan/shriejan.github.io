



def innocent_bot(inp):
    
    return res

def getResponse(inp):
    '''return combined input and output'''
    response = innocent_bot(inp) # later i will link it with api
    total = f'the response for your "{inp}" is "{response}"'
    return total 


# run for loop for 5 times and call get response function based on your input


for i in range(5):
    inp = input('please write you input:')
    out = getResponse(inp)

    print(out)

    
    
    