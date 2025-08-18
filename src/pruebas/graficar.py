import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def graficar():
    # creo carpeta
    carpeta_dir = "images_test" 
    os.makedirs(carpeta_dir, exist_ok=True)

    #
    grafico_dispersion(os.path.join(carpeta_dir, "puntaje_vs_tiempo.png"))
    grafico_puntaje_total(os.path.join(carpeta_dir, "puntaje_total.png"))
    grafico_nivel_puntaje(os.path.join(carpeta_dir, "nivel_vs_puntaje.png"))
    grafico_lineas_eliminadas(os.path.join(carpeta_dir, "lineas_eliminadas.png"))
    grafico_consistencia(os.path.join(carpeta_dir, "consistencia.png"))
    grafico_piezas_lineas(os.path.join(carpeta_dir, "piezas_lineas.png"))
    heatmap(os.path.join(carpeta_dir, "heatmap.png"))

    #-----TABLAS-----------------------------------------------
    graficar_tabla("tabla_consistencia.csv",os.path.join(carpeta_dir, "tabla_consistencia.png"))
    graficar_tabla("tabla_promedio_eliminaciones.csv",os.path.join(carpeta_dir, "tabla_promedio_eliminaciones.png"))
    graficar_tabla("tabla_piezas_lineas.csv",os.path.join(carpeta_dir, "tabla_piezas_lineas.png"))
    graficar_tabla("tabla_promedio_metricas.csv",os.path.join(carpeta_dir, "tabla_promedio_metricas.png"))


def grafico_dispersion(imagen):
    # Cargar datos y calcular promedio por algoritmo
    df = pd.read_csv('resultados_algoritmos.csv', sep='|')
    df_prom = df.groupby('Algoritmo')[['Puntaje', 'Tiempo promedio']].mean().reset_index()

    # Colores y marcadores por algoritmo
    colores = {'Hill Climbing':'blue', 'Simulated Annealing':'green', 'Genetico':'red'}
    markers = {'Hill Climbing':'o', 'Simulated Annealing':'s', 'Genetico':'^'}

    plt.figure(figsize=(12, 6))
    for _, row in df_prom.iterrows():
        plt.scatter(row['Tiempo promedio'], row['Puntaje'],
                    color=colores[row['Algoritmo']],
                    marker=markers[row['Algoritmo']],
                    s=200)
        plt.text(row['Tiempo promedio'], row['Puntaje'] + 100, row['Algoritmo'], ha='center', fontweight='bold')

    plt.xlabel('Tiempo promedio de decisión (s)')
    plt.ylabel('Puntaje obtenido')
    plt.title('Comparación de Puntaje vs Tiempo por Algoritmo (promedio)', pad=20)
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(imagen)
    plt.close()

def grafico_puntaje_total(imagen):
    
    df = pd.read_csv("resultados_algoritmos.csv", sep='|')

    # Crear boxplot
    plt.figure(figsize=(12, 6))
    
    df.boxplot(column='Puntaje', by='Algoritmo', grid=False)
    plt.title('Distribución de Puntajes por Algoritmo')
    plt.suptitle("")
    # Etiquetas y título
    plt.xlabel('Algoritmo')
    plt.ylabel('Puntaje obtenido')
    

    # Guardar imagen
    plt.tight_layout()
    plt.savefig(imagen)
    plt.close()

def grafico_nivel_puntaje(imagen):
    df = pd.read_csv('resultados_algoritmos.csv', sep='|')

    # Calcular promedio por algoritmo
    df_prom = df.groupby('Algoritmo')[['Nivel', 'Puntaje']].mean().reset_index()

    # Crear gráfico
    plt.figure(figsize=(10, 6))
    colores = {'Hill Climbing':'blue', 'Simulated Annealing':'green', 'Genetico':'red'}

    for _, row in df_prom.iterrows():
        plt.scatter(row['Nivel'], row['Puntaje'], color=colores[row['Algoritmo']], s=200)
        plt.text(row['Nivel'], row['Puntaje'] + 200, row['Algoritmo'], ha='center', fontweight='bold')

    # Etiquetas y título
    plt.xlabel('Nivel alcanzado (promedio)')
    plt.ylabel('Puntaje obtenido (promedio)')
    plt.title('Nivel vs Puntaje por Algoritmo (promedio)')
    plt.grid(True)
    plt.tight_layout()

    # Guardar imagen
    plt.savefig(imagen)
    plt.close()

def grafico_lineas_eliminadas(imagen):
    # Cargar CSV
    df = pd.read_csv("tabla_promedio_eliminaciones.csv")

    # Seleccionar solo las columnas de interés
    tipos = ['Singles', 'Doubles', 'Triples', 'Tetrises']
    algoritmos = df.columns[1:]

    x = np.arange(len(algoritmos)) * 2  # posición de cada grupo de barras
    width = 0.3  # ancho de cada barra

    fig, ax = plt.subplots(figsize=(10,6))

    for i, tipo in enumerate(tipos):
        valores = df.loc[df['Métrica'] == tipo, algoritmos].values.flatten()
        ax.bar(x + i*width - (width*1.5), valores, width, label=tipo)
    
    ax.set_xlabel('Algoritmo')
    ax.set_ylabel('Promedio por partida')
    ax.set_title('Promedio de Eliminaciones por Tipo y Algoritmo')
    ax.set_xticks(x)
    ax.set_xticklabels(algoritmos)
    ax.legend(title='Tipo de Eliminación')

    plt.tight_layout()
    plt.savefig(imagen)
    plt.close()

def grafico_consistencia(imagen):

    df = pd.read_csv("tabla_consistencia.csv")

    df_pivot = df.pivot(index='Algoritmo', columns='Métrica', values='Cv%').reset_index()

    # Limpio % y paso a float (si vienen con % en texto)
    df_pivot['Puntaje'] = df_pivot['Puntaje'].str.rstrip('%').astype(float)
    df_pivot['Lineas eliminadas'] = df_pivot['Lineas eliminadas'].str.rstrip('%').astype(float)

    # Gráfico de dispersión CV Puntaje vs CV Líneas eliminadas
    plt.figure(figsize=(8,6))
    plt.scatter(df_pivot['Puntaje'], df_pivot['Lineas eliminadas'], s=100)

    for i, row in df_pivot.iterrows():
        plt.text(row['Puntaje'] + 0.1, row['Lineas eliminadas'], row['Algoritmo'])

    plt.xlabel('CV Puntaje (%)')
    plt.ylabel('CV Líneas eliminadas (%)')
    plt.title('Consistencia por Algoritmo (Coeficiente de Variación)')
    plt.grid(True)

    # Guardar gráfico
    plt.savefig(imagen)
    plt.close()
    
def grafico_piezas_lineas(imagen):

    df_piezas_lineas = pd.read_csv("tabla_piezas_lineas.csv")

    df_ordenado = df_piezas_lineas.sort_values(by='Lineas/pieza', ascending=False)

    plt.figure(figsize=(8,6))
    sns.barplot(data=df_ordenado, x='Algoritmo', y='Lineas/pieza', palette='viridis')
    plt.title('Líneas/Pieza por Algoritmo')
    plt.ylabel('Líneas por Pieza')
    plt.xlabel('Algoritmo')
    
    # Guardar gráfico
    plt.savefig(imagen)
    plt.close()
    
def heatmap(imagen):
    df_promedio_metricas = pd.read_csv("tabla_promedio_metricas.csv")
    df_heatmap = df_promedio_metricas.set_index('Métrica')
    
    plt.figure(figsize=(14,4))
    sns.heatmap(df_heatmap, annot=True, cmap='coolwarm', fmt=".4f")
    plt.title('Matriz de Métricas por Algoritmo')
    plt.ylabel('Métrica')
    plt.xlabel('Algoritmo')
    
    # Guardar gráfico
    plt.savefig(imagen)
    plt.close()
    
#-------------------TABLAS-----------------------------
def graficar_tabla(csv_path, imagen):
    # Leer CSV
    df = pd.read_csv(csv_path)

    # Crear figura
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.axis('off')  # quitar ejes

    # Dibujar tabla
    tabla = ax.table(cellText=df.values, colLabels=df.columns, loc='center')

    tabla.auto_set_font_size(False)
    tabla.set_fontsize(10)
    tabla.scale(1.2, 1.2)  # ajustar tamaño
    tabla.auto_set_column_width(col=list(range(len(df.columns))))


    plt.savefig(imagen, dpi=300, bbox_inches="tight")
    plt.show()
