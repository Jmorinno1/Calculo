# Análisis de Campos y Fórmulas de la Tabla de Recursos

## Campos Identificados

1. **AÑO**: Año del cálculo
2. **MES**: Mes del cálculo
3. **ASISTENCIAS**: Número de asistencias registradas en ese mes
4. **RATIO ESTIMADO**: Ratio aplicado (varía entre 1,40 y 2,00 según el mes)
5. **HORAS NECESARIAS SERVICIO**: Horas requeridas para cubrir las asistencias
6. **HORAS PERSONAL CONTRATADO**: Horas disponibles del personal ya contratado
7. **ABSENTISMO Y VACACIONES ESTIMADO**: Horas estimadas de ausencia por vacaciones y absentismo
8. **HORAS NUEVAS NECESARIAS**: Horas adicionales requeridas (o sobrantes si es negativo)
9. **HORAS CONTRATADAS PERSONAL EVENTUAL**: Horas disponibles de personal eventual
10. **Nº PERSONAS NUEVAS CONTRATACIONES**: Número de personas a contratar (o reducir si es negativo)
11. **HORAS TOTALES**: Total de horas necesarias incluyendo absentismo

## Fórmulas Identificadas

Basado en los datos proporcionados, las fórmulas parecen ser:

1. **HORAS NECESARIAS SERVICIO** = ASISTENCIAS × RATIO ESTIMADO
   - Ejemplo: 13870 × 1,40 = 19418

2. **HORAS NUEVAS NECESARIAS** = HORAS NECESARIAS SERVICIO + ABSENTISMO Y VACACIONES ESTIMADO - HORAS PERSONAL CONTRATADO
   - Ejemplo: 19418 + 796 - 17551 = 2663

3. **Nº PERSONAS NUEVAS CONTRATACIONES** = Parece calcularse dividiendo HORAS NUEVAS NECESARIAS entre un valor estándar de horas por persona
   - Este valor parece variar según el mes, pero aproximadamente 160-170 horas/persona

4. **HORAS TOTALES** = HORAS NECESARIAS SERVICIO + ABSENTISMO Y VACACIONES ESTIMADO
   - Ejemplo: 19418 + 796 = 20214

## Observaciones Adicionales

- El **RATIO ESTIMADO** cambia según el mes:
  - Valor 1,40 para la mayoría de los meses
  - Valor 2,00 para junio, julio y agosto (meses de verano)

- El **ABSENTISMO Y VACACIONES ESTIMADO** tiene valores más altos en:
  - Julio (2314)
  - Agosto (2207)
  - Diciembre (2039)
  - Esto probablemente refleja períodos vacacionales más intensos

- Las **HORAS CONTRATADAS PERSONAL EVENTUAL** varían ligeramente por mes, pero mantienen cierta estabilidad dentro de rangos:
  - 1420-1633 para la mayoría de los meses
  - 1704 para septiembre, octubre y noviembre

- El **Nº PERSONAS NUEVAS CONTRATACIONES** puede ser positivo o negativo:
  - Positivo indica necesidad de contratar más personal
  - Negativo indica exceso de personal para las necesidades

## Dependencias con Otros Módulos

1. **Módulo de Asistencias**: Proporciona los datos de ASISTENCIAS por mes
2. **Módulo de Personal**: Proporciona información sobre HORAS PERSONAL CONTRATADO
3. **Módulo de Vacaciones**: Contribuye al cálculo de ABSENTISMO Y VACACIONES ESTIMADO
4. **Parámetros del Sistema**: Define los RATIO ESTIMADO para cada mes

## Consideraciones para la Implementación

1. Permitir la configuración de ratios por mes y por aeropuerto
2. Implementar cálculos automáticos basados en datos históricos y proyecciones
3. Habilitar ajustes manuales para casos especiales
4. Mostrar totales y subtotales como en la tabla original
5. Destacar visualmente valores negativos y positivos en HORAS NUEVAS NECESARIAS y Nº PERSONAS NUEVAS CONTRATACIONES
6. Permitir exportación a Excel manteniendo el formato original
