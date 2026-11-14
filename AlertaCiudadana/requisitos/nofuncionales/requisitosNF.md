# Requerimientos No Funcionales (RNF)

## RNF-01: Persistencia Local y Compresión de Imágenes
- **ID:** RNF-01
- **Descripción:** El sistema debe almacenar los reportes de forma autónoma en el navegador (`localStorage` bajo la clave `delitos_colombia_db`) y comprimir automáticamente las fotografías adjuntas a un máximo de 800 px de lado mayor en formato JPEG al 70% de calidad para evitar desbordar la cuota de almacenamiento.
- **Versión:** 1.0
- **Prioridad:** Alta
- **Responsable:** Jonathan David Bohorquez Maldonado
- **Estado:** Validado
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given una imagen adjunta superior a 2 MB y 2000 px de ancho, When se procesa en el formulario, Then se redimensiona proporcionalmente a máx. 800 px y se almacena sin generar error de cuota.

---

## RNF-02: Seguridad contra Inyección XSS
- **ID:** RNF-02
- **Descripción:** Toda cadena de texto ingresada por el usuario (ubicación, descripción, nombre, notas de bitácora) debe ser sanitizada mediante escape de caracteres HTML (`&`, `<`, `>`, `"`, `'`) antes de ser renderizada en el DOM para prevenir ataques Cross-Site Scripting (XSS).
- **Versión:** 1.0
- **Prioridad:** Alta
- **Responsable:** Sergio Dario Ordoñez Aguilera
- **Estado:** Validado
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given una descripción con etiquetas `<script>alert(1)</script>`, When el reporte se visualiza en el listado o modal del CAD, Then el texto se muestra literalmente como cadena escapada sin ejecutar código JavaScript.

---

## RNF-03: Usabilidad Responsiva y Tema Oscuro Persistente
- **ID:** RNF-03
- **Descripción:** La interfaz debe adaptarse sin desbordamiento horizontal desde pantallas móviles (360x800 px) hasta escritorio (1920x1080 px) e incluir un selector de modo claro/oscuro persistente (`ac_theme`) que adapte los estilos de tarjetas, mapas Leaflet y gráficos Chart.js.
- **Versión:** 1.1
- **Prioridad:** Baja
- **Responsable:** Juan Camilo Perez Chivata
- **Estado:** Validado
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given un usuario que activa el botón de modo oscuro, When recarga la página o cambia de pestaña, Then el sistema conserva la preferencia visual en `localStorage` y adapta los colores de los gráficos y el mapa.