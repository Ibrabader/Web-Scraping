from web_scraper import __version__
from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report,URL

# def test_version():
#     assert __version__ == '0.1.0'

def test_count_of_citations():
    excepted=5
    actual= get_citations_needed_count(URL)
    assert actual == excepted
    pass 
def test_preceding_passage():
    excepted= 0
    actual=get_citations_needed_report(URL)
    assert actual == excepted

