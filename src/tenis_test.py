from tenis import*
from datetime import date

def test_lee_partidos_tenis(datos:list[PartidoTenis]):
    print("\ntest_lee_partidos_tenis")
    print(f"\nNumero total de partidos leidos: {len(datos)}")
    print("\nMostrando los tres primeros registros leidos:")
    for i in range(0, 3, 1):
        print(f"{i+1}-{datos[i]}")

def test_partido_menos_errores(datos:list[PartidoTenis]):
    print("\ntest_partido_menos_errores")
    print(f"el partido con menos errores es: {partido_menos_errores(datos)}")

def test_jugador_mas_partido(datos:list[PartidoTenis]):
    print("test_jugador_mas_partido")
    print(f"El jugador que ha jugado más partidos es {jugador_mas_partido(datos)[0]},\
           con un total de {jugador_mas_partido(datos)[1]} partidos")
    
def test_tenista_mas_victorias(datos:list[PartidoTenis]):
    print("\ntest_tenista_mas_victorias")
    fecha1 = None
    fecha2 = None
    print(f"El tenista con más victorias entre las fechas {fecha1} y {fecha2} es\
        {tenista_mas_victorias(datos)}")
    fecha22 = date(2020,1,1)
    print(f"El tenista con más victorias entre las fechas {fecha1} y {fecha22} es\
        {tenista_mas_victorias(datos,fecha2 = fecha22)}")
    print(f"El tenista con más victorias entre las fechas {fecha22} y {fecha2} es\
        {tenista_mas_victorias(datos, fecha22)}")
    fecha11 = date(2013,1,1)
    print(f"El tenista con más victorias entre las fechas {fecha11} y {fecha22} es\
        {tenista_mas_victorias(datos, fecha11, fecha22)}")
    
def test_media_errores_por_jugador(datos:list[PartidoTenis]):
    print("\ntest_media_errores_por_jugador")
    print("La media de errores por jugador, de menos a más errores es:") 
    contador = 1
    for i in media_errores_por_jugador(datos):
        print(f"{contador}-{i}")
        contador+=1

def test_jugadores_mayor_porcentaje_victorias(datos:list[PartidoTenis]):
    print("\ntest_jugadores_mayor_porcentaje_victorias")
    contador = 1
    for i in jugadores_mayor_porcentaje_victorias(datos):
        print(f"{contador}-{i}")
        contador+=1

def test_n_tenistas_con_mas_errores(datos:list[PartidoTenis]):
    print("\ntest_n_tenistas_con_mas_errores")
    print("\nn_tenistas_con_mas_errores, n=None")
    contador = 1
    for i in n_tenistas_con_mas_errores(datos):
        print(f"{contador}-{i}")
        contador+=1
    n = 5
    print(f'\nn_tenistas_con_mas_errores, n={n}')
    contador = 1
    for i in n_tenistas_con_mas_errores(datos, 5):
        print(f"{contador}-{i}")
        contador+=1

def test_fecha_ordenadas_por_jugador(datos:list[PartidoTenis]):
    print("\ntest_fecha_ordenadas_por_jugador")
    print("\nLas fechas de cada partido por jugador son:")
    for c,v in fecha_ordenadas_por_jugador(datos).items():
        print(f"\n{c} ---> {v}")

def test_num_partidos_nombre(datos:list[PartidoTenis]):
    print("\ntest_num_partidos_nombre")
    jugador = "Rafael Nadal"
    print(f"Los partidos jugados y ganados por superficie de {jugador} son")
    for c,v in num_partidos_nombre(datos, jugador).items():
        print(f"{c[0]} ---> {v}")
    jugador = "Carlos Alcaraz"
    print(f"Los partidos jugados y ganados por superficie de {jugador} son")
    for c,v in num_partidos_nombre(datos, jugador).items():
        print(f"{c[0]} ---> {v}")

def test_num_tenistas_distintos_por_superficie(datos:list[PartidoTenis]):
    print("\ntest_num_tenistas_distintos_por_superficie")
    print("El número de tenistas distintos segun cada superficie es")
    for c,v in num_tenistas_distintos_por_superficie(datos).items():
        print(f"{c} ---> {v}")

def test_superficie_con_mas_tenistas_distintos(datos:list[PartidoTenis]):
    print("\ntest_superficie_con_mas_tenistas_distintos")
    print(f"la superficie en la que juegan un mayor numero de jugadores distintos es\
        {superficie_con_mas_tenistas_distintos(datos)[0]} y\
            {superficie_con_mas_tenistas_distintos(datos)[1]} jugadores han jugado en esa superficie")
    
def test_mas_errores_por_jugador(datos:list[PartidoTenis]):
    print("\ntest_mas_errores_por_jugador")
    print("El partido con mas errores por cada jugador es")
    for c,v in mas_errores_por_jugador(datos).items():
        print(f"\n{c} ---> {v[1]}")

def test_partido_mas_errores_por_mes(datos:list[PartidoTenis]):
    print("\ntest_partido_mas_errores_por_mes")
    superficies = ["Sintética"]
    print(f"Los partidos con mas errores para las superificies {superficies} son")
    for c,v in partido_mas_errores_por_mes(datos, superficies).items():
        print(f"{c} ---> {v[1]}")
    superficies=['Sintética', 'Tierra']
    print(f"\nLos partidos con mas errores para las superificies {superficies} son")
    for c,v in partido_mas_errores_por_mes(datos, superficies).items():
        print(f"{c} ---> {v[1]}")
    superficies=None
    print(f"\nLos partidos con mas errores para las superificies {superficies} son")
    for c,v in partido_mas_errores_por_mes(datos, superficies).items():
        print(f"{c} ---> {v[1]}")

def test_n_partidos_mas_errores_por_jugador(datos:list[PartidoTenis]):
    print("\ntest_n_partidos_mas_errores_por_jugador")
    numero = 3
    print(f"Los {numero} partidos con mas errores para los jugadores son")
    for c,v in n_partidos_mas_errores_por_jugador(datos, numero).items():
        print(f"{c} ---> {v}")

def test_mayor_numero_dias_sin_jugar(datos:list[PartidoTenis]):
    print("\ntest_mayor_numero_dias_sin_jugar")
    jugador = "Carlos Alcaraz"
    print(f"El mayor numero de dias que el jugador {jugador} ha estado sin jugar es\
        {mayor_numero_dias_sin_jugar(datos, jugador)}")

if __name__=="__main__":
    datos = lee_partidos_tenis("Proyectos Python\TEO-Tenis-Extendido-main\data\Tenis.csv")
    #test_lee_partidos_tenis(datos)
    #test_partido_menos_errores(datos)
    #test_jugador_mas_partido(datos)
    #test_tenista_mas_victorias(datos)
    #test_media_errores_por_jugador(datos)
    #test_jugadores_mayor_porcentaje_victorias(datos)
    #test_n_tenistas_con_mas_errores(datos)
    #test_fecha_ordenadas_por_jugador(datos)
    #test_num_partidos_nombre(datos)
    #test_num_tenistas_distintos_por_superficie(datos)
    #test_superficie_con_mas_tenistas_distintos(datos)
    #test_mas_errores_por_jugador(datos)
    #test_partido_mas_errores_por_mes(datos)
    #test_n_partidos_mas_errores_por_jugador(datos)
    #test_mayor_numero_dias_sin_jugar(datos)