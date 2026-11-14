# Especificación de Casos de Uso - AlertaCiudadana (Colombia)

Este documento detalla los casos de uso principales del sistema autónomo de gestión de incidentes urbanos, vinculados directamente a los requerimientos funcionales (`RF-01` a `RF-05`) y no funcionales (`RNF-01` a `RNF-03`).

---

## CU-01: Registrar Incidente Urbano
- **Requerimientos asociados:** `RF-01`, `RNF-01`, `RNF-02`
- **Actor principal:** Ciudadano
- **Precondiciones:** El usuario se encuentra en la pestaña "Reportar Incidente" (`#view-citizen`).
- **Flujo Normal:**
  1. El ciudadano selecciona el **Tipo de Delito / Incidente** y el **Nivel de Prioridad** (`Baja`, `Media`, `Alta`).
  2. El sistema precarga la fecha y hora local actual; el ciudadano la confirma o ajusta (sin superar la fecha/hora actual).
  3. El ciudadano ingresa la dirección manualmente, usa el botón **GPS** o hace clic en el **mini-mapa** (`#miniMap`) para fijar las coordenadas exactas.
  4. El ciudadano redacta la descripción de los hechos (máx. 500 caracteres) y opcionalmente adjunta una imagen (que el sistema comprime a máx. 800 px en formato JPEG).
  5. El ciudadano elige entre **Denuncia Anónima** o ingresa su nombre y teléfono móvil colombiano (`3XXXXXXXXX`).
  6. El ciudadano pulsa **"Enviar Reporte al Sistema"**.
  7. El sistema verifica que no existan reportes activos similares en un radio de 150 m en las últimas 24 horas, genera un folio único `REP-XXXX`, almacena el registro en `localStorage` y muestra la confirmación al usuario.
- **Flujos Alternativos / Excepciones:**
  - *3a. Sin ubicación seleccionada:* El sistema asigna por defecto las coordenadas centrales de Bogotá (`4.6097, -74.0817`).
  - *5a. Teléfono inválido o fecha futura:* El sistema bloquea el registro y muestra una alerta (`toast`) indicando el error de validación.
  - *7a. Reporte duplicado detectado:* El sistema solicita confirmación explícita antes de crear un nuevo registro.
- **Postcondiciones:** El reporte queda guardado con estado inicial `"Pendiente"` y su folio se precarga en el módulo de consulta ciudadana.

---

## CU-02: Consultar Estado de Reporte por Folio
- **Requerimientos asociados:** `RF-02`, `RNF-02`
- **Actor principal:** Ciudadano
- **Precondiciones:** El ciudadano cuenta con un código de folio previamente generado (`REP-XXXX`).
- **Flujo Normal:**
  1. El ciudadano ubica la tarjeta **"Consultar Estado de mi Reporte"** en la vista principal.
  2. Ingresa el código del folio (ej. `REP-1001`) y presiona el botón **"Buscar"** o la tecla `Enter`.
  3. El sistema normaliza el texto a mayúsculas, busca el registro en `localStorage` y despliega el tipo de delito, estado actual (`Pendiente`, `En Despacho` o `Atendido`), prioridad y el último movimiento registrado en la bitácora.
- **Flujos Alternativos / Excepciones:**
  - *3a. Folio inexistente:* El sistema muestra el mensaje de error `"No se encontró ese folio."`.
- **Postcondiciones:** El ciudadano conoce el estado actual de atención de su denuncia.

---

## CU-03: Autenticar Operador en Centro de Mando (CAD)
- **Requerimientos asociados:** `RF-03`
- **Actor principal:** Operador CAD / Autoridad
- **Precondiciones:** El operador no posee una sesión activa en la pestaña actual del navegador.
- **Flujo Normal:**
  1. El operador hace clic en la pestaña **"Centro de Mando (CAD)"** en la barra superior.
  2. El sistema despliega el modal de acceso restringido (`#pinModal`).
  3. El operador digita el PIN de seguridad y presiona **"Ingresar"** o la tecla `Enter`.
  4. El sistema valida el PIN, registra la sesión en `sessionStorage` (`cad_ok = 1`) y habilita la vista operativa `#view-police`.
- **Flujos Alternativos / Excepciones:**
  - *4a. PIN incorrecto:* El sistema deniega el acceso, limpia el campo de entrada y muestra la alerta `"PIN incorrecto"`.
- **Postcondiciones:** El operador tiene acceso al mapa operativo, listado de despacho y analítica estadística.

---

## CU-04: Gestionar, Filtrar y Despachar Incidentes en el CAD
- **Requerimientos asociados:** `RF-04`, `RF-05`, `RNF-02`, `RNF-03`
- **Actor principal:** Operador CAD
- **Precondiciones:** El operador se encuentra autenticado dentro del Centro de Mando (`#view-police`).
- **Flujo Normal:**
  1. El sistema muestra las tarjetas de resumen estadístico, el mapa operativo con marcadores por color de prioridad y la lista de casos.
  2. El operador filtra los incidentes por texto (folio, tipo o dirección), prioridad, estado o tipo de delito.
  3. El operador selecciona un caso de la lista; el mapa centra la ubicación (`flyTo`) y se abre el modal de expediente (`#detailModal`).
  4. El operador agrega una nota de seguimiento y cambia el estado del caso a `"En Despacho"` o `"Atendido"`.
  5. El sistema actualiza los contadores, gráficos Chart.js y registra el movimiento con fecha y hora en la bitácora del reporte.
- **Flujos Alternativos / Excepciones:**
  - *1a. Incumplimiento de SLA:* Si un reporte de prioridad `"Alta"` en estado `"Pendiente"` supera los 30 minutos sin atención, el sistema resalta la tarjeta con la alerta parpadeante `⚠ SLA`.
  - *2a. Exportación de datos:* El operador puede descargar en cualquier momento los reportes filtrados/almacenados en formato `.csv` o `.json`.
- **Postcondiciones:** El estado del incidente y su trazabilidad en bitácora quedan actualizados en `localStorage`.