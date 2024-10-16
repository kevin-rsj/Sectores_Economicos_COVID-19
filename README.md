# Sectores_Economicos_COVID-19
Análisis Exploratorio de Datos (EDA): Comportamiento de Sectores Económicos antes, durante y después de la Pandemia de COVID-19 (2019-2022)

### **1. Definición del Objetivo**

- **Objetivo Principal**: Realizar un análisis exploratorio de datos (EDA) para identificar las diferencias en el comportamiento de los distintos sectores económicos previo, durante y después de la pandemia de COVID-19, considerando un rango temporal de junio de 2019 a junio de 2022.
- **Sectores**: Supermercados, Farmacéutica, Tecnología de Comunicación, E-commerce, Telecomunicaciones, Finanzas, Energía y Manufactura.
- **Empresas**: Se analizarán tres empresas representativas de cada sector, con el fin de observar las tendencias y la evolución de su desempeño en el periodo de interés.

### **2. Recolección de Datos**

- **Fuente de Datos**: Yahoo Finance (API `yfinance`)
- **Periodo de Datos**: Desde el 1 de junio de 2019 hasta el 30 de junio de 2022.
- **Empresas Representativas por Sector**:
  
    - **Supermercados**: Walmart (WMT), Costco (COST), Kroger (KR)
    - **Farmacéutica**: Pfizer (PFE), Johnson & Johnson (JNJ), Merck (MRK)
    - **Tecnología de Comunicación**: Zoom (ZM), Microsoft (MSFT), Cisco Webex (CSCO)
    - **E-commerce**: Amazon (AMZN), Alibaba (BABA), eBay (EBAY)
    - **Telecomunicaciones**: Verizon (VZ), AT&T (T), T-Mobile (TMUS)
    - **Finanzas**: JPMorgan Chase (JPM), Bank of America (BAC), Goldman Sachs (GS)
    - **Energía**: ExxonMobil (XOM), Chevron (CVX), BP p.l.c. (BP)
    - **Manufactura**: General Motors (GM), Caterpillar (CAT), Ford (F)
      
### **Script de Recolección de Datos**:

Se descargan los datos históricos de cada empresa, agrupados por sector, para el periodo definido utilizando el script ([“data_collection_py”](https://github.com/kevin-rsj/Sectores_Economicos_COVID-19/blob/main/Scripts/data_collection.py.py)). Los datos son guardados en archivos CSV ([ “raw_data”](https://github.com/kevin-rsj/Sectores_Economicos_COVID-19/blob/main/Data/raw_data.csv)) para su procesamiento posterior.

### **3. Limpieza de Datos**

- **Validación Inicial**: Verificar que los datos descargados no contengan valores nulos ni duplicados.
- **Script de Limpieza de Datos**: script ([“data_cleaning_py”](https://github.com/kevin-rsj/Sectores_Economicos_COVID-19/blob/main/Scripts/data_cleaning.py.py)), asegurando que los datos estén listos para el análisis exploratorio, se genera guarda el resultado en un archivo CSV ([“cleaned_data”](https://github.com/kevin-rsj/Sectores_Economicos_COVID-19/blob/main/Data/cleaned_data.csv)).

### **4. Análisis Exploratorio de Datos (EDA)**
Este análisis examina el comportamiento del mercado bursátil en varios sectores durante la pandemia de COVID-19. A través de un enfoque sectorial, se busca identificar patrones y diferencias clave en el rendimiento de las acciones a lo largo de este periodo. Para más detalles, consulta el ([notebook](https://github.com/kevin-rsj/Sectores_Economicos_COVID-19/blob/main/Notebooks/EDA_Sectores_Economicos_COVID-19.ipynb)).

**4.1  Resumen Estadístico**:

El análisis explora información de 24 empresas pertenecientes a 8 sectores económicos, con un total de 18,624 observaciones (2,328 por sector) desde el 3 de junio de 2019 hasta el 29 de junio de 2022. El conjunto de datos incluye las siguientes columnas:

  - Open: Precio de apertura de la acción.
  - High: Precio más alto alcanzado durante el día.
  - Low: Precio más bajo durante el día.
  - Close: Precio de cierre de la acción.
  - Adj Close: Precio de cierre ajustado.
  - Volume: Cantidad de acciones intercambiadas en el mercado.
  - Sector: Sector económico al que pertenece la empresa.
  - Ticker: Símbolo de cotización de la empresa.

    
**4.2 Visualización de la Distribución de Precios**

- Sectores sin Outliers:
  
  Los sectores de supermercados, manufactura y finanzas  no presentan outliers, lo que indica una estabilidad en los precios de sus acciones. Durante la pandemia, estos sectores probablemente experimentaron una demanda constante, especialmente en los supermercados, que vieron un aumento en las compras debido a la preocupación propias del contexto de pandemia.

- Sectores con Outliers:

  - Energía: El sector energético tiene una alta volatilidad y se refleja en el número significativo de outliers en CVX (83) y XOM (18), esto sugiere que las empresas enfrentaron importantes desafíos durante la   pandemia, incluyendo la caída de la demanda de petróleo.
  - Telecomunicaciones: El sector mostró variaciones en su desempeño, con 47 outliers en T. Con el augue del trabajo remoto, los servicios de telecomunicaciones fueron esenciales, aunque también enfrentaron desafíos por competencia y cambios en la demanda.
  - Farmacéuticas: Con 68 outliers en MRK y 2 en PFE, la pandemia reflejo un impacto significativo en el sector farmacéutico. La presión por el desarrollo de tratamientos y vacunas, junto con noticias sobre COVID-19, causaron fluctuaciones notables en los precios de las acciones.

**4.3. Análisis Temporal del Precio**

  - Pre-pandemia (junio 2019 - febrero 2020):
El mercado mostró un comportamiento moderadamente positivo, con sectores tecnológicos y  financieros. Microsoft y Alibaba lideraron el auge tecnológico, por otra parte Cisco y Zoom mostraron ligera depreciación. En finanzas, Goldman Sachs, JPMorgan y Bank of America reflejaron un crecimiento estable.

  - Pandemia (marzo 2020 - mayo 2021):
Durante este periodo, la mayoría de los sectores registraron una clara apreciación. El trabajo remoto impulsó un crecimiento considerable en empresas como Zoom y Microsoft. El sector financiero, encabezado por Goldman Sachs y JPMorgan, se valorizó debido al movimiento de capitales. La manufactura, con Caterpillar y General Motors, mostró signos de recuperación, y los sectores de e-commerce y supermercados se beneficiaron de la creciente demanda por productos esenciales. En contraste, el sector de telecomunicaciones, aunque relevante, mostró un crecimiento moderado, destacándose T-Mobile.

  - Post-pandemia (junio 2021 - junio 2022):
El comportamiento del mercado fue heterogéneo, con sectores en crecimiento y otros enfrentando correcciones. El e-commerce, que había registrado un fuerte crecimiento, sufrió caídas significativas en empresas como Alibaba, Amazon y eBay. El sector tecnológico también experimentó correcciones como es el caso de Zoom que enfrento una caída considerable. Sin embargo, el sector energético se recuperó, Chevron y ExxonMobil se revaloraron posiblemente motivado por el aumento de los precios en el petróleo. 

**4.4. Volatilidad**:

Durante la pandemia (2020), se registró un aumento generalizado en la volatilidad de los retornos diarios en todos los sectores analizados. Por ejemplo, los tickers de e-commerce como AMZN, BABA y EBAY experimentaron incrementos en su volatilidad, pasando de promedios pre-pandemia de 0.013733, 0.018401 y 0.016821 a 0.022406, 0.026101 y 0.023784, respectivamente. El sector energético también vio un aumento significativo, con BP, CVX y XOM subiendo de 0.012233, 0.012322 y 0.014112 a 0.036754, 0.035379 y 0.031248. Aunque la volatilidad se redujo tras la pandemia, sectores como el e-commerce, con BABA alcanzando 0.043596, continuaron mostrando alta volatilidad.

**4.5. Rendimiento Acumulado (Total Returns)**

Entre junio de 2019 y junio de 2022, los sectores económicos mostraron comportamientos diversos frente a la pandemia y su recuperación. En el periodo de pandemia, los sectores de Tecnologías de Comunicación y Supermercados destacaron, con Zoom (+193.10%) y Microsoft (+46.30%) impulsados por la demanda de trabajo remoto, y Kroger (+27.86%) y Costco (+26.89%) por el aumento en la demanda de productos esenciales. El sector financiero también tuvo un desempeño notable, con Goldman Sachs (+82.10%) y JPMorgan (+41.00%).

El sector farmacéutico se mantuvo estable, con Johnson & Johnson (+24.92%) y Pfizer (+23.10%) beneficiándose de su participación en el desarrollo de vacunas. Por su parte, tras el auge pandémico, el e-commerce sufrió correcciones significativas, con Alibaba (-47.13%) y Amazon (-32.32%).

Post-pandemia, el sector energético mostró una notable recuperación, con ExxonMobil (+53.16%) y Chevron (+43.95%) beneficiándose del aumento en los precios del petróleo. Los sectores de tecnología y supermercados lideraron durante la pandemia, mientras que el energético demostró una gran capacidad de recuperación, y el e-commerce enfrentó importantes correcciones.


**4.6. Correlación entre Sectores**

En el análisis de correlación entre sectores, se observa una alta correlación positiva entre empresas del sector energético, como Chevron (CVX) y ExxonMobil (XOM), con un coeficiente de 0.97. También, las empresas financieras como JPMorgan (JPM), Goldman Sachs (GS) y Bank of America (BAC) presentan una correlación moderada (entre 0.5 y 0.8), lo que indica que sus retornos tienden a moverse en la misma dirección. 

Por otro lado, algunas empresas del sector tecnológico como Zoom (ZM) y ExxonMobil (XOM) de energia, presentan una correlación negativa (-0.79), sugiriendo que sus retornos tienden a moverse en direcciones opuestas.

**4.7. Análisis de Tendencias y Estacionalidad**

El análisis de descomposición de series de tiempo revela patrones significativos durante la pandemia, donde la mayoría de las empresas experimentaron caídas drásticas en sus valores estacionales. No obstante, algunas, como ExxonMobil (XOM), Verizon (VZ), Merck (MRK), Johnson & Johnson (JNJ) y Amazon (AMZN), mostraron notable resiliencia, recuperándose más rápidamente. En el periodo post-pandemia, varias de estas empresas mantienen una tendencia positiva y un crecimiento robusto, incluyendo a ExxonMobil, Pfizer (PFE), Microsoft (MSFT), Kroger (KR), Costco (COST), Caterpillar (CAT) y BP (BP). 

### **5. Visualización de Resultados**
**5.1 Gráficos**

- Los visualizaciones generadas con el análisis exploratorio esta disponibles en la carpeta de(["visualizations"](https://github.com/kevin-rsj/Sectores_Economicos_COVID-19/tree/main/visualizations)) .

**5.2 Dashboard**
El dashboard del proyecto, que resume los análisis y resultados del Análisis Exploratorio de Datos del comportamiento de sectores económicos antes, durante y después de la pandemia de COVID-19, esta disponible en Looker Studio:(["Link"](https://lookerstudio.google.com/reporting/2484ea4b-337d-467b-86fa-dd9e4a7c180c))

-  **Portada**
  
    - **Titulo: Análisis de Sectores Económicos: Impacto de la Pandemia de COVID-19 (2019-2022**
    - **Descripción** : Un análisis visual de los principales sectores económicos antes, durante y después de la pandemia de COVID-19. Se incluye la evolución de precios, volatilidad, y tendencias de recuperación de empresas representativas.
    - **Periodo Analizado**: Junio 2019 - Junio 2022.
    
-  **Evolución Temporal por Sector**
  
    **Gráfico 1: Serie Temporal de Precios Ajustados** 
    
    - Tipo: **Gráfico de líneas múltiples**
    - Ejes:
        - **Eje X**: Tiempo (Años/meses: Junio 2019 - Junio 2022)
        - **Eje Y**: Precio Ajustado
    - **Propósito**: Mostrar la evolución de los precios de las acciones para los sectores clave en diferentes momentos de la pandemia.
    
    **Gráfico 2: Rendimiento Acumulado por Sector**
    
    - Tipo: **Gráfico de líneas**
    - Ejes:
        - **Eje X**: Tiempo (Años/meses: Junio 2019 - Junio 2022)
        - **Eje Y**: Retornos normalizados
    - **Propósito**: Evaluar el rendimiento acumulado de las empresas en cada sector durante el periodo pre-pandemia, pandemia y post-pandemia.
  
-  **Volatilidad y Comportamiento de Precios**
  
    **Gráfico 3: Volatilidad de Precios** 
    
    - Tipo: **Gráfico de caja (Boxplot)**
    - Ejes:
        - **Eje X**: Sectores
        - **Eje Y**: Precio ajustado
    - **Propósito**: Mostrar la variabilidad en los precios de las acciones de los sectores, comparando la volatilidad durante diferentes fases de la pandemia.
    
    **Gráfico 4: Outliers por Empresa (Junio 2019- Junio 2022)**
    
    - Tipo: **Gráfico de barras**
    - Ejes:
        - **Eje X**: Empresa
        - **Eje Y**: Cantidad de outliers
    - **Propósito**: Identificar los sectores y empresas que mostraron mayor número de valores atípicos (outliers) en su comportamiento de precios durante el periodo.
  
-  **Comparación de Rendimientos**
  
    **Gráfico 5: Rendimiento Porcentual Acumulados por Periodo**
    
    - Tipo: **Gráfico de barras**
    - Ejes:
        - **Eje X**: Retornos acumulado
        - **Eje Y**: Ticker
    - **Propósito**: Mostrar la variabilidad en los en los retornos acumulados de los distintos sectores en las diferentes fases de la pandemia.
    
    **Gráfico 6: Correlación de Rendimientos** 
    
    - Tipo: **Tabla Dinámica con** **Heatmap**
    - Ejes:
        - **Fila**: Ticker
        - **Columna**: Valores de correlación
    - **Propósito**: Medir la correlación entre los rendimientos de los sectores, identificando relaciones positivas o negativas en su comportamiento durante la pandemia.
  
-  **Análisis de Tendencias y Estacionalidad**
  
    **Gráfico 7: Descomposición de Series Temporales - Estacionalidad**
    
    - Tipo: **Gráfico de líneas múltiples**
    - Ejes:
        - **Eje X**: Tiempo
        - **Eje Y**: Componente de estacionalidad
    - **Propósito**: Visualizar los patrones estacionales identificados en el análisis de series temporales para cada sector y empresa.
      
    **Gráfico 8: Descomposición de Series Temporales - Tendencia**
   
    - Tipo: **Gráfico de líneas múltiples**
    - Ejes:
        - **Eje X**: Tiempo
        - **Eje Y**: Componente de tendencia
    - **Propósito**: Visualizar la tendencia por serie temporal para cada sector y empresa.
  
-  **Resumen**
  
    **Gráfico 8: Top 5: Empresas con Mayores Retornos Porcentuales Acumulados**
    
    - Tipo: **Gráfico de barras**
    - Ejes:
        - **Eje X**: Retornos acumulado
        - **Eje Y**: Ticker
    - **Propósito**: Mostrar las 5 empresas con mayor retorno acumulado en cada periodo de estudio.
      
    **Gráfico 9: Top 5: Empresas con Menores Retornos Porcentuales Acumulados**
   
    - Tipo: **Gráfico de barras**
    - Ejes:
        - **Eje X**: Retornos acumulado
        - **Eje Y**: Ticker
    - **Propósito**: Mostrar las 5 empresas con menor retorno acumulado en cada periodo de estudio.
      
    **Gráfico 10: Retorno Porcentual Promedio por Sector**
   
    - Tipo: **Gráfico de líneas**
    - Ejes:
        - **Eje X**: Retornos acumulado
        - **Eje Y**: Sector
    - **Propósito**: Identificar la evolución de los retornos acomunados por sector durante los periodos de estudio.
      
    **Gráfico 11: Retorno Porcentual Promedio**
   
    - Tipo: **Score Card**
    - Métrica: Promedio de retorno acumulado
  
    Las visualizaciones disponen de filtros:
    
    - Selector de sector (Supermercados, Farmacéutica, Tecnología, etc.)
    - Periodo de estudio (pre-pandemia, pandemia y post-pandemia)

### **6. Conclusiones**

1. **Impacto Diferenciado**:  Algunos sectores, como el **tecnológico** y los **supermercados**, experimentaron un auge significativo durante el confinamiento, otros, como el **sector energético** y **manufacturero**, enfrentaron grandes desafíos iniciales, pero se recuperaron fuertemente en la etapa post-pandemia.
   
2. **Volatilidad Sectorial**: Durante la pandemia los sectores en general estuvieron afectos a la volatilidad de sus precios, especialmente en **energía** y **e-commerce**, debido a la disrupción en las cadenas de suministro y fluctuaciones en la demanda. Sin embargo, sectores como **farmacéutica** y **supermercados** mantuvieron una mayor estabilidad durante este periodo, en parte por la demanda continua de productos esenciales y avances médicos.
   
3. **Augue del Trabajo Remoto**: El sector de **tecnología de comunicación**, representado por empresas como **Zoom** y **Microsoft**, creció exponencialmente durante la pandemia debido al auge del trabajo remoto. Sin embargo, en la etapa post-pandemia, empresas como **Zoom** enfrentaron fuertes correcciones a medida que la demanda por herramientas digitales se estabilizaba.
   
4. **Recuperación del Sector Energético**: Después de una caída pronunciada en 2020, el sector de **energía** se recuperó notablemente en 2021-2022 lo cual se podria explicar por la reactivación de la demanda de petróleo y el incremento en los precios de los combustibles. Empresas como **Chevron** y **ExxonMobil** se beneficiaron de esta recuperación, mostrando un rendimiento positivo en el periodo de post-pandemia.
 
5. **Sector E-commerce**: Aunque el sector experimentó un auge durante la pandemia debido al aumento de las compras en línea, empresas como **Amazon** y **Alibaba** sufrieron importantes correcciones post-pandemia, Lo cual se puede atribuir a una normalizacion de la demanda en sectores mas tradicionales.
   
6. **Evoluación del Sector Financiero**: El sector mostró un rendimiento resiliente durante la pandemia, impulsado por políticas monetarias expansivas y estímulos económicos implementados por el contexto de pandemia. Sin embargo, en la fase post-pandemia, este sector sufrió correcciones importantes, reflejando las incertidumbres económicas globales y nuevos desafios en los mercados financieros.
   
7. **Patrones de Correlación**: Se identificaron altas correlaciones dentro de sectores como **energía** y **finanzas**, lo que indica que las empresas dentro de un mismo sector tienden a moverse en direcciones similares. Por otro lado, la correlación negativa entre sectores como **tecnología** y **energía** evidencia que los retornos de estos sectores reaccionan de manera opuesta a ciertos eventos.

### **7. Documentación y Repositorio en GitHub**

- **Estructura del Repositorio**:
    - `data/`: Carpeta que contiene los archivos CSV con los datos crudos y limpios utilizados en el EDA y Dashboard.
    - `scripts/`: Scripts de recolección y limpieza de datos.
    - `notebooks/`: Notebooks con el análisis exploratorio de datos y visualizaciones.
    - `README.md`: Descripción detallada del proyecto.
    - `visualizations/`: Carpeta con las visualizaciones generadas.


