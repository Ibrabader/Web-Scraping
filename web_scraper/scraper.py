import requests

URL='https://en.wikipedia.org/wiki/History_of_Mexico'
from bs4 import BeautifulSoup

def get_citations_needed_count(URL):
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    _Data= soup.find_all('a',title="Wikipedia:Citation needed")
    return len(_Data)

def get_citations_needed_report(URL):
    strArr=[]
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    _Data= soup.find_all('a',title="Wikipedia:Citation needed")
    for iarticle in _Data:
        strArr.append(iarticle.parent.parent.parent.text)
    return "\n".join(strArr)

if __name__=="__main__":
    print(get_citations_needed_count(URL))
    print(type(get_citations_needed_report(URL)))
