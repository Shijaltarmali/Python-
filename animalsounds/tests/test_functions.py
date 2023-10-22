import pytest
import dog as d
import cat as c

def test_doghi():
    dogres = d.makesound()
    assert isinstance(dogres, str) 

def test_cathi():
    catres = c.makesound()
    assert isinstance(catres, str)