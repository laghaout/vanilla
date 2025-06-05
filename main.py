# -*- coding: utf-8 -*-
"""
Created on Tue Jun  3 15:03:47 2025

@author: Amine Laghaout
"""

import json
import os
from pydantic import BaseModel
from types import SimpleNamespace
from typing import Optional, Any, Dict

#%% Data models

class Input(BaseModel):
    age: int
    current_year: Optional[int] = 2025

class Output(BaseModel):
    yob: int

#%% Main object

class Object(BaseModel):
    params: dict | list = ["params.json"]

    def model_post_init(self, __context: Dict[str, Any]) -> None:
        """ Load the configuration parameters. """
        if isinstance(self.params, list):
            self.params = os.path.join(*self.params)
            with open(self.params) as file:
                self.params = json.load(file)
        assert isinstance(self.params, dict)
        self.params = SimpleNamespace(**self.params)

    def __call__(self):
        print("Parameters:")
        print(self.params)

    def yob(self, args: Input) -> Output:
        """ Mock subroutine """
        if args.age is None:
            raise ValueError("Age must be provided.")
        yob = args.current_year - args.age
        return Output(yob=yob)

def main():
    obj = Object()
    return obj

if __name__ == "__main__":
    main()
