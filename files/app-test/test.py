import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import ../app-python/lancement_QCM.py as lance_QCM

def test_get_nom():
    assert lance_QCM.hello('lucie') == 'Hello lucie'
