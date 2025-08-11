# -*- coding: utf-8 -*-
"""
Created on Thu Jun  5 08:45:47 2025

@author: Amine Laghaout
"""

from fastapi import FastAPI, HTTPException
from main import Object, Input, Output

app = FastAPI()
obj = Object() 

@app.post("/yob", response_model=Output)
async def get_yob(input_data: Input):
    try:
        return obj.yob(input_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
