import_error = []


try:
    from gsearchlib import Search
    from colorama import Fore, Back, init
    from time import sleep
    import urllib
except ImportError:
    import_error.append('gsearchlib')
    import_error.append('colorama')
    import_error.append('time')
    import_error.append('urllib3')
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
        input(f'You havent installed {import_error} library. \nTo do so, write: pip install {import_error} \nPress CLOSE to exit')
        exit()
    else:
        print("Then fuck off idiot")
        input("Press CLOSE to exit")
        exit()

init(convert=True)

while True:
    print(Back.CYAN + Fore.BLACK + '1. Open link.')
    print(Back.CYAN + Fore.BLACK + '2. Read URL data')
    print(Back.CYAN + Fore.BLACK + '3. Google Search')

    usrintinp = int(input(Back.CYAN + Fore.BLACK + 'Welcome to my program! \nWrite function you want to see: '))

    usrfucntion = ('1', '2', '3')
    if usrintinp in usrfucntion == 1:
        openthis_url() # this function is not defined yet
    elif usrintinp in usrfucntion == 2:
        read_url_from_input() # this function is not defined yet
    elif usrintinp in usrfucntion == 3:
        google_search() # this function is not defined yet
    else:
        input("This function doesnt exist :( \nPress ENTER to close")
        exit()



def openthis_url(url):
    get_url = urllib.urlopen(url)
    print("Response Status: "+ str(get_url.getcode()) )
def read_url_from_input(url_2):
    get_url_2 = urllib.urlopen(url_2)
    print(get_url_2.read())

def openthe_link():
        print("1. Get response status from the link. \n2. Read url file")

        usrinp = ("Tell me what to do: ")
        choice_from_user = ('1', '2')
        if usrinp in choice_from_user == 1:
            usrinpchoice = input("Paste your link here: ")
            result_from_1 = openthis_url(usrinpchoice)
            print(result_from_1)
            A = input("Are you happy with the result? ")
            B = input("Thank you for using my functions! \nPress ENTER to close")
            exit()
        elif usrinp in choice_from_user == 2:
            usrinpchoice_2 = input("Paste your link here: ")
            result_from_2 = read_url_from_input(usrinpchoice_2)
            print(result_from_2)
            C = input("Copy the result if needed.")
            D = input(Fore.BLACK + Back.CYAN + 'Thank you for using my functions! \nPress ENTER to close')
            exit()


def google_search():
        print(Back.CYAN + Fore.BLACK + 'This program was made by me while I was drunk xd')
        searchvariant = input(Fore.BLACK + 'Welcome to Google Search! \nWrite "Y" to continue or "N" to close program: ')
        yes = ['Y']
        if searchvariant in (yes):
            print(Fore.BLACK + 'Search engine is loading....')
            sleep(4)
            var = input(Back.WHITE + 'Write what do you want to see: ')
            res = Search(var)
            print(res)
            k = input("Do you want to continue? ")
            if k in (yes):
                openthe_link()
            elif k not in (yes):
                input("Thank you for using my little app! \nPress ENTER to close")
                exit()
