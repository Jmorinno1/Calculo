# Análisis de Parámetros y Tiempos Específicos por Aeropuerto

## Parámetros Identificados

### 1. Distribución de Tráfico
Porcentaje de asistencias que corresponden a llegadas y salidas para cada aeropuerto:

| Aeropuerto | Llegada (%) | Salida (%) |
|------------|-------------|------------|
| TENERIFE SUR/ REINA SOFIA | 45,53% | 54,47% |
| TENERIFE NORTE/ LOS RODEOS | 48,69% | 48,90% |
| LA PALMA /STA.CRUZ DE LA PALMA | 49,88% | 49,80% |
| GRAN CANARIA | 43,13% | 54,45% |
| LANZAROTE | 48,03% | 51,92% |
| FUERTEVENTURA | 45,80% | 54,15% |

### 2. Tiempos Promedio de Asistencias
Tiempo medio (en horas) que toma cada tipo de asistencia:

| Aeropuerto | Llegada (h) | Salida (h) | Interrupción (h) |
|------------|-------------|------------|------------------|
| LA PALMA /STA.CRUZ DE LA PALMA | 0,42 | 0,45 | 0,5 |
| TENERIFE NORTE/ LOS RODEOS | 0,46 | 0,42 | 0,5 |
| TENERIFE SUR/ REINA SOFIA | 0,91 | 1,40 | 0,5 |
| GRAN CANARIA | 0,67 | 1,17 | 0,5 |
| LANZAROTE | 0,61 | 1,10 | 0,5 |
| FUERTEVENTURA | 0,56 | 1,22 | 0,5 |

### 3. Ratio Promedio (Ejemplo para Tenerife Sur en Marzo)
Cálculo detallado del ratio estimado:

| Aeropuerto | Llegada | Salida | Mostradores | Coordinación | Asistencias | Improductividad 5% | Ratio Estimado |
|------------|---------|--------|-------------|--------------|-------------|-------------------|---------------|
| TENERIFE SUR/ REINA SOFIA | 54148,98 | 99676,07 | 20440 | 25337 | 130706 | -16966 | 1,40 |

## Fórmulas Identificadas

Basado en los datos proporcionados, las fórmulas para calcular el ratio estimado parecen ser:

1. **Horas Llegada** = Número de asistencias de llegada × Tiempo promedio de llegada × % Distribución llegada
   - Ejemplo TFS: 130706 × 0,91 × 45,53% = 54148,98 horas

2. **Horas Salida** = Número de asistencias de salida × Tiempo promedio de salida × % Distribución salida
   - Ejemplo TFS: 130706 × 1,40 × 54,47% = 99676,07 horas

3. **Horas Mostradores** = Valor específico para cada aeropuerto (posiblemente calculado con otra fórmula)
   - Ejemplo TFS: 20440 horas

4. **Horas Coordinación** = Valor específico para cada aeropuerto (posiblemente calculado con otra fórmula)
   - Ejemplo TFS: 25337 horas

5. **Improductividad** = 5% del total de horas (Llegada + Salida + Mostradores + Coordinación)
   - Ejemplo TFS: 5% de (54148,98 + 99676,07 + 20440 + 25337) = 16966 horas

6. **Ratio Estimado** = (Horas Llegada + Horas Salida + Horas Mostradores + Horas Coordinación - Improductividad) / Número de asistencias
   - Ejemplo TFS: (54148,98 + 99676,07 + 20440 + 25337 - 16966) / 130706 = 1,40

## Observaciones Adicionales

1. Los tiempos de asistencia varían significativamente entre aeropuertos:
   - Las asistencias de salida generalmente toman más tiempo que las de llegada
   - Tenerife Sur tiene los tiempos más altos (0,91h para llegadas y 1,40h para salidas)
   - La Palma tiene los tiempos más bajos (0,42h para llegadas y 0,45h para salidas)

2. La interrupción es constante (0,5h) para todos los aeropuertos

3. La distribución entre llegadas y salidas es relativamente equilibrada, pero varía por aeropuerto:
   - Gran Canaria tiene la mayor diferencia (43,13% llegadas vs 54,45% salidas)
   - La Palma tiene la distribución más equilibrada (49,88% llegadas vs 49,80% salidas)

4. El ratio estimado de 1,40 para Tenerife Sur indica que se necesitan aproximadamente 1,4 horas de trabajo por cada asistencia

## Consideraciones para la Implementación

1. Crear un modelo de datos para almacenar estos parámetros específicos por aeropuerto:
   - Distribución de tráfico (llegadas/salidas)
   - Tiempos promedio (llegadas, salidas, interrupciones)
   - Valores para mostradores y coordinación
   - Porcentaje de improductividad

2. Permitir la edición de estos parámetros a través de una interfaz de usuario

3. Integrar estos parámetros en el cálculo de recursos necesarios:
   - Utilizar los tiempos específicos de cada aeropuerto
   - Aplicar la distribución de tráfico correspondiente
   - Calcular el ratio estimado basado en estos valores

4. Implementar un sistema de versiones para los parámetros, permitiendo:
   - Guardar configuraciones históricas
   - Comparar resultados con diferentes conjuntos de parámetros
   - Proyectar escenarios con parámetros modificados

5. Asegurar que los cálculos de recursos utilicen automáticamente los parámetros correctos según el aeropuerto seleccionado
