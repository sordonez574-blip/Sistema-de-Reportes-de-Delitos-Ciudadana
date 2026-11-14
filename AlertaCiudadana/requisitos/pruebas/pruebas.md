# Plan y Casos de Prueba (Criterios de Aceptación Given - When - Then)

Este documento contiene los casos de prueba funcionales (`TC-01` a `TC-05`) y no funcionales (`TC-06` a `TC-08`) derivados de los criterios de aceptación del proyecto **AlertaCiudadana**.

---

## TC-01: Registro de Reporte Ciudadano (`RF-01`)
- **Caso 1.1 (Exitoso):**
  - **Given:** Un ciudadano en la vista "Reportar Incidente" con todos los campos obligatorios diligenciados y coordenadas fijadas en Bogotá.
  - **When:** Presiona el botón `"Enviar Reporte al Sistema"`.
  - **Then:** El sistema almacena el reporte en `localStorage`, genera un folio único con formato `REP-XXXX`, muestra la notificación de éxito y precarga el folio en el buscador.
- **Caso 1.2 (Alternativo - Denuncia Anónima):**
  - **Given:** Un ciudadano que marca la casilla `"Realizar Denuncia Anónima"`.
  - **When:** Envía el formulario sin llenar nombre ni teléfono.
  - **Then:** El sistema deshabilita los campos personales y guarda el reporte con `userName: "Anónimo"` y `userPhone: "N/A"`.
- **Caso 1.3 (Error - Teléfono Inválido):**
  - **Given:** Un ciudadano con denuncia identificada que ingresa un número celular que no inicia en `3` o no tiene 10 dígitos (ej. `123456`).
  - **When:** Intenta enviar el formulario.
  - **Then:** El sistema cancela el envío y muestra la alerta `"Teléfono inválido: 10 dígitos iniciando en 3"`.

---

## TC-02: Consulta de Estado por Folio (`RF-02`)
- **Caso 2.1 (Exitoso):**
  - **Given:** Un reporte registrado en el sistema con folio `REP-1001` en estado `"En Despacho"`.
  - **When:** El ciudadano escribe `rep-1001` en el campo de consulta y pulsa `"Buscar"`.
  - **Then:** El sistema convierte el texto a mayúsculas y muestra el tipo de incidente, estado actual, prioridad y último registro de bitácora.
- **Caso 2.2 (Alternativo - Tecla Enter):**
  - **Given:** Un usuario que digita un folio válido dentro del campo `#folioInput`.
  - **When:** Presiona la tecla `Enter`.
  - **Then:** El sistema ejecuta `consultFolio()` y despliega los datos del reporte.
- **Caso 2.3 (Error - Folio Inexistente):**
  - **Given:** Un código no registrado como `REP-9999`.
  - **When:** El usuario ejecuta la búsqueda.
  - **Then:** El sistema muestra en color rojo `"No se encontró ese folio."`.

---

## TC-03: Control de Acceso al Centro de Mando (`RF-03`)
- **Caso 3.1 (Exitoso):**
  - **Given:** Un operador sin sesión activa que hace clic en `"Centro de Mando (CAD)"`.
  - **When:** Ingresa el PIN autorizado (`1234`) y pulsa `"Ingresar"`.
  - **Then:** El sistema guarda `cad_ok=1` en `sessionStorage`, cierra el modal y muestra el dashboard operativo.
- **Caso 3.2 (Alternativo - Sesión Persistente en Pestaña):**
  - **Given:** Un operador ya autenticado que regresa temporalmente a `"Reportar Incidente"`.
  - **When:** Vuelve a seleccionar `"Centro de Mando (CAD)"`.
  - **Then:** El sistema omite la solicitud de PIN y abre directamente el panel CAD.
- **Caso 3.3 (Error - PIN Incorrecto):**
  - **Given:** Un usuario en el modal de autenticación `#pinModal`.
  - **When:** Ingresa una clave errónea (ej. `0000`).
  - **Then:** El sistema bloquea el acceso, limpia el campo de contraseña y muestra la alerta `"PIN incorrecto"`.

---

## TC-04: Gestión y Cambio de Estado en CAD (`RF-04`)
- **Caso 4.1 (Exitoso):**
  - **Given:** Un operador dentro del expediente de un reporte en estado `"Pendiente"`.
  - **When:** Hace clic en el botón `"En Despacho"`.
  - **Then:** El sistema actualiza el estado, registra `"Estado: Pendiente → En Despacho"` con marca de tiempo en la bitácora y recalcula los indicadores del tablero.
- **Caso 4.2 (Alternativo - Agregar Nota Operativa):**
  - **Given:** Un operador que escribe `"Unidad cuadrante 15 en ruta"` en el campo de notas del expediente.
  - **When:** Pulsa `"Agregar"`.
  - **Then:** La nota se anexa a la bitácora del caso sin modificar su estado actual.
- **Caso 4.3 (Error - Nota Vacía):**
  - **Given:** Un operador con el campo de nota vacío o solo con espacios en blanco.
  - **When:** Pulsa `"Agregar"`.
  - **Then:** El sistema ignora la acción y no inserta líneas vacías en la bitácora.

---

## TC-05: Alerta SLA y Exportación de Datos (`RF-05`)
- **Caso 5.1 (Exitoso - Alerta SLA):**
  - **Given:** Un reporte con prioridad `"Alta"` y estado `"Pendiente"` cuya hora de creación supera los 30 minutos respecto a la hora actual.
  - **When:** Se carga o refresca el dashboard del CAD.
  - **Then:** La tarjeta del reporte se resalta con borde rojo y muestra el indicador parpadeante `⚠ SLA`.
- **Caso 5.2 (Exitoso - Exportación CSV/JSON):**
  - **Given:** Al menos un reporte almacenado en el sistema.
  - **When:** El operador presiona el botón `"CSV"` o `"Respaldo JSON"`.
  - **Then:** El navegador descarga automáticamente el archivo `reportes_alertaciudadana.csv` o `respaldo_alertaciudadana.json` con todos los registros.

---

## TC-06 a TC-08: Pruebas de Requerimientos No Funcionales
- **TC-06 (`RNF-01` - Compresión de Imagen):** Given una fotografía de 4 MB y 3000 px de ancho adjuntada en el formulario, When se carga en `#crimeImage`, Then `compressImage()` la convierte a JPEG (calidad 0.7) con lado mayor de 800 px antes de guardarla en `localStorage`.
- **TC-07 (`RNF-02` - Prevención XSS):** Given una descripción con código malicioso `<script>alert('XSS')</script>`, When se renderiza en el listado o modal del CAD, Then la función `esc()` convierte los caracteres `<` y `>` en entidades HTML seguras sin ejecutar el script.
- **TC-08 (`RNF-03` - Tema Oscuro Persistente):** Given un usuario que activa el botón de modo oscuro en el encabezado, When recarga el navegador, Then la clase `dark` se mantiene activa mediante `localStorage.getItem('ac_theme')` y actualiza tanto los estilos como los gráficos Chart.js.