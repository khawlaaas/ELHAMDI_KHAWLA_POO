with open('Table de multiplication.txt','w') as file:
    for i in range(1,11):
        file.write(f'La table de multiplication de {i:02}\n')
        for j in range (1,11):
            result = i*j
            file.write(f'{i:02} x {j:02} = {result}\n')
        file.write('\n')