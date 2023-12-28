import gzip
import json
import ast
import numpy as np
import pandas as pd


def leer_archivo(path):
    try:
        return leer_archivo_metodo_uno(path)
    except Exception as error:
        return leer_archivo_metodo_dos(path)


def leer_archivo_metodo_uno(path):
    array_dict = []
    with gzip.open(path, "r") as file:
        for line in file:
            object_json = json.loads(line)
            array_dict.append(object_json)
    df = pd.DataFrame(array_dict)
    return df


def leer_archivo_metodo_dos(path):
    array_dict = []
    with gzip.open(path, "r") as file:
        for line in file:
            decoded_line = line.decode("utf-8")
            array_dict.append(ast.literal_eval(decoded_line))
    df = pd.DataFrame(array_dict)
    return df
