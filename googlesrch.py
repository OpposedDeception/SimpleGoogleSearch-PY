import_error = []


try:
    from googlesearch import search
    from colorama import Fore, Back
    from time import sleep
except ImportError:
    import_error.append('googlesearch-python')
    import_error.append('colorama')
    import_error.append('time')
    user_choice = input("You got import error. Do you want to continue?: ")

    positive_variants = ['yes',
                         'Yes',
                         'yES',
                         'yEs',
                         'YeS',
                         'yeS',
                         'YES']

    negative_variants = ['no',
                         'NO',
                         'nah',
                         'NAH',
                         'noo',
                         'nO',
                         'No']

    if user_choice in (positive_variants):
        input(Fore.RED + f'You havent installed {import_error} library. \nTo do so, write: pip install {import_error} \nPress CLOSE to exit')
        exit()
    else:
        print("Then fuck off idiot")
        input("Press CLOSE to exit")
        exit()


print(Back.CYAN + Fore.BLACK + 'This program was made by me while I was drunk xd')
searchvariant = input(Fore.BLACK + 'Welcome to Google Search! \nWrite "Y" to continue or "N" to close program: ')
yes = ['Y']
if searchvariant in (yes):
    print(Fore.BLACK + 'Search engine is loading....')
    sleep(4)
    var = input(Back.WHITE + 'Write what do you want to see: ')
    res = Search(var)
    print(res)
    k = input("Press CLOSE to exit")
    exit()
else:
    input(Back.CYAN + Fore.BLACK + 'N means NO, then goodbye. Press CLOSE to exit')
    exit()
