#determine whether the seller has made a profit or incurred a loss. Also, 
# determine the quantum of profit or loss
cp=int(input('enter the user pcost prize'))
sp=int(input('enter the user seller prize'))
if sp>cp:
    profit = sp-cp
    print('profit')
    print(f'profit{profit}')
else:
    loss =cp-sp
    print(f'loss{loss}')
    