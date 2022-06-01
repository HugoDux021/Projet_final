import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
import modules.applications as applications

def test_get_nom():
    app = applications.Application()
    assert app.get_version == "22.04" 