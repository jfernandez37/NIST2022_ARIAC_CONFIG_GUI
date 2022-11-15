from jsonschema import validate
from jsonschema import validators
import json
import yaml
def validateAriac(yamlFile, schemaFile):
    schema=yaml.full_load(schemaFile)  # reads in the schema file as a json file
    for i in schema['properties']:
        print(i)
    validate(yamlFile, schema)