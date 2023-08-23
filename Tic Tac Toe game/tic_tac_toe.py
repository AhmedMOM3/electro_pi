#func checks if x wins
def x_wins(ls):
    for i in range(3):
        if (ls[i][0]=='x' and ls[i][1]=='x' and ls[i][2]=='x'):
            return True
    for i in range(3):
        if (ls[0][i]=='x' and ls[1][i]=='x' and ls[2][i]=='x'):
            return True    
    if (ls[0][2]=='x' and ls[1][1]=='x' and ls[2][0]=='x'):
        return True 
    if (ls[0][0]=='x' and ls[1][1]=='x' and ls[2][2]=='x'):
        return True   
#func checks if o wins
def o_wins(ls):
    for i in range(3):
        if (ls[i][0]=='o' and ls[i][1]=='o' and ls[i][2]=='o'):
            return True
    for i in range(3):
        if (ls[0][i]=='o' and ls[1][i]=='o' and ls[2][i]=='o'):
            return True    
    if (ls[0][2]=='o' and ls[1][1]=='o' and ls[2][0]=='o'):
        return True 
    if (ls[0][0]=='o' and ls[1][1]=='o' and ls[2][2]=='o'):
        return True   
#the game board        
tic=[['_','_','_'],
    ['_','_','_'],
    ['_','_','_'],]

old_sympol=''
i=0
while(i<9):
    i+=1 
#getting the sympol       
    sympol=input('please enter the sympol(o/x): ').lower()
    if sympol !='x' and sympol !='o':
        print ('please enter just (x/o)')
        i-=1
        continue
    
    if i!=1 and sympol ==old_sympol:
        print('please enter another sympol.')
        i-=1
        continue
    old_sympol=sympol
#q will be 1 if he entered the True symppl
    q=0
    while(q==0):
#x will be 1 if he entered a valied location         
        x=0
        while(x==0):
            try:
                row=int (input('enter the row (1,2,3): '))
                column=int (input('enter the column (1,2,3): '))
                
            except ValueError:
                print('please enter a valid location.')
                x=0
                continue
            else:
                x=1
            if(row>3 or column>3):
                x=0
                print('please enter a valid location')    

        if tic[row-1][column-1] =='x' or tic[row-1][column-1]=='o':
            q=0
            print('there is a sympol in the location')
        else:    
            tic[row-1][column-1]=sympol
            q=1

#printing the board
    for x in range(3):
        for y in range(3):
            print(tic[x][y], end=" ")
        print("")    

#check if x or o wins
    if x_wins(tic):
        print('* X wins')
        break
    elif o_wins(tic):
        print('* O wins')
        break   


if x_wins(tic)!= True and o_wins(tic)!= True:
    print('No one win')      