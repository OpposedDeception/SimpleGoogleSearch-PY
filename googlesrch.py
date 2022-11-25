try:
    from gsearchlib import Search
    from colorama import Fore, Back, init
    from time import sleep
    import urllib
    import webbrowser
except ImportError:
    import_error.append('gsearchlib')
    import_error.append('colorama')
    import_error.append('time')
    import_error.append('urllib3')
    import_error.append('webbrowser')           
    input(f'You havent installed {import_error} library. \nTo do so, write: pip install {import_error} \nPress CLOSE to exit')
        exit()
        
init(convert=True)

class OpenInBrowser:
    def __init__(self, choice_the_user):
        self.choice_the_user = choice_the_user
        
    def open_in_browser_link(self, choice_the_user):
       webbrowser.open(self.choice_the_user, new = 0, autoraise = True)
       
    @staticmethod
    def ask_user():
        try:
            dogshit = input("Paste your link here: ")
            open_in_browser_link()
        except NameError:
            webbrowser.open(dogshit, new = 0, autoraise = True)
        
class UrlStatus(OpenInBrowser):
    def openthis_url(self, choice_the_user):
        with urllib.urlopen(self.choice_the_user) as get_url:
            print(f'Response Status: {get_url.getcode()}')

def openthe_link():
        print("3. Get response status from the link. \n4. Read url file")

        usrinp = input("Tell me what to do: ")
        choice_from_user = ('3')
        choice_from_user_two = ('4')
        if usrinp in (choice_from_user):
            if usrinp in (choice_from_user):
            OpenInBrowser.ask_user()
            A = input("Are you happy with the result? ")
            B = input("Thank you for using my functions! \nPress ENTER to close")
            exit()
        elif usrinp in (choice_from_user_two):
            usrinpchoice_2 = input("Paste your link here: ")
            UrlStatus.openthis_url(usrinpchoice_2)
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

while True:
     print(Back.CYAN + Fore.BLACK + '1. More URL functions')
     print(Back.CYAN + Fore.BLACK + '2. Google Search')

     usrintinp = int(input(Back.CYAN + Fore.BLACK + 'Welcome to my program! \nWrite function you want to see: '))

     usrfucntion = ('1', '2')
     if usrintinp == 1:
         openthe_link()
     elif usrintinp == 2:
         google_search()
     else:
         input("This function doesnt exist :( \nPress ENTER to close")
         exit()
