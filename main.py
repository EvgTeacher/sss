# Встроенная - Глобальная - Локальная - Нелокальная
# def func():
#     var_1 = 10
#     print(var_1)
#
#
# var_1 = 1
# func()
# print(var_1)

# def first():
#     var_1 = 10
#     print(var_1)
#
#     def second():
#         global var_1
#         var_1 = 50
#         print(var_1)
#
#     second()
#
#
# var_1 = 5
# first()
# print(var_1)


from random import choice


def game(choise_user, result):
    print('--------Start Game----------')
    choise_comp = choice('rps')
    print('----------------------------')
    print('Your select', choise_user.lower())
    print('Comp select', choise_comp)

    if choise_user.lower() == choise_comp:
        print('Result of game - DRAW')
        print('Score, Computer', result['user'], result['comp'])
    elif choise_user.lower() == 'r' and choise_comp == 'p':
        print('Comp WIN')
        result['comp'] += 1
        print('Score, Computer', result['user'], result['comp'])
    elif choise_user.lower() == 'r' and choise_comp == 's':
        print('User WIN')
        result['user'] += 1
        print('Score, Computer', result['user'], result['comp'])
    elif choise_user.lower() == 's' and choise_comp == 'r':
        print('Comp WIN')
        result['comp'] += 1
        print('Score, Computer', result['user'], result['comp'])
    elif choise_user.lower() == 's' and choise_comp == 'p':
        print('User WIN')
        result['user'] += 1
        print('Score, Computer', result['user'], result['comp'])
    elif choise_user.lower() == 'p' and choise_comp == 's':
        print('Comp WIN')
        result['comp'] += 1
        print('Score, Computer', result['user'], result['comp'])
    elif choise_user.lower() == 'p' and choise_comp == 'r':
        print('User WIN')
        result['user'] += 1
        print('Score, Computer', result['user'], result['comp'])


result = {'comp': 0, 'user': 0}
choise_user = input("Select R / P / S ")

game(choise_user, result)