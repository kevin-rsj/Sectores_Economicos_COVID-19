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
  
  Los sectores de supermercados (WMT, COST, KR), manufactura (GM, CAT, F), finanzas (GS, BAC, JPM) y telecomunicaciones (TMUS, EBAY, CSCO, MSFT, ZM) no presentan outliers, lo que indica una estabilidad en los precios de sus acciones. Durante la pandemia, estos sectores probablemente experimentaron una demanda constante, especialmente en los supermercados, que vieron un aumento en las compras debido a la preocupación por la disponibilidad de productos esenciales.

- Sectores con Outliers:

  - Energía: La alta volatilidad en el sector energético se refleja en el número significativo de outliers en CVX (83) y XOM (18), lo que sugiere que estas empresas enfrentaron importantes desafíos durante la   pandemia, incluyendo la caída de la demanda de petróleo.
  - Telecomunicaciones: El sector mostró variaciones en su desempeño, con 47 outliers en T. A medida que más personas trabajaban desde casa, los servicios de telecomunicaciones fueron esenciales, aunque también enfrentaron desafíos por competencia y cambios en la demanda.
  - Farmacéuticas: Con 68 outliers en MRK y 2 en PFE, el sector farmacéutico mostró un impacto significativo de la pandemia. La presión por el desarrollo de tratamientos y vacunas, junto con noticias sobre COVID-19, causaron fluctuaciones notables en los precios de las acciones.

**4.3. Análisis Temporal del Precio**

  - Pre-pandemia (junio 2019 - febrero 2020):
El mercado mostró un comportamiento moderadamente positivo, con sectores tecnológicos, financieros y de consumo esencial en crecimiento. Microsoft y Alibaba lideraron el auge tecnológico, impulsados por la digitalización, aunque Cisco y Zoom mostraron ligera depreciación. En finanzas, Goldman Sachs, JPMorgan y Bank of America reflejaron un crecimiento estable, mientras que el sector de supermercados, liderado por Costco, también mostró apreciación, aunque Walmart y Kroger crecieron de manera más moderada. Los sectores de energía y manufactura enfrentaban desafíos, con ExxonMobil y Ford viendo caídas en sus precios ajustados.

  - Pandemia (marzo 2020 - mayo 2021):
Durante este periodo, la mayoría de los sectores registraron una clara apreciación. El trabajo remoto impulsó un crecimiento considerable en empresas como Zoom y Microsoft. El sector financiero, encabezado por Goldman Sachs y JPMorgan, se valorizó debido al movimiento de capitales. La manufactura, con Caterpillar y General Motors, mostró signos de recuperación, y los sectores de e-commerce y supermercados se beneficiaron de la creciente demanda por productos esenciales. En contraste, el sector de telecomunicaciones, aunque relevante, mostró un crecimiento moderado, destacándose T-Mobile.

  - Post-pandemia (junio 2021 - junio 2022):
El comportamiento del mercado fue heterogéneo, con sectores en crecimiento y otros enfrentando correcciones. El e-commerce, que había crecido exponencialmente, sufrió caídas significativas en empresas como Alibaba, Amazon y eBay. El sector tecnológico también experimentó correcciones, con Zoom enfrentando una caída considerable. Sin embargo, el sector energético se recuperó, con Chevron y ExxonMobil apreciándose gracias al aumento en los precios del petróleo. El sector de supermercados mantuvo una tendencia positiva, mientras que el de telecomunicaciones mostró desaceleración. El sector financiero también enfrentó correcciones negativas, con Goldman Sachs y JPMorgan registrando caídas en sus precios, reflejando la volatilidad económica.

**4.4. Volatilidad**:

Durante la pandemia (2020), se registró un aumento generalizado en la volatilidad de los retornos diarios en todos los sectores analizados. Por ejemplo, los tickers de e-commerce como AMZN, BABA y EBAY experimentaron incrementos en su volatilidad, pasando de promedios pre-pandemia de 0.013733, 0.018401 y 0.016821 a 0.022406, 0.026101 y 0.023784, respectivamente. El sector energético también vio un aumento significativo, con BP, CVX y XOM subiendo de 0.012233, 0.012322 y 0.014112 a 0.036754, 0.035379 y 0.031248. Aunque la volatilidad se redujo tras la pandemia, sectores como el e-commerce, con BABA alcanzando 0.043596, continuaron mostrando alta volatilidad. En contraste, el sector farmacéutico y de telecomunicaciones se estabilizaron, con promedios de 0.010242 y 0.010682, respectivamente.

**4.5. Rendimiento Acumulado (Total Returns)**

Entre junio de 2019 y junio de 2022, los sectores económicos mostraron comportamientos diversos frente a la pandemia y su recuperación. Durante la pandemia, los sectores de Tecnologías de Comunicación y Supermercados destacaron, con Zoom (+193.10%) y Microsoft (+46.30%) impulsados por la demanda de trabajo remoto, y Kroger (+27.86%) y Costco (+26.89%) reflejando el aumento en la demanda de productos esenciales. El sector financiero también tuvo un desempeño notable, con Goldman Sachs (+82.10%) y JPMorgan (+41.00%) subrayando la resiliencia del sistema financiero.

El sector farmacéutico se mantuvo estable, con Johnson & Johnson (+24.92%) y Pfizer (+23.10%) beneficiándose de su participación en el desarrollo de vacunas. Sin embargo, tras el auge pandémico, el e-commerce sufrió correcciones significativas, con Alibaba (-47.13%) y Amazon (-32.32%), mientras que el sector financiero enfrentó caídas, con Goldman Sachs (-18.93%) y JPMorgan (-28.80%).

Post-pandemia, el sector energético mostró una notable recuperación, con ExxonMobil (+53.16%) y Chevron (+43.95%) beneficiándose del aumento en los precios del petróleo. En resumen, los sectores de tecnología y supermercados lideraron durante la pandemia, mientras que el energético demostró una gran capacidad de recuperación, y el e-commerce enfrentó importantes correcciones.


**4.6. Correlación entre Sectores**

En el análisis de correlación entre sectores, se observa una alta correlación positiva entre empresas del sector energético, como Chevron (CVX) y ExxonMobil (XOM), con un coeficiente de 0.97. También, las empresas financieras como JPMorgan (JPM), Goldman Sachs (GS) y Bank of America (BAC) presentan una correlación moderada (entre 0.5 y 0.8), lo que indica que sus retornos tienden a moverse en la misma dirección. En el sector de supermercados, Costco (COST) y Walmart (WMT) muestran una correlación moderada de 0.57.

Por otro lado, algunas empresas del sector tecnológico, como Zoom (ZM) y ExxonMobil (XOM), presentan correlaciones negativas (-0.79), sugiriendo que sus retornos tienden a moverse en direcciones opuestas. En el sector farmacéutico, Pfizer (PFE) y Merck (MRK) muestran una baja correlación de 0.27, indicando que no siguen patrones de retorno similares.

**4.7. Análisis de Tendencias y Estacionalidad**

El análisis de descomposición de series de tiempo revela patrones significativos durante la pandemia, donde la mayoría de las empresas experimentaron caídas drásticas en sus valores estacionales. No obstante, algunas, como ExxonMobil (XOM), Verizon (VZ), Merck (MRK), Johnson & Johnson (JNJ) y Amazon (AMZN), mostraron notable resiliencia, recuperándose más rápidamente. En el periodo post-pandemia, varias de estas empresas mantienen una tendencia positiva y un crecimiento robusto, incluyendo a ExxonMobil, Pfizer (PFE), Microsoft (MSFT), Kroger (KR), Costco (COST), Caterpillar (CAT) y BP (BP). Esto sugiere no solo una efectiva recuperación, sino también una posible expansión en sus operaciones, reforzando su posición en un entorno post-pandemia.
