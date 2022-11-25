import random


def choose_options():
    user_option = input('Piedra, papel o tijera => ')
    user_option = user_option.lower()
    computer_option = ['piedra','papel','tijera']
    computer_option2 = random.choice(computer_option)

    if not user_option in computer_option:
        print('Esa opción no es valida, escriba la opción correcta')
        #continue
        return None, None

    return user_option, computer_option2

def check_rules(user_option, computer_option2, user_wins, computer_wins):
    if user_option == computer_option2:
        print('Empate!')
    elif (user_option == 'piedra' and computer_option2 == 'tijera'):
        print('Piedra gana a tijera')
        print('user gano')
        user_wins += 1
    elif(user_option == 'tijera' and computer_option2 == 'papel'):
        print('Tijera gana a papel')
        print('user gano')
        user_wins += 1
    elif (user_option == 'papel' and computer_option2 == 'piedra'):
        print('Papel gana a piedra')
        print('user gano')
        user_wins += 1
    else:
        print(computer_option2 +' gana')
        print('Computer gano')
        computer_wins += 1
    return user_wins, computer_wins

def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1


    while True:
        print('*'*10)
        print('round', rounds)
        print('*'*10)

        print('User wins ', user_wins)
        print('Computer wins ', computer_wins)
        rounds += 1

        user_option, computer_option2 = choose_options()
        user_wins, computer_wins = check_rules(user_option, computer_option2, user_wins, computer_wins)


        if computer_wins == 3:
            print('El ganador es la computadora')
            print('Computer ', computer_wins)
            print('Usuario ', user_wins)
            break
        elif user_wins == 3:
            print('El ganador es el usuario')
            print('Usuario ', user_wins)
            print('Computer ', computer_wins)
            break

run_game()