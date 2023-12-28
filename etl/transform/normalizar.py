def desanidar_dataframe(df, columnas):
  """
  aumentar el numero de registros del dataframe convirtiendo la columna que contiene como datos listas
  en multiples filas, donde en cada una hay un elemento de la lista y el resto de la informacion se repite
  hasta que el conjunto de filas y columnas sea el mismo que habia en registro original
  """
  for i in columnas:
    df = df.explode(i)
  return df.reset_index(drop=True)

# *****************************************************

import pandas as pd

def expandir_columna(df, columna):
  """
  Este es un comentario
  """
  df_columna_expandida = pd.json_normalize(df[columna])
  new_header = list(df.columns.append(df_columna_expandida.columns))
  new_df = pd.concat([df.reset_index(drop=True), df_columna_expandida], ignore_index=True, axis=1)
  new_df.columns = new_header
  new_df.drop(columna, axis=1, inplace=True)
  return new_df


def cambiar_nombre_a_una_columna(df, name, new_name):
    return df.rename(columns={name: new_name})


def reemplazar(df, columna, valor, new_valor):
    df[columna] = df[columna].apply(lambda x: new_valor if x == valor else x)


def unir_columnas_de_texto(df, columna1, columna2):
    df[columna1] = df[columna1].fillna("")
    df[columna2] = df[columna2].fillna("")

    def combinar_nombres(row):
        if row[columna1] == row[columna2]:
            return row[columna1]
        elif row[columna1] == "":
            return row[columna2]
        else:
            return row[columna1] + " " + row[columna2]

    df["name"] = df.apply(combinar_nombres, axis=1)
    df.drop(columns=[columna1, columna2], inplace=True)
