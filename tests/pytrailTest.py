from pytrail.__init__ import __version__
from pytrail.models import Client
from pytrail.exceptions import InvalidNameException

def TestVersion():
    assert __version__ == '0.1.0'

def TestClient():
    assert Client('red notice').trailer == 'https://www.youtube.com/watch/?v=T6l3mM7AWew'

def TestException():
    assert Client('') == InvalidNameException('the name you entered is invalid.')