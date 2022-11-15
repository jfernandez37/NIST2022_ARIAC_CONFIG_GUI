import tkinter as tk
from tkinter import filedialog
import tkinter.ttk as ttk
import math
import platform
import os.path
from os import chdir, path
import os
from pathlib import Path
from functools import partial
from jsonschema import validate
from jsonschema import validators
import json

def validateAriac(yamlFile, schemaFile):
    schema=json.load(schemaFile)  # reads in the schema file as a json file
    for i in schema['properties']:
        print(i)
    