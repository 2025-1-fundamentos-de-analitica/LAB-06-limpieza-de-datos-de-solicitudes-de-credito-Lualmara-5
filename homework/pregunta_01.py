"""
Escriba el codigo que ejecute la accion solicitada en la pregunta.
"""

def pregunta_01():

    import pandas as pd
    import os

    ruta_entrada = "files/input/solicitudes_de_credito.csv"
    datos = pd.read_csv(ruta_entrada, sep=";")

    datos.drop(columns=["Unnamed: 0"], inplace=True)

    datos.dropna(inplace=True)
    datos.drop_duplicates(inplace=True)

    datos[["dia", "mes", "anio"]] = datos["fecha_de_beneficio"].str.split("/", expand=True)

    años_cortos = datos["anio"].str.len() < 4
    datos.loc[años_cortos, ["dia", "anio"]] = datos.loc[años_cortos, ["anio", "dia"]].values

    datos["fecha_de_beneficio"] = datos["anio"] + "-" + datos["mes"] + "-" + datos["dia"]
    datos.drop(columns=["dia", "mes", "anio"], inplace=True)

    columnas_texto = ["sexo", "tipo_de_emprendimiento", "idea_negocio", "línea_credito"]
    datos[columnas_texto] = datos[columnas_texto].apply(
        lambda columna: columna.str.lower().replace(["-", "_"], " ", regex=True).str.strip()
    )

    datos["barrio"] = datos["barrio"].str.lower().replace(["-", "_"], " ", regex=True)

    datos["monto_del_credito"] = (
        datos["monto_del_credito"]
        .str.replace("[$, ]", "", regex=True)
        .str.strip()
    )

    datos["monto_del_credito"] = (
        pd.to_numeric(datos["monto_del_credito"], errors="coerce")
        .fillna(0)
        .astype(int)
    )

    datos["monto_del_credito"] = datos["monto_del_credito"].astype(str)

    datos.drop_duplicates(inplace=True)

    ruta_salida = "files/output"
    os.makedirs(ruta_salida, exist_ok=True)

    archivo_salida = os.path.join(ruta_salida, "solicitudes_de_credito.csv")
    datos.to_csv(archivo_salida, sep=";", index=False)

    return datos.head()

"""
    Realice la limpieza del archivo "files/input/solicitudes_de_credito.csv".
    El archivo tiene problemas como registros duplicados y datos faltantes.
    Tenga en cuenta todas las verificaciones discutidas en clase para
    realizar la limpieza de los datos.

    El archivo limpio debe escribirse en "files/output/solicitudes_de_credito.csv"
"""
