N = int(input())

print(N)

print(f'{N//100} nota(s) de R$ 100,00')
N = N % 100

print(f'{N//50} nota(s) de R$ 50,00')
N = N % 50

print(f'{N//20} nota(s) de R$ 20,00')
N = N % 20

print(f'{N//10} nota(s) de R$ 10,00')
N = N % 10

print(f'{N//5} nota(s) de R$ 5,00')
N = N % 5

print(f'{N//2} nota(s) de R$ 2,00')
N = N % 2

print(f'{N//1} nota(s) de R$ 1,00')
N = N % 1
