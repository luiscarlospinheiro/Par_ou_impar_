

from random import randint

v = 0
pc = 0
o = ''
r = 0
print('Jogo do par ou ímpar')
while True:
    v = int(input('digite um valor: '))
    pc = randint (0,20)
    o = str(input('Par ou Impar? [P/I]')).strip().upper()[0]
    r = v + pc
    if o == 'P':
        if r % 2 == 0:
            print(f'Ganhou! deu par (o pc jogou {pc})')
    if o == 'P':
        if r % 2 != 0:
           print(f'Perdeu! deu ímpar (o pc jogou {pc})')
    if o == 'I':
        if r % 2 == 0:
            print(f'Perdeu! deu par (o pc jogou {pc})')
        if r % 2 != 0:
            print(f'Ganhou! deu ímpar (o pc jogou {pc})')
    print('Vamos jogar novamente...')




