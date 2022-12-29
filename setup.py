from setuptools import setup, find_packages

setup(
    name='SimpleGoogleSearch-PY',
    version='0.5Beta',
    description='Simple google search engine in command prompt',
    author='KotenAngered',
    author_email='anonovezgame@tutanota.com',
    url='https://https://github.com/KotenAngered/SimpleGoogleSearch-PY',
    packages=find_packages(include=['googlesrch.py']),
    install_requires=[
        'gsearchlib',
        'pprintpp',
        'colorama',
        'urllib.request',
        'rich',
        'webbrowser',
        'json'
    ]
)
