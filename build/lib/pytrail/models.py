from pytube import Search

from pytrail.exceptions import *

class Client:
    def __init__(self, name: str):
        self.name = name
        if self.name in ['', ' ']:
            raise InvalidNameException('the name you entered is invalid.')
        self.trailer = ''
        self.search()
    
    def search(self) -> str:
        s = Search(f'{self.name} trailer')
        res = s.results
        if res != []:
            url = str(res[0]).split(' ')
            id = url[2][url[2].index('=')+1:len(url[2])-1]
            self.trailer = f'https://www.youtube.com/watch/?v={id}'