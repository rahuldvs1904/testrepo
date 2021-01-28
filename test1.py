def funct(x): 
    n=[]
    for i in x:
        if i!=' ':
            n.append(i)
    spaces= len(x) - len(n)
    r = ' '*spaces    
    print(r + ''.join(n))
  
s1 = "w3  resources"
print(funct(s1))


