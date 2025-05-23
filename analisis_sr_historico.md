# Análisis de Campos y Fórmulas de SR Histórico

## Campos Identificados

1. **AÑO**: Año del registro de asistencias
2. **MES**: Mes del registro de asistencias
3. **ASISTENCIAS**: Número de asistencias registradas en ese mes
4. **DIST ACT**: Distribución actual - porcentaje que representa cada mes sobre el total anual
5. **DIST CERT**: Distribución certificada (aparece vacía en los datos proporcionados)
6. **INCREMENTO VS [AÑO ANTERIOR]**: Porcentaje de incremento respecto al mismo mes del año anterior

## Fórmulas Identificadas

Basado en los datos proporcionados, las fórmulas parecen ser:

1. **DIST ACT** = (ASISTENCIAS del mes / TOTAL ASISTENCIAS del año) × 100%
   - Ejemplo: (13870 / 140722,85) × 100% = 9,86%

2. **INCREMENTO VS [AÑO ANTERIOR]** = ((ASISTENCIAS año actual - ASISTENCIAS año anterior) / ASISTENCIAS año anterior) × 100%
   - Ejemplo: ((13870 - 12187) / 12187) × 100% = 13,81%

3. **TOTAL ASISTENCIAS** = Suma de todas las asistencias mensuales del año
   - Ejemplo 2023: 12187 + 10755 + ... + 12800 = 122155
   - Ejemplo 2024: 13870 + 12688 + ... + 14464 = 140722,85

4. **INCREMENTO TOTAL ANUAL** = ((TOTAL año actual - TOTAL año anterior) / TOTAL año anterior) × 100%
   - Ejemplo: ((140722,85 - 122155) / 122155) × 100% = 7,00%

## Observaciones Adicionales

- Los últimos meses del año 2024 (octubre, noviembre, diciembre) parecen tener un incremento proyectado del 13,00% respecto a 2023.
- El incremento total anual de 2024 vs 2023 es del 7,00%.
- La columna DIST CERT (Distribución Certificada) aparece vacía en los datos proporcionados, pero probablemente sea para registrar distribuciones oficiales o aprobadas.
- Las distribuciones (DIST ACT) siempre suman 100% para cada año completo.

## Dependencias con Otros Módulos

1. **Módulo de Asistencias**: Proporciona los datos de asistencias mensuales
2. **Módulo de Aeropuertos**: Para diferenciar los datos por aeropuerto

## Consideraciones para la Implementación

1. Permitir la visualización de datos históricos por año y aeropuerto
2. Calcular automáticamente las distribuciones al introducir nuevos datos de asistencias
3. Calcular automáticamente los incrementos respecto al año anterior
4. Permitir la proyección de meses futuros basados en incrementos definidos
5. Visualizar gráficamente la evolución de asistencias y distribuciones
6. Habilitar la comparación entre años y entre aeropuertos
7. Permitir la exportación de datos a Excel
8. Integrar con la página de Recursos para utilizar estos datos en los cálculos de personal necesario
