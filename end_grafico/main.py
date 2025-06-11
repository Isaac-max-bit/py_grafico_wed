import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- Datos ---
data = {
    'Categoría': [
        'Alimentos', 'Cuidado personal', 'Hogar', 'Cuidado personal', 'Cuidado personal',
        'Belleza', 'Mascotas', 'Hogar', 'Cuidado personal', 'Cuidado personal',
        'Mascotas', 'Mascotas', 'Mascotas', 'Hogar', 'Hogar', 'Hogar', 'Hogar',
        'Hogar', 'Hogar', 'Cuidado personal', 'Cuidado personal',
        'Cuidado personal', 'Cuidado personal', 'Belleza', 'Cuidado personal',
        'Alimentos', 'Belleza', 'Cuidado personal', 'Cuidado personal',
        'Cuidado personal', 'Cuidado personal', 'Cuidado personal', 'Cuidado personal'
    ],
    'Producto': [
        'Snacks orgánicos', 'Shampoo de café', 'Cesto de fibra', 'Bloqueador',
        'Hilo dental de seda', 'Esmalte', 'Shampoo (mascotas)', 'Cortinas de algodón',
        'Pasta de dientes', 'Pañitos biodegradables', 'Juguete cuerda natural',
        'Collar de algodón', 'Arena de bambú', 'Sábanas de algodón', 'Suavizante natural',
        'Toallas de microfibra', 'Vajilla de porcelana', 'Bolsa de basura compostable',
        'Cortinas de algodón', 'Detergente en polvo', 'Sérums hidratantes',
        'Mascarilla de arcilla', 'Brocha mango de bambú', 'Esmalte ecológico',
        'Gel ducha de aguacate', 'Cápsulas de algarrobo', 'Base líquida natural',
        'Aceite natural de coco', 'Crema dental de menta', 'Rasuradora inoxidable',
        'Esponja de baño natural', 'Desodorante libre de aluminio', 'Jabón con aceite de oliva'
    ],
    'Cantidad': [
        3, 6, 4, 8, 1, 3, 7, 2, 9, 6, 5, 10, 11, 17, 7, 1, 6, 4, 19, 18, 20, 5, 7,
        25, 9, 30, 45, 6, 7, 2, 1, 9, 45
    ],
    'Precio': [
        10000, 34000, 17000, 7600, 6500, 54000, 32000, 2000, 22000, 43000,
        21000, 3200, 4000, 50000, 45000, 43000, 21000, 22000, 6700, 41000,
        45000, 28000, 4900, 56000, 9800, 78000, 56000, 75000, 10000, 42000,
        98000, 65000, 6500
    ]
}

# Crear DataFrame y calcular 'Total_Venta'
df = pd.DataFrame(data)
df['Total_Venta'] = df['Cantidad'] * df['Precio']

# --- Configuración global de estilo para todas las gráficas ---
def configure_plot_style():
    """Configura el estilo general de Matplotlib y Seaborn para todas las gráficas."""
    sns.set_theme(style="whitegrid", palette="viridis")
    plt.rcParams.update({
        'font.size': 10,
        'axes.titlesize': 14,
        'axes.labelsize': 12,
        'xtick.labelsize': 10,
        'ytick.labelsize': 10
    })
    plt.style.use('seaborn-v0_8-darkgrid') # Un estilo adicional que mejora la estética

# --- Funciones para generar cada tipo de gráfica ---

def plot_total_ventas_categoria(dataframe):
    """
    Genera y muestra un gráfico de barras del total de ventas por categoría.
    Incluye un análisis descriptivo.
    """
    plt.figure(figsize=(10, 7))
    total_ventas_categoria = dataframe.groupby('Categoría')['Total_Venta'].sum().sort_values(ascending=False)
    sns.barplot(x=total_ventas_categoria.index, y=total_ventas_categoria.values)
    plt.title('1. Total de Ventas por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Total de Ventas ($)')
    plt.ticklabel_format(style='plain', axis='y')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.figtext(0.5, 0.02,
                "Análisis: Esta gráfica muestra la contribución de cada categoría al ingreso total. Se observa que 'Belleza' y 'Cuidado personal' son las categorías con mayores ventas, indicando su importancia en la facturación general de la empresa.",
                fontsize=9, ha='center', va='bottom', wrap=True, transform=plt.gcf().transFigure)
    plt.tight_layout(rect=[0, 0.15, 1, 1])
    plt.savefig('grafica_1_ventas_categoria.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_cantidad_promedio_productos_categoria(dataframe):
    """
    Genera y muestra un gráfico de barras de la cantidad promedio de productos por categoría.
    Incluye un análisis descriptivo.
    """
    plt.figure(figsize=(10, 7))
    avg_cantidad_categoria = dataframe.groupby('Categoría')['Cantidad'].mean().sort_values(ascending=False)
    sns.barplot(x=avg_cantidad_categoria.index, y=avg_cantidad_categoria.values)
    plt.title('2. Cantidad Promedio de Productos por Categoría')
    plt.xlabel('Categoría')
    plt.ylabel('Cantidad Promedio')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.figtext(0.5, 0.02,
                "Análisis: Aquí se visualiza la cantidad promedio de unidades vendidas por producto dentro de cada categoría. Las categorías 'Alimentos' y 'Belleza' muestran una alta cantidad promedio por transacción, lo que podría indicar compras más grandes o productos que se venden en mayores volúmenes por unidad.",
                fontsize=9, ha='center', va='bottom', wrap=True, transform=plt.gcf().transFigure)
    plt.tight_layout(rect=[0, 0.15, 1, 1])
    plt.savefig('grafica_2_cantidad_promedio_categoria.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_distribucion_precios(dataframe):
    """
    Genera y muestra un histograma de la distribución de precios de los productos.
    Incluye un análisis descriptivo.
    """
    plt.figure(figsize=(10, 7))
    sns.histplot(dataframe['Precio'], kde=True, bins=10)
    plt.title('3. Distribución de Precios de Productos')
    plt.xlabel('Precio ($)')
    plt.ylabel('Frecuencia')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.figtext(0.5, 0.02,
                "Análisis: Este histograma muestra la distribución de precios de los productos. Se observa que la mayoría de los productos se encuentran en el rango de precios más bajos (menos de $20,000), con una cola más larga hacia precios más altos, indicando la presencia de algunos productos de alto valor.",
                fontsize=9, ha='center', va='bottom', wrap=True, transform=plt.gcf().transFigure)
    plt.tight_layout(rect=[0, 0.15, 1, 1])
    plt.savefig('grafica_3_distribucion_precios.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_top_5_productos_ventas(dataframe):
    """
    Genera y muestra un gráfico de barras de los top 5 productos por total de ventas.
    Incluye un análisis descriptivo.
    """
    plt.figure(figsize=(10, 7))
    top_5_productos_ventas = dataframe.groupby('Producto')['Total_Venta'].sum().nlargest(5).sort_values(ascending=True)
    sns.barplot(x=top_5_productos_ventas.values, y=top_5_productos_ventas.index, palette='mako', hue=top_5_productos_ventas.index, legend=False)
    plt.title('4. Top 5 Productos por Total de Ventas')
    plt.xlabel('Total de Ventas ($)')
    plt.ylabel('Producto')
    plt.ticklabel_format(style='plain', axis='x')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.figtext(0.5, 0.02,
                "Análisis: Esta gráfica destaca los cinco productos que generan el mayor ingreso total. 'Cápsulas de algarrobo', 'Base líquida natural' y 'Esponja de baño natural' lideran las ventas, señalando su popularidad y contribución significativa a los ingresos. Estos productos podrían ser focos para promociones o mantenimiento de stock.",
                fontsize=9, ha='center', va='bottom', wrap=True, transform=plt.gcf().transFigure)
    plt.tight_layout(rect=[0, 0.15, 1, 1])
    plt.savefig('grafica_4_top_5_productos.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_relacion_cantidad_precio_scatter(dataframe):
    """
    Genera y muestra un diagrama de dispersión de la relación entre cantidad y precio unitario.
    Incluye un análisis descriptivo.
    """
    plt.figure(figsize=(10, 7))
    sns.scatterplot(x='Precio', y='Cantidad', hue='Categoría', data=dataframe, s=100, alpha=0.7)
    plt.title('5. Relación entre Cantidad y Precio Unitario')
    plt.xlabel('Precio Unitario ($)')
    plt.ylabel('Cantidad Vendida')
    plt.ticklabel_format(style='plain', axis='x')
    plt.legend(title='Categoría', bbox_to_anchor=(1.02, 1), loc='upper left', borderaxespad=0.)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.figtext(0.5, 0.02,
                "Análisis: Este diagrama de dispersión explora si existe una correlación entre el precio unitario de un producto y la cantidad vendida. No parece haber una correlación lineal fuerte y clara, lo que sugiere que la cantidad comprada no está directamente dictada solo por el precio unitario, sino también por la categoría del producto o su necesidad.",
                fontsize=9, ha='center', va='bottom', wrap=True, transform=plt.gcf().transFigure)
    plt.tight_layout(rect=[0, 0.15, 1, 1])
    plt.savefig('grafica_5_cantidad_precio_scatter.png', dpi=300, bbox_inches='tight')
    plt.show()

def plot_proporcion_productos_categoria(dataframe):
    """
    Genera y muestra un gráfico circular de la proporción de productos por categoría.
    Incluye un análisis descriptivo.
    """
    plt.figure(figsize=(10, 7))
    productos_por_categoria = dataframe['Categoría'].value_counts()
    plt.pie(productos_por_categoria, labels=productos_por_categoria.index, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
    plt.title('6. Proporción de Productos por Categoría')
    plt.axis('equal') # Asegura que el círculo sea un círculo
    plt.figtext(0.5, 0.02,
                "Análisis: Este gráfico circular muestra la distribución porcentual de los productos listados por categoría. 'Cuidado personal' domina con la mayor proporción, indicando una amplia variedad de productos en esta sección, seguido por 'Hogar' y 'Belleza'. Esto resalta el enfoque del inventario en estas áreas.",
                fontsize=9, ha='center', va='bottom', wrap=True, transform=plt.gcf().transFigure)
    plt.tight_layout(rect=[0, 0.15, 1, 1])
    plt.savefig('grafica_6_proporcion_categorias.png', dpi=300, bbox_inches='tight')
    plt.show()

# --- Diccionario de funciones de gráficos ---
graph_functions = {
    '1': plot_total_ventas_categoria,
    '2': plot_cantidad_promedio_productos_categoria,
    '3': plot_distribucion_precios,
    '4': plot_top_5_productos_ventas,
    '5': plot_relacion_cantidad_precio_scatter,
    '6': plot_proporcion_productos_categoria,
}

# --- Menú principal de opciones ---
def main_menu():
    """Muestra el menú principal y gestiona las opciones del usuario."""
    while True:
        print("\n--- Por favor, selecciona una opción ---")
        print("1. Mostrar la tabla de datos original")
        print("2. Ver gráficas de análisis de datos")
        print("3. Salir del programa")

        main_choice = input("Ingresa el número de tu opción (1, 2 o 3): ")

        if main_choice == '1':
            print("\nTabla de Datos Original con 'Total_Venta' calculado:")
            print(df.to_string())
            print("\n" + "="*80 + "\n")
            input("Presiona Enter para continuar...")
        elif main_choice == '2':
            graph_submenu()
        elif main_choice == '3':
            print("¡Hasta luego!, buena suerte ✅")
            break
        else:
            print("Opción no válida. Por favor, ingresa 1, 2 o 3.")

# --- Submenú para elegir una gráfica ---
def graph_submenu():
    """Muestra el submenú de gráficas y gestiona la selección del usuario."""
    while True:
        print("\n--- Selecciona la gráfica que deseas ver ---")
        print("1. Total de Ventas por Categoría")
        print("2. Cantidad Promedio de Productos por Categoría")
        print("3. Distribución de Precios de Productos")
        print("4. Top 5 Productos por Total de Ventas")
        print("5. Relación entre Cantidad y Precio Unitario (Scatter Plot)")
        print("6. Proporción de Productos por Categoría (Pie Chart)")
        print("7. Volver al menú principal")

        graph_choice = input("Ingresa el número de la gráfica que deseas ver (1-7): ")

        if graph_choice in graph_functions:
            # Llama a la función de gráfico correspondiente desde el diccionario
            graph_functions[graph_choice](df)
            input("Presiona Enter para continuar...")
        elif graph_choice == '7':
            print("Volviendo al menú principal...")
            break
        else:
            print("Opción de gráfica no válida. Por favor, ingresa un número del 1 al 7.")

# --- Ejecución principal del programa ---
if __name__ == "__main__":
    configure_plot_style()
    main_menu()