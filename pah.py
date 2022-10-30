from multiprocessing.connection import wait
import modules.random_roll as random_roll
import modules.user_interaction as usr_interaction


waiting_for_input = True
print('\nWELCOME TO THE\nPYTHON AGAINST HOOMAAAANS\nPlease dont be offended as this is just some random string concatenator? Please.')
while waiting_for_input:
    print('\n')
    print('Choose what to do(enter number or "q").')
    print('1: Roll one.')
    print('2: Append your of prompt line.')
    print('3: Append your of response line.')
    print('q: Quit.')

    user_choice = usr_interaction.get_user_input()
    if user_choice == '1':
        generated_string = random_roll.random_string()
        string_len = len(generated_string) + 4
        print(("=" * string_len) + "\n= " +
              generated_string + " =\n" + ("=" * string_len))

    elif user_choice == '2':
        usr_interaction.append_prompt()
    elif user_choice == '3':
        usr_interaction.append_resp()
    elif user_choice == 'q':
        waiting_for_input = False

    else:
        print('Input was invalid, please pick a value from the list!')

else:

    print("BUT WAIT, THERE'S MORE!\n" + random_roll.random_string())

print('\nDone, user left.')
