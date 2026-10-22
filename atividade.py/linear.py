números = [10,25,8,40,15,30,7,50,12,20]
busca = int(input('Digite o numero que deseja buscar:'))
encontrado=False
for i in range(len(números)):
 if números[i]== busca:
   print(f'numero encontrado no índice {i}')
   encontrado = True
   break
if not encontrado:
 print('numero não encontrado.')
 