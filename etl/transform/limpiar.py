import numpy as np
import pandas as pd


def eliminar_filas_vacias(df):
    print("la cantidad de filas en el dataframe es:", df.shape[0])
    df.dropna(how="all", inplace=True)
    print("despues de eliminar las filas vacias es:", df.shape[0])


def eliminar_filas_por_celdas_vacias_en(df, columnas):
    print("la cantidad de filas en el dataframe es:", df.shape[0])
    df.dropna(subset=columnas, inplace=True)
    print("despues de eliminar las filas vacias es:", df.shape[0])


def eliminar_columnas_innecesarias(df, columns):
    df.drop(columns=columns, inplace=True)


def eliminar_filas_duplicadas(df):
    # solo puede hacerde en datos planos
    print("la cantidad de filas en el dataframe es:", df.shape[0])
    df = df[~df.duplicated()]
    print("despues de eliminar las filas repetidas es:", df.shape[0])
    return df
