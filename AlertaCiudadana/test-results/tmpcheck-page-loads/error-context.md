# Instructions

- Following Playwright test failed.
- Explain why, be concise, respect Playwright best practices.
- Provide a snippet of code with the fix, if possible.

# Test info

- Name: tmpcheck.spec.js >> page loads
- Location: tmpcheck.spec.js:3:1

# Error details

```
Test timeout of 30000ms exceeded.
```

# Page snapshot

```yaml
- generic [active] [ref=e1]:
  - generic [ref=e2]: Acceso verificado al CAD
  - banner [ref=e7]:
    - generic [ref=e8]:
      - generic [ref=e13]:
        - heading "AlertaCiudadana Colombia · v4.0" [level=1] [ref=e14]:
          - text: AlertaCiudadana
          - generic [ref=e15]: Colombia · v4.0
        - paragraph [ref=e16]: Sistema local de gestión de incidentes urbanos
      - generic [ref=e17]:
        - button "Reportar Incidente" [ref=e18] [cursor=pointer]
        - button "Centro de Mando (CAD)" [ref=e22] [cursor=pointer]
        - button "Modo claro / oscuro" [ref=e28] [cursor=pointer]
  - main [ref=e31]:
    - generic [ref=e32]:
      - generic [ref=e33]:
        - generic [ref=e34]:
          - heading "Centro de Mando Asistido por Computadora (CAD)" [level=2] [ref=e35]
          - paragraph [ref=e36]: Supervisión en tiempo real e historial de incidentes reportados
        - generic [ref=e37]:
          - button "CSV" [ref=e38] [cursor=pointer]
          - button "Respaldo JSON" [ref=e42] [cursor=pointer]
          - button "Ver todos" [ref=e46] [cursor=pointer]
          - button "Cargar Ejemplos Bogotá" [ref=e52] [cursor=pointer]
          - button "Limpiar Todo" [ref=e56] [cursor=pointer]
          - button "Salir" [ref=e60] [cursor=pointer]
      - generic [ref=e64]:
        - generic [ref=e66]:
          - paragraph [ref=e67]: Total Reportes
          - paragraph [ref=e68]: "3"
        - generic [ref=e74]:
          - paragraph [ref=e75]: Prioridad Alta
          - paragraph [ref=e76]: "1"
        - generic [ref=e81]:
          - paragraph [ref=e82]: En Despacho / Pendientes
          - paragraph [ref=e83]: "2"
        - generic [ref=e92]:
          - paragraph [ref=e93]: Casos Atendidos
          - paragraph [ref=e94]: "1"
          - paragraph [ref=e95]: 33 % de resolución
      - generic [ref=e100]:
        - generic [ref=e101]:
          - generic [ref=e102]:
            - heading "Mapa Operativo (Centrado en Colombia)" [level=3] [ref=e103]
            - generic [ref=e107]: Clic en un caso de la lista para centrarlo
          - generic [ref=e108]:
            - generic:
              - generic:
                - button "A" [ref=e109] [cursor=pointer]
                - button "M" [ref=e111] [cursor=pointer]
                - button "B" [ref=e113] [cursor=pointer]
            - generic:
              - generic [ref=e115]:
                - button "Zoom in" [ref=e116] [cursor=pointer]: +
                - button "Zoom out" [ref=e117] [cursor=pointer]: −
              - generic [ref=e118]:
                - link "Leaflet" [ref=e119] [cursor=pointer]:
                  - /url: https://leafletjs.com
                - text: "| ©"
                - link "OpenStreetMap" [ref=e124] [cursor=pointer]:
                  - /url: https://www.openstreetmap.org/copyright
        - generic [ref=e125]:
          - generic [ref=e126]:
            - generic [ref=e127]:
              - heading "Despacho de Unidades" [level=3] [ref=e128]
              - generic [ref=e130]: 3 de 3 casos
            - generic [ref=e131]:
              - textbox "Buscar folio, tipo o dirección..." [ref=e132]
              - combobox [ref=e133]:
                - 'option "Prioridad: Todas" [selected]'
                - option "Alta"
                - option "Media"
                - option "Baja"
            - generic [ref=e134]:
              - combobox [ref=e135]:
                - 'option "Estado: Todos" [selected]'
                - option "Pendiente"
                - option "En Despacho"
                - option "Atendido"
              - combobox [ref=e136]:
                - 'option "Tipo: Todos" [selected]'
                - option "Robo / Asalto"
                - option "Robo a Vehículo"
                - option "Vandalismo"
                - option "Violencia Intrafamiliar"
                - option "Actividad Sospechosa"
                - option "Otro"
              - combobox [ref=e137]:
                - option "Más recientes" [selected]
                - option "Más antiguos"
                - option "Por prioridad"
          - generic [ref=e138]:
            - generic [ref=e139] [cursor=pointer]:
              - generic [ref=e140]:
                - generic [ref=e141]: REP-1001
                - generic [ref=e143]: Alta
              - generic [ref=e144]: Robo / Asalto
              - generic [ref=e145]: Av. Caracas con Calle 45, Bogotá
              - generic [ref=e149]:
                - generic [ref=e150]: En Despacho · hace 26 d
                - generic [ref=e151]: Ver detalles →
            - generic [ref=e152] [cursor=pointer]:
              - generic [ref=e153]:
                - generic [ref=e154]: REP-1002
                - generic [ref=e156]: Media
              - generic [ref=e157]: Actividad Sospechosa
              - generic [ref=e158]: Parque de la 93, Bogotá
              - generic [ref=e162]:
                - generic [ref=e163]: Pendiente · hace 27 d
                - generic [ref=e164]: Ver detalles →
            - generic [ref=e165] [cursor=pointer]:
              - generic [ref=e166]:
                - generic [ref=e167]: REP-1003
                - generic [ref=e169]: Baja
              - generic [ref=e170]: Vandalismo
              - generic [ref=e171]: Carrera 7 con Calle 72, Bogotá
              - generic [ref=e175]:
                - generic [ref=e176]: Atendido · hace 28 d
                - generic [ref=e177]: Ver detalles →
      - generic [ref=e178]:
        - heading "Analítica Estadística de Incidentes" [level=3] [ref=e179]
        - generic [ref=e182]:
          - paragraph [ref=e184]: Por tipo
          - paragraph [ref=e188]: Por estado
          - paragraph [ref=e192]: Por prioridad
  - contentinfo [ref=e195]:
    - generic [ref=e196]:
      - paragraph [ref=e197]: Desarrollado por
      - generic [ref=e198]:
        - generic [ref=e199]: Sergio Dario Ordoñez Aguilera
        - generic [ref=e200]: •
        - generic [ref=e201]: Juan Camilo Perez Chivata
        - generic [ref=e202]: •
        - generic [ref=e203]: Jonathan David Bohorquez Maldonado
      - paragraph [ref=e204]: © 2026 AlertaCiudadana - Sistema de Reporte de Delitos Urbano (Colombia)
```