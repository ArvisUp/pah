from multiprocessing.connection import wait
import modules.random_roll as random_roll


def get_user_choice():
    """gets user input"""
    user_input = input('Your choice: ')
    print('\n')
    return user_input


waiting_for_input = True

while waiting_for_input:
    print('\n')
    print('Please choose one.')
    print('1: Roll one.')
    print('q: Quit.')

    user_choice = get_user_choice()
    if user_choice == '1':
        print(random_roll.random_string())
    elif user_choice == 'q':
        waiting_for_input = False

    else:
        print('Input was invalid, please pick a value from the list!')

else:
    print('User left.')

print('Done!')
