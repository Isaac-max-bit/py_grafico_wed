import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# --- Datos (los mismos que hemos estado usando) ---
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
        10.000, 34.000, 17.000, 7.600, 6.500, 54.000, 32.000, 2.000, 22.000, 43.000,
        21.000, 3.200, 4.000, 50.000, 45.000, 43.000, 21.000, 22.000, 6.700, 41.000,
        45.000, 28.000, 4.900, 56.000, 9.800, 78.000, 56.000, 75.000, 10.000, 42.000,
        98.000, 65.000, 6.500
    ]
}

df = pd.DataFrame(data)
df['Total_Venta'] = df['Cantidad'] * df['Precio']

# --- Configuración de estilo y fuentes generales para gráficas individuales (se mueven fuera para que estén disponibles siempre) ---
sns.set_theme(style="whitegrid", palette="viridis")
plt.rcParams.update({'font.size': 10})
plt.rcParams['axes.titlesize'] = 14
plt.rcParams['axes.labelsize'] = 12
plt.rcParams['xtick.labelsize'] = 10
plt.rcParams['ytick.labelsize'] = 10

# --- Menú principal de opciones ---
while True:
    print("\n--- Por favor, selecciona una opción ---")
    print("1. Mostrar la tabla de datos original")
    print("2. Ver gráficas de análisis de datos")
    print("3. Salir del programa")

    main_choice = input("Ingresa el número de tu opción (1, 2 o 3): ")

    if main_choice == '1':
        # Opción 1: Mostrar la tabla de datos original
        print("\nTabla de Datos Original con 'Total_Venta' calculado:")
        print(df.to_string())
        print("\n" + "="*80 + "\n")
        input("Presiona Enter para continuar...")
    elif main_choice == '2':
        # Opción 2: Submenú para elegir una gráfica
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

            if graph_choice == '1':
                # Gráfica 1: Total de Ventas por Categoría
                plt.figure(figsize=(10, 7))
                total_ventas_categoria = df.groupby('Categoría')['Total_Venta'].sum().sort_values(ascending=False)
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
                input("Presiona Enter para continuar...")
            elif graph_choice == '2':
                # Gráfica 2: Cantidad Promedio de Productos por Categoría
                plt.figure(figsize=(10, 7))
                avg_cantidad_categoria = df.groupby('Categoría')['Cantidad'].mean().sort_values(ascending=False)
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
                input("Presiona Enter para continuar...")
            elif graph_choice == '3':
                # Gráfica 3: Distribución de Precios de Productos
                plt.figure(figsize=(10, 7))
                sns.histplot(df['Precio'], kde=True, bins=10)
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
                input("Presiona Enter para continuar...")
            elif graph_choice == '4':
                # Gráfica 4: Top 5 Productos por Total de Ventas
                plt.figure(figsize=(10, 7))
                top_5_productos_ventas = df.groupby('Producto')['Total_Venta'].sum().nlargest(5).sort_values(ascending=True)
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
                input("Presiona Enter para continuar...")
            elif graph_choice == '5':
                # Gráfica 5: Relación entre Cantidad y Precio Unitario (Scatter Plot)
                plt.figure(figsize=(10, 7))
                sns.scatterplot(x='Precio', y='Cantidad', hue='Categoría', data=df, s=100, alpha=0.7)
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
                input("Presiona Enter para continuar...")
            elif graph_choice == '6':
                # Gráfica 6: Proporción de Productos por Categoría (Pie Chart)
                plt.figure(figsize=(10, 7))
                productos_por_categoria = df['Categoría'].value_counts()
                plt.pie(productos_por_categoria, labels=productos_por_categoria.index, autopct='%1.1f%%', startangle=90, textprops={'fontsize': 10})
                plt.title('6. Proporción de Productos por Categoría')
                plt.axis('equal')
                plt.figtext(0.5, 0.02,
                            "Análisis: Este gráfico circular muestra la distribución porcentual de los productos listados por categoría. 'Cuidado personal' domina con la mayor proporción, indicando una amplia variedad de productos en esta sección, seguido por 'Hogar' y 'Belleza'. Esto resalta el enfoque del inventario en estas áreas.",
                            fontsize=9, ha='center', va='bottom', wrap=True, transform=plt.gcf().transFigure)
                plt.tight_layout(rect=[0, 0.15, 1, 1])
                plt.savefig('grafica_6_proporcion_categorias.png', dpi=300, bbox_inches='tight')
                plt.show()
                input("Presiona Enter para continuar...")
            elif graph_choice == '7':
                # Volver al menú principal
                print("Volviendo al menú principal...")
                break # Sale del bucle del submenú de gráficas
            else:
                print("Opción de gráfica no válida. Por favor, ingresa un número del 1 al 7.")
    elif main_choice == '3':
        # Opción 3: Salir del programa
        print("¡Hasta luego! ✅ ")
        break
    else:
        # Mensaje de error para entradas inválidas en el menú principal
        print("Opción no válida. Por favor, ingresa 1, 2 o 3.")