#Imprima la tabla de posiciones luego de cada ronda.
#Cada ronda debe indicar quién fue el ganador (mayor puntaje).
#La cantidad de rondas ganadas se debe contabilizar.
#imprimir la tabla final con puntaje total acumulado, cantidad de rondas ganadas, mejor puntaje en una ronda y promedio por ronda.
# La tabla debe estar en orden decreciente por puntaje total.

#Calcular puntaje de un participante
def calcular_puntaje(jueces):
    return sum(jueces.values())

#Devuelve puntajes por cocinero
def procesar_ronda(ronda):
    resultados = {}
    
    for cocinero, jueces in ronda['scores'].items():
        resultados[cocinero] = calcular_puntaje(jueces)
    
    return resultados

#Determina ganador
def obtener_ganador(resultados):
    return max(resultados, key=resultados.get)

#Inicializar estadisticas
def inicializar_stats(cocineros):
    stats = {}
    
    for c in cocineros:
        stats[c] = {
            'total': 0,
            'rondas_ganadas': 0,
            'mejor_ronda': 0,
            'rondas': 0
        }
    
    return stats

#Actualizar estadisticas
def actualizar_stats(stats, resultados, ganador):
    for c, puntaje in resultados.items():
        stats[c]['total'] += puntaje
        stats[c]['rondas'] += 1
        
        if puntaje > stats[c]['mejor_ronda']:
            stats[c]['mejor_ronda'] = puntaje
    
    stats[ganador]['rondas_ganadas'] += 1
    
    
#Muestra ranking
def mostrar_ranking(stats):
    ranking = sorted(stats.items(), key=lambda x: x[1]['total'], reverse=True)
  
    for nombre, datos in ranking:
        print(nombre, datos['total'])