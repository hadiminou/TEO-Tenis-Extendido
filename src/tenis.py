from typing import*
from datetime import datetime, date, timedelta
import csv
from collections import defaultdict, Counter

Parcial = NamedTuple('Parcial', 
                [('juegos_j1',int),
                 ('juegos_j2',int)])
PartidoTenis = NamedTuple('PartidoTenis', 
                [('fecha',datetime.date), 
                 ('jugador1',str), 
                 ('jugador2',str), 
                 ('superficie',str), 
                 ('resultado', List[Parcial]), 
                 ('errores_nf1',int), 
                 ('errores_nf2',int)])

def parsea_set(resultado:str)->tuple[Parcial]:
    parcial=resultado.split("-")
    return (Parcial(int(parcial[0]), int(parcial[1])))

def lee_partidos_tenis(ruta_fichero:str)->list[PartidoTenis]:
    lista_partido = list()
    resultado = list()
    with open(ruta_fichero, 'rt', encoding = "utf-8") as f:
        lector = csv.reader(f, delimiter = ';')
        for fecha, jugador1, jugador2, superficie, resultado1, resultado2, resultado3, errores_nf1,\
            errores_nf2 in lector:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date()
            resultado = [parsea_set(resultado1), parsea_set(resultado2), parsea_set(resultado3)]
            errores_nf1 = int(errores_nf1)
            errores_nf2 = int(errores_nf2)
            lista_partido.append(PartidoTenis(fecha, jugador1, jugador2, superficie, resultado,\
                                            errores_nf1, errores_nf2))
    return lista_partido

def partido_menos_errores(partidos:list[PartidoTenis])->list[PartidoTenis]:
    return min(partidos, key = lambda e:e.errores_nf1+e.errores_nf2)

def jugador_mas_partido(partidos:list[PartidoTenis])->tuple[str, int]:
    lista_jugador = list()
    for i in partidos:
        lista_jugador.append(i.jugador1)
        lista_jugador.append(i.jugador2)
    dic_jugador = Counter(lista_jugador)
    return max(dic_jugador.items(), key = lambda e:e[1])

def ganador(partido:tuple[PartidoTenis])->str:
    contador1, contador2 = 0, 0
    for juego in partido.resultado:
        if juego.juegos_j1 > juego.juegos_j2:
            contador1+=1
        if juego.juegos_j1 < juego.juegos_j2:
            contador2+=1
    if contador1 > contador2:
        res = partido.jugador1
    else:
        res = partido.jugador2
    return res

def tenista_mas_victorias(partidos:list[PartidoTenis], fecha1:date=None, fecha2:date=None)->str:
    dic_ganador = defaultdict(int)
    for i in partidos:
        if (fecha1 == None or fecha1 <= i.fecha) and (fecha2 == None or i.fecha <= fecha2):
            dic_ganador[ganador(i)]+=1
    return max(dic_ganador.items(), key = lambda e:e[1])
        
def media_errores_por_jugador(partidos:list[PartidoTenis])->list[tuple[str, float]]:
    dic_jugador = defaultdict(list)
    dic_res = defaultdict(float)
    for i in partidos:
        dic_jugador[i.jugador1].append(i.errores_nf1)
        dic_jugador[i.jugador2].append(i.errores_nf2)
    for c,v in dic_jugador.items():
        dic_res[c] = sum(v)/len(v)
    return sorted(dic_res.items(), key = lambda e:e[1])

def jugadores_mayor_porcentaje_victorias(partidos:list[PartidoTenis])->list[tuple[str, float]]:
    dic_gana = defaultdict(list)
    res = dict()
    for i in partidos:
        if i.jugador1 == ganador(i):
            dic_gana[i.jugador1].append(1)
            dic_gana[i.jugador2].append(0)
        else:
            dic_gana[i.jugador2].append(1)
            dic_gana[i.jugador1].append(0)
    for c,v in dic_gana.items():
        res[c] = sum(v)/len(v)
    return sorted(res.items(), key = lambda e:e[1], reverse = True)
    
def n_tenistas_con_mas_errores(partidos:list[PartidoTenis], num_jugador:int=None)->[tuple[str, int]]:
    dic_errores = defaultdict(int)
    for i in partidos:
        dic_errores[i.jugador1]+=i.errores_nf1
        dic_errores[i.jugador2]+=i.errores_nf2
    if num_jugador == None: 
        return sorted(dic_errores.items(), key = lambda e:e[1], reverse = True)
    else:
        return sorted(dic_errores.items(), key = lambda e:e[1], reverse = True)[:num_jugador]
    
def fecha_ordenadas_por_jugador(partidos:list[PartidoTenis])->dict[str,list[date]]:
    dic_fechas=defaultdict(list)
    res = dict()
    for i in partidos:
        dic_fechas[i.jugador1].append(i.fecha)
        dic_fechas[i.jugador2].append(i.fecha)
    for c,v in dic_fechas.items():
        res[c] = sorted(v)
    return res

def num_partidos_nombre(partidos:list[PartidoTenis], nombre:str)->dict[str, tuple[int, int]]:
    dic_superficie = defaultdict(list)
    dic_juegos = defaultdict(int)
    dic_ganador = defaultdict(list)
    dic_ganas = defaultdict(int)
    for i in partidos:
        if nombre == i.jugador1 or nombre == i.jugador2:
            dic_juegos[(i.superficie, i.jugador1)]+=1
            dic_juegos[(i.superficie, i.jugador2)]+=1
            dic_ganador[(i.superficie, i.jugador1)].append(ganador(i))
            dic_ganador[(i.superficie, i.jugador2)].append(ganador(i))
    for c,v in dic_ganador.items():
        for nom in v:
            if nombre not in v:
                dic_ganas[c]=0
            elif nom == nombre:
                dic_ganas[c]+=1
    for c,v in dic_juegos.items():
        if c[1] == nombre:
            dic_superficie[c]=(dic_juegos.get(c), dic_ganas.get(c))
    return dic_superficie

def num_partidos_nombre2(partidos:list[PartidoTenis], nombre:str)->dict[str, tuple[int, int]]:
    dic = defaultdict(int)
    for i in partidos:
        if i.jugador1 == nombre and ganador(i) == i.jugador1:
            dic[i.superficie] += 1
        if i.jugador2 == nombre and ganador(i) == i.jugador2:
            dic[i.superficie] += 1
    return dic

def num_tenistas_distintos_por_superficie(partidos:list[PartidoTenis])->dict[str, int]:
    dic_jugadores = defaultdict(set)
    dic_res = defaultdict(int)
    for i in partidos:
        dic_jugadores[i.superficie].add(i.jugador1)
        dic_jugadores[i.superficie].add(i.jugador2)
    for c,v in dic_jugadores.items():
        dic_res[c]=len(v)
    return dic_res

def superficie_con_mas_tenistas_distintos(partidos:list[PartidoTenis])->tuple[str, int]:
    dic_superficie = defaultdict(set)
    dic_res = dict()
    for i in partidos:
        dic_superficie[i.superficie].add(i.jugador1)
        dic_superficie[i.superficie].add(i.jugador2)
    for c,v in dic_superficie.items():
        dic_res[c] = len(v)
    return max(dic_res.items(), key = lambda e:e[1])

def mas_errores_por_jugador(partidos:list[PartidoTenis])->dict[str, list]:
    dic_errores = defaultdict(list)
    dic_res = dict()
    for i in partidos:
        dic_errores[i.jugador1].append((i.errores_nf1, PartidoTenis(i.fecha, i.jugador1, i.jugador2,\
                                            i.superficie, i.resultado, i.errores_nf1, i.errores_nf2)))
        dic_errores[i.jugador2].append((i.errores_nf2, PartidoTenis(i.fecha, i.jugador1, i.jugador2,\
                                            i.superficie, i.resultado, i.errores_nf1, i.errores_nf2)))
    for c,v in dic_errores.items():
        dic_res[c] = max(v, key = lambda e:e[0])
    return dic_res

def partido_mas_errores_por_mes(partidos:list[PartidoTenis], superficies:list[str]=None)->dict[date.month,\
                                                                            tuple[date, str, str]]:
    dic_mes = defaultdict(list)
    dic_res = dict()
    for i in partidos:
        if superficies == None or i.superficie in superficies:
            dic_mes[i.fecha.month].append((i.errores_nf1+i.errores_nf2,\
                                        (i.fecha, i.jugador1, i.jugador2)))
    for c,v in dic_mes.items():
        dic_res[c] = max(v, key = lambda e:e[0])
    return dic_res

def n_partidos_mas_errores_por_jugador(partidos:list[PartidoTenis], num_partidos:int)->dict[str,\
                                                                                    list[PartidoTenis]]:
    dic_errores = defaultdict(list)
    dic_ordenado = dict()
    for i in partidos:
        dic_errores[i.jugador1].append(i)
        dic_errores[i.jugador2].append(i)
    for c,v in dic_errores.items():
        for j in v:
            if c == j[1]:
                dic_ordenado[c] = sorted(v, key = lambda e:e[5], reverse = True)[:num_partidos]
            if c == j[2]:
                dic_ordenado[c] = sorted(v, key = lambda e:e[6], reverse = True)[:num_partidos]
    return dic_ordenado

def mayor_numero_dias_sin_jugar(partidos:list[PartidoTenis], jugador:str)->int:
    res = [i.fecha for i in partidos if (i.jugador1 or i.jugador2) == jugador]
    if len(res) == 0:
        return None
    res.sort()
    diferencias = [res[i+1] - res[i] for i in range(len(res)-1)]
    return (max(diferencias).days)

def mayor_numero_dias_sin_jugar2(partidos:list[PartidoTenis], jugador:str)->int:
    dic_fechas = defaultdict(list)
    dic_ordenado = dict()
    for i in partidos:
        if jugador == i.jugador1:
            dic_fechas[i.jugador1].append(i.fecha)
        if jugador == i.jugador2:
            dic_fechas[i.jugador2].append(i.fecha)
    for c,v in dic_fechas.items():
        dic_ordenado[c] = sorted(v)
    indice = 0
    res = 0
    lista2 = list()
    for c,v in dic_ordenado.items():
    #    lista2.append((v[indice+1]-v[indice]).days)
        if (v[indice+1]-v[indice]).days > res:
            res = (v[indice+1]-v[indice]).days
        indice+=1
    #return max(lista2)
    return res