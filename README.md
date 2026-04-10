# Microservicio DevOps

## Descripción
En este proyecto desarrollamos un repositorio Git basado en un microservicio, aplicando prácticas DevOps como control de versiones, trabajo colaborativo y automatización.

## Estrategia de Ramificación
Se utiliza GitFlow:
* main: producción
* develop: desarrollo
* feature/*: nuevas funcionalidades
* hotfix/*: correcciones

### Justificación:
Se eligió GitFlow porque permite organizar el trabajo en equipo, mantener estabilidad y facilitar la integración continua.

## Modelos de Ramificación
* GitFlow
* GitHub Flow
* Trunk-Based Development
Se selecciona GitFlow por su control en entornos colaborativos.

## Flujo DevOps
1. Crear ramas feature desde develop
2. Realizar commits
3. Crear Pull Request
4. Validar cambios
5. Merge a main

## Simulación Colaborativa
* Feature login
* Feature register
* Hotfix error-login
Se utilizaron Pull Requests para integrar cambios.

## Convenciones
* feat: funcionalidad
* fix: error
* docs: documentación

## GitHub Actions
Se implementa un pipeline que se ejecuta en:
* push a develop
* pull request a main


## Tecnologías
* Git
* GitHub
* GitHub Actions

## Conclusión
En este proyecto aprendí a utilizar GitFlow, automatización y trabajo colaborativo en un entorno DevOps.
