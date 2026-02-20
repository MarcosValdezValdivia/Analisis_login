#========================================
# Proyecto: Analisis de logs de login
# Autor: Valdez Valdivia Marcos Yamil
#========================================

import pandas as pd

def cargar_datos():
    tb = pd.read_csv("analisis_login/data/logs_login.csv")
    tb["timestamp"] = pd.to_datetime(tb["timestamp"])
    return tb


def operaciones(tb, fallos, exitos, mexico, españa, usa, brasil, argentina):
    porcentaje_fallo = len(fallos) / len(tb) * 100
    porcentaje_exitos = len(exitos) / len(tb) * 100
    porcentaje_mx = len(mexico) / len(tb) * 100
    porcentaje_es = len(españa) / len(tb) * 100
    porcentaje_usa = len(usa) / len(tb) * 100
    porcentaje_brs = len(brasil) / len(tb) * 100
    porcentaje_arg = len(argentina) / len(tb) * 100

    print("\nPorcentaje de fallos: {:.2f}%".format(porcentaje_fallo))
    print("\nPorcentaje de exitos: {:.2f}%".format(porcentaje_exitos))
    print("\nPorcentaje de intentos MX: {:.2f}%".format(porcentaje_mx))
    print("\nPorcentaje de intentos ES: {:.2f}%".format(porcentaje_es))
    print("\nPorcentaje de intentos USA: {:.2f}%".format(porcentaje_usa))
    print("\nPorcentaje de intentos BR: {:.2f}%".format(porcentaje_brs))
    print("\nPorcentaje de intentos ARG: {:.2f}%".format(porcentaje_arg))



def analisis(tb, fallos, exitos):
    print("\nTotal de registros:", len(tb))
    print("\nTotal de fallos:", len(fallos))
    print("\nTotal de exitos:", len(exitos))

    print("\nRegistros por usuario:")
    print(tb.groupby("usuario").size())

    print("\nIntentos por pais:")
    print(tb["pais"].value_counts())
    


def main():
    tb = cargar_datos()

    fallos = tb[tb["estado_login"] == "fallo"]
    exitos = tb[tb["estado_login"] == "exito"]
    mexico = tb[tb["pais"] == "Mexico"]
    españa = tb[tb["pais"] == "España"]
    usa = tb[tb["pais"] == "USA"]
    brasil = tb[tb["pais"] == "Brasil"]
    argentina = tb[tb["pais"] == "Argentina"]

    operaciones(tb, fallos, exitos, mexico, españa, usa, brasil, argentina)
    analisis(tb, fallos, exitos)


if __name__ == "__main__":
    main()