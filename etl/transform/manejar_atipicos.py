import matplotlib.pyplot as plt
import seaborn as sns


def eliminar_outliers(df, columna):
    data = df[columna]
    plt.subplots(figsize=(12, 4))
    sns.boxplot(x=columna, data=df)
    sns.stripplot(x=columna, data=df, color="black", size=6, jitter=True)
    plt.show()

    estadisticas_descriptivas = data.describe()
    q1 = estadisticas_descriptivas["25%"]
    q3 = estadisticas_descriptivas["75%"]
    iqr = q3 - q1
    whisker_inferior = q1 - 1.5 * iqr
    whisker_superior = q3 + 1.5 * iqr
    df_filtrado = df[
        (df[columna] >= whisker_inferior) & (df[columna] <= whisker_superior)
    ]

    # configurar la apariencia del grafico
    sns.set(style="whitegrid")

    # crear un histograma
    plt.figure(figsize=(11, 4))
    sns.histplot(df_filtrado[columna], kde=True, color="skyblue", bins=30)
    plt.title(f"Distribución de {columna}")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.show()

    return df_filtrado
