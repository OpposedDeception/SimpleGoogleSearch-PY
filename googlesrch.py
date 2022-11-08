import_error = []


try:
    from googlesearch import search
    import colorama
except ImportError:
    import_error.append('googlesearch-python')
    import_error.append('colorama')
    import_error.append('variantsez')
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
        print(f"You havent installed {import_error} library. \nTo do so, write: pip install {import_error}")
    else:
        print("Then fuck off idiot")