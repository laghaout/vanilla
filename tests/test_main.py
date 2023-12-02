# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 00:04:37 2023

@author: Amine Laghaout
"""

import myrepo.main as main

def test_add() -> None:
    result = main.add(number1=1, number2=-4)
    assert result == -3