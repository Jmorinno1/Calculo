# Documentación del Sistema de Cálculo de Recursos

## Introducción

Este documento proporciona información sobre el prototipo web desarrollado para reemplazar el archivo Excel "2025. Cálculo de recursos PMR TFS_MARZO.xlsx". El sistema permite gestionar parámetros, personal, vacaciones, asistencias históricas y realizar cálculos de recursos necesarios, todo ello a través de una interfaz web intuitiva y una base de datos centralizada.

## Acceso al Sistema

El prototipo está disponible temporalmente en la siguiente URL:
- **URL de acceso**: [https://5000-iiu5u530fvuyunycw7vda-a8d40c44.manus.computer](https://5000-iiu5u530fvuyunycw7vda-a8d40c44.manus.computer)

> **Nota importante**: Este es un entorno de pruebas y la URL es temporal. Los datos introducidos se almacenarán en una base de datos de desarrollo y podrían perderse al finalizar la sesión de prueba.

## Funcionalidades Principales

El sistema cuenta con las siguientes secciones principales:

### 1. Dashboard

Muestra un resumen general con:
- Contadores de personal, parámetros, asistencias y cálculos
- Últimos cálculos de recursos realizados
- Últimas asistencias registradas

### 2. Gestión de Parámetros

Permite configurar los parámetros del sistema que afectan a los cálculos:
- Crear, editar y eliminar parámetros
- Asignar categorías para organizar los parámetros
- Establecer valores numéricos y descripciones

Los parámetros clave que deben configurarse son:
- **% CONTRA**: Porcentaje de contratación
- **MARGEN H. COMP %**: Margen de horas complementarias

### 3. Gestión de Personal

Permite administrar la información del personal:
- Crear, editar y eliminar registros de personal
- Gestionar diferentes tipos de contrato (Fijo, Fijo Discontinuo, Temporal)
- Establecer fechas de inicio y fin de contrato
- Configurar horas de contrato

### 4. Gestión de Vacaciones

Permite administrar los periodos vacacionales del personal:
- Crear, editar y eliminar periodos vacacionales
- Filtrar vacaciones por empleado
- Establecer estado de las vacaciones (Pendiente, Aprobada, Rechazada)
- Calcular automáticamente periodos vacacionales para personal fijo discontinuo

### 5. Gestión de Asistencias

Permite registrar y consultar datos históricos de asistencias:
- Crear, editar y eliminar registros de asistencias
- Filtrar asistencias por año
- Registrar cantidad, distribución e incremento de asistencias

### 6. Cálculo de Recursos

Permite realizar cálculos de recursos necesarios:
- Crear nuevos cálculos especificando periodo y parámetros
- Visualizar resultados de cálculos anteriores
- Comparar recursos necesarios con recursos disponibles

## Guía de Uso Inicial

### Configuración Inicial Recomendada

Para comenzar a utilizar el sistema, se recomienda seguir estos pasos:

1. **Configurar Parámetros Básicos**:
   - Acceder a la sección "Parámetros"
   - Crear el parámetro "% CONTRA" con un valor inicial (ej: 0.45)
   - Crear el parámetro "MARGEN H. COMP %" con un valor inicial (ej: 0.1)

2. **Registrar Personal**:
   - Acceder a la sección "Personal"
   - Añadir al menos 3-5 empleados con diferentes tipos de contrato
   - Asegurarse de incluir al menos un empleado con contrato "Fijo Discontinuo"

3. **Registrar Datos Históricos de Asistencias**:
   - Acceder a la sección "Asistencias"
   - Añadir datos de asistencias para los últimos 12 meses
   - Incluir cantidad de asistencias y distribución para cada mes

4. **Realizar un Cálculo de Recursos**:
   - Acceder a la sección "Cálculos"
   - Crear un nuevo cálculo especificando el periodo (ej: "Mayo 2025")
   - Revisar los resultados obtenidos

5. **Gestionar Vacaciones**:
   - Acceder a la sección "Vacaciones"
   - Crear periodos vacacionales para el personal
   - Probar la funcionalidad de cálculo automático para fijos discontinuos

## Lógica de Cálculo Implementada

### Cálculo de Recursos Necesarios

El sistema implementa la siguiente lógica para calcular los recursos necesarios:

1. Obtiene el promedio de asistencias de los últimos 12 meses
2. Aplica el incremento proyectado especificado por el usuario
3. Utiliza la distribución promedio para calcular los recursos necesarios
4. Calcula los recursos disponibles basados en las horas contratadas del personal
5. Ajusta los recursos disponibles según el porcentaje de contratación
6. Calcula la diferencia entre recursos disponibles y necesarios

### Cálculo de Vacaciones para Fijos Discontinuos

Para el personal con contrato fijo discontinuo, el sistema:

1. Calcula los días de vacaciones proporcionales según el tiempo trabajado
2. Distribuye las vacaciones en dos periodos (verano e invierno)
3. Genera automáticamente los registros de vacaciones con fechas de inicio y fin

## Consideraciones Técnicas

- **Entorno de Desarrollo**: Este es un prototipo y no debe utilizarse en un entorno de producción sin revisiones adicionales de seguridad.
- **Base de Datos**: El sistema utiliza MySQL para almacenar la información. La estructura de la base de datos se crea automáticamente al iniciar la aplicación.
- **Seguridad**: Se han implementado validaciones básicas, pero se recomienda una revisión de seguridad completa antes de un despliegue en producción.
- **Respaldo de Datos**: Se recomienda implementar un sistema de respaldo regular de la base de datos en un entorno de producción.

## Próximos Pasos Recomendados

Para evolucionar este prototipo a un sistema completo de producción, se recomienda:

1. Implementar un sistema de autenticación y autorización de usuarios
2. Mejorar la validación de datos y manejo de errores
3. Añadir funcionalidades de exportación de datos e informes
4. Implementar un sistema de notificaciones para eventos importantes
5. Realizar pruebas exhaustivas con datos reales
6. Configurar un entorno de producción seguro con respaldos automáticos

## Soporte y Contacto

Para cualquier consulta o soporte relacionado con este prototipo, por favor contacte al equipo de desarrollo.

---

© 2025 Sistema de Cálculo de Recursos - Versión 1.0
