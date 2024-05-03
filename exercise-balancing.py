# Crie um programa em Python que verifique se uma expressão matemática contendo parênteses está corretamente balanceada.
# Ou seja, todos os parênteses abertos devem ser fechados na ordem correta.

def check_balancing(expr):
    stack = []
    for c in expr:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0 or stack.pop() != '(':   # módulo: se a pilha nao esta vazia.
                return False
    return len(stack) == 0


result = check_balancing('')
print(result)
