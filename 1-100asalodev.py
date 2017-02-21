for x in range(2,100,1):
    kontrol=True
    for y in range(2,100,1):
        if x==y:
            continue
        elif x%y==0 and x!=2:
            kontrol=False
    if kontrol:
        print(x)
