def pifagor(y,x):

    print(' '.center(5),end=' ')
    for j in range(y-5,y+6):
        print(str(j).center(5),end=' ')
        
    print('\n')
    for i in range(x-5,x+6):
        print(str(i).center(5),end=' ')
        
        for j in range(y-5,y+6):
            z=i*j
            print(str(z).center(5),end=' ')
           
        print('\n')
        
pifagor(7,9)