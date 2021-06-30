print('Would you like to continue?')
is_continue_str = str(input())

if(is_continue_str == 'yes' or is_continue_str == 'y'):
    print('Continuing ...')
    print('Complete!')
elif(is_continue_str == 'no' or is_continue_str == 'n'):
    print('Exiting')
else:
    print('Please try again and respond with yes or no.')