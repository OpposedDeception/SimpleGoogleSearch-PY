from gsearchlib import Search
from colorama import Fore, Back, init
from time import sleep
import urllib.request
import webbrowser
from rich.progress import Progress 
from pprint import pprint 
import json
        
init(convert=True)

# Not tested yet
class SaveInJSON:
    def __init__(self, data, results):
        self.data = data
        self.results = results
        
    def save_in_json(self):
        json_object = json.dumps(self.data, indent=self.results)
        with open("search_result.json", "w") as outfile:
            outfile.write(json_object)

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
    def openthis_url(self):
        catshit = input("Write the link here: ")
        with urllib.request.urlopen(catshit) as url:
            print(f'Response Status: {url.getcode()}')

def openthe_link():
        print("3. Get response status from the link. \n4. Read url file.")
        print("5. Save data in JSON file")

        usrinp = input("Tell me what to do: ")
        choice_from_user = ('3')
        choice_from_user_two = ('4')
        choice_from_user_three = ('5')
        if usrinp in (choice_from_user):
            if usrinp in (choice_from_user):
            OpenInBrowser.ask_user()
            A = input("Are you happy with the result? ")
            B = input("Thank you for using my functions! \nPress ENTER to close")
            exit()
        elif usrinp in (choice_from_user_two):
            pass
            UrlStatus.openthis_url(usrinp)
            C = input("Copy the result if needed.")
            D = input(Fore.BLACK + Back.CYAN + 'Thank you for using my functions! \nPress ENTER to close')
            exit()
        elif usrinp in (choice_from_user_three):
            try:
                SaveInJSON.save_in_json(data, count)
            except:
                raise IOError("There was an issue with writing data into file.")
            finally:
                pass 
                exit()


def google_search():
        print(Back.CYAN + Fore.BLACK + 'This program was made by me while I was drunk xd')
        searchvariant = input(Fore.BLACK + 'Welcome to Google Search! \nWrite "Y" to continue or "N" to close program: ')
        yes = ['Y']
        if searchvariant in (yes):
            with Progress() as progress:
                engine_loading = progress.add_task("[green]Loading search engine....", total=100)
                while not progress.finished:
                    progress.update(engine_loading, advance=0.5)
                    sleep(0.04)
            var = input(Back.WHITE + 'Write what do you want to see: ')
            res = Search(var)
            data = pprint(res)
            count = int(input("Write how many results you got: "))
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
