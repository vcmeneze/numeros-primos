a, b = map(int, input('Digite o intervalo de numeros que deseja: ').split())
primo=0 

for x in range(a,b+1):
  contador=0
  for y in range(1,x+1):
    if x % y == 0:
      contador +=1
  if contador == 2: 
    primo +=1
print('Essa é a quantidade de números primos existentes entre', a, 'e', b, ': ', primo)