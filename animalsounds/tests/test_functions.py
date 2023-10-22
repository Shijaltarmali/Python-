import pytest
import animalsounds.dog as d
import animalsounds.cat as c

def test_doghi():
    dogres = d.makesound()
    assert isinstance(dogres, str) 

def test_cathi():
    catres = c.makesound()
    assert isinstance(catres, str)

