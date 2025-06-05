from lib.includes_todo import *

def test_TODO_present():
    assert includes_todo('call the dentist #TODO') == True

#not present

def test_TODO_not_present():
    assert includes_todo('call the dentist') == False

# test for lower case todo

def test_TODO_lower_case():
    assert includes_todo('call the dentist #todo') == True
