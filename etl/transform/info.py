######################################################

import pandas as pd

def celdas_vacias (df):
    """
    retorna un informe, un dataframe, de las celdas en las columnas del dataframe
    """
    missing_number = df.isnull().sum()
    missing_percent = df.isnull().sum()/df.isnull().count()
    missing_values = pd.concat([missing_number, missing_percent], axis=1, keys=['Cantidad', 'Porcentaje'])
    return missing_values

######################################################

def ver_la_cantidad_de_celdas_vacias(df):
    print("la cantidad de  celdas vacias por columan en el dataframe es:")
    return df.isna().sum()


def mostrar_info_fila_key_value(df, row):
    # colocar en nombre de las columnas en un array
    columnas = df.columns
    array_columnas = []
    for i in columnas:
        array_columnas.append(i)
    # colocar los valores de la fila en un array
    array_valores = []
    for i in df.iloc[row]:
        array_valores.append(i)
    # guardar la clave valor en un set
    my_set = set()
    for index, value in enumerate(array_columnas):
        my_set.add(f"{value} : {array_valores[index]}")
    print(my_set)


"""
obtener los clave tipos de la fila en especifica
el row se define mas arriva
"""


def mostrar_info_fila_key_type(df, row):
    # colocar en nombre de las columnas en un array
    columnas = df.columns
    array_columnas = []
    for i in columnas:
        array_columnas.append(i)
    # colocar los valores de la fila en un array
    array_typos = []
    for i in df.iloc[row]:
        array_typos.append(type(i))
        # guardar la clave valor en un set
    my_set = set()
    for index, value in enumerate(array_columnas):
        my_set.add(f"{value} : {array_typos[index]}")
    print(my_set)


"""
"""


def mostrar_info_key_types(df):
    columnas = df.columns
    for i in columnas:
        types = set()
        for j in df[i]:
            types.add(type(j))
        print(f"{i} - {types}")


"""
"""
"""
MOSTRAR LOS REGISTROS DONDE EL TIPO DE DATO COINCIDE
"""


def mostrar_info_coincidencia_tipo_celda_en_columna(df, columna, tipo_de_dato):
    for index, i in enumerate(df[columna]):
        if type(i) == tipo_de_dato:
            print(i, "===", index)


import numpy as np
import pandas as pd

# print(type(np.NaN))
# print(np.NaN)


def mostrar_coincidencia_tipo_celda_en_columna(df, columna, tipo):
    # es NaN
    # isinstance(i, float) and pd.isna(i)
    # es NaT
    # isinstance(i, pd._libs.tslibs.nattype.NaTType) and pd.isna(i)
    for index, i in enumerate(df[columna]):
        if type(i) == tipo or i == tipo:
            print(i, "=>", index)


# type(i) == dato or i == dato:
# mostrar_coincidencia_tipo_celda_en_columna(df_steam_game, "release_date", str)
# mostrar_coincidencia_tipo_celda_en_columna(df_steam_game, "release_date", "Soon..")
# mostrar_coincidencia_tipo_celda_en_columna(df_steam_game, "release_date", "January 2018")
# mostrar_coincidencia_tipo_celda_en_columna(df_steam_game, "release_date")
# isinstance(elemento, float) and pd.isna(elemento):

"""

"""


# obtener los clave valor unicos de una columna compuesta por un diccionario
def monstrar_info_columna_list_dict_key_values(df, columna):
    keys_and_values = set()
    for i in df[columna]:
        for j in i:
            for key, value in j.items():
                keys_and_values.add((key, type(value)))
    print(keys_and_values)


# mostrar valores que utiliza en la columna
def monstrar_valores_no_repetidos_en_columna(df, columna):
    values = set()
    for i in df[columna]:
        values.add(i)
    print(values)


import seaborn as sns
import matplotlib.pyplot as plt


def mostrar_frecuencia_de_valores_en_columnma(df, columna):
    # configurar el tema del grafico
    sns.set(style="whitegrid")

    # crear un histograma
    plt.figure(figsize=(11, 4))
    sns.histplot(df[columna], kde=True, color="skyblue", bins=30)
    plt.title(
        f"Distribución de la columna {columna}",
        fontdict={"color": "darkblue", "weight": "bold", "size": 16},
    )
    plt.xlabel(
        columna,
        fontdict={"color": "black", "weight": "bold", "size": 16},
    )
    plt.ylabel(
        "Frecuencia",
        fontdict={"color": "black", "weight": "bold", "size": 16},
    )
    plt.show()


import matplotlib.pyplot as plt


def mostrar_pie_de_valores_en_columnas(df, columna):
    conteo = df[columna].value_counts()
    porcentajes = df[columna].value_counts(normalize=True) * 100
    labels = [f"{i} - {conteo[i]} ({porcentajes[i]:.1f}%)" for i in conteo.index]

    fig, ax = plt.subplots()
    plt.pie(
        conteo,
        labels=labels,
        textprops={"fontsize": 11, "weight": "bold"},
    )
    plt.title(
        f"Distribución porcentual de la columna {columna}",
        fontdict={"family": "serif", "color": "darkblue", "weight": "bold", "size": 16},
    )
    plt.show()


"""ver valores no valido de fechas"""
import pandas as pd


def mostrar_fechas_no_validas(df, columna):
    fechas_validas = pd.to_datetime(df[columna], errors="coerce")
    valores_no_fecha = df[columna][~fechas_validas.notna()]
    print(valores_no_fecha)


def cualitativo_mostar_columna_y_variable_objetivo(df, columna1, columna2):
    import matplotlib.pyplot as plt
    import pandas as pd
    import seaborn as sns

    sns.set_palette("Paired")
    # mostrar los porcentajes"bright"

    df_auxiliar_1 = df.groupby([columna1, columna2]).size().reset_index(name="Cuenta")
    df_total_por_sexo = df.groupby(columna1).size().reset_index(name="Total")

    df_resultante = pd.merge(df_auxiliar_1, df_total_por_sexo, on=columna1)

    df_resultante["Porcentaje"] = (
        df_resultante["Cuenta"] / df_resultante["Total"]
    ) * 100

    print(df_resultante)

    #

    conteo = df[columna1].value_counts()
    porcentajes = df[columna1].value_counts(normalize=True) * 100
    labels = [f"{i} - {conteo[i]} ({porcentajes[i]:.1f}%)" for i in conteo.index]

    # crear una figura de dos filas y 1 columnas
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 8))

    # crear el primer grafico para la primera fila
    axes[0].pie(conteo, labels=labels, colors=sns.color_palette())
    axes[0].set_title(f"Distribución porcentual de la columna {columna1}",fontdict={"color": "darkblue", "weight": "bold", "size": 16},)
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.histplot(
        data=df,
        x=columna1,
        hue=columna2,
        multiple="stack",
        ax=axes[1],
    )
    axes[1].set_title(
        "Histograma",
        fontdict={"color": "darkblue", "weight": "bold", "size": 16},
    )
    axes[1].set_xlabel(
        columna1,
        fontdict={"color": "black", "weight": "bold", "size": 16},
    )
    axes[1].set_ylabel(
        "Frecuencia",
        fontdict={"color": "black", "weight": "bold", "size": 16},
    )
    plt.show()
