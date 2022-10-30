"""User interactions for input and appending text"""


def get_user_input():
    """gets user input"""
    user_input = input('Enter here: ')
    print('\n')
    return user_input


def append_prompt():
    print('Enter your desired prompt text with "{}" where a NOUN should be.')
    print('I.e. I\'m not a big fan of {}, but hey, you do you.')
    with open('txt_files/prompt.txt', 'a') as q:
        q.write('\n' + get_user_input())


def append_resp():
    print('Enter a response or a noun that will be included in the text string.')
    print('I.e. Monty Python / Punching my dad in the face and stealing his car / Lightsabers  .')
    with open('txt_files/resp.txt', 'a') as q:
        q.write('\n' + get_user_input())
