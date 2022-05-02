with open('/etc/passwd') as f:
    lines = f.readlines() 
    for a in lines:
        print(a)