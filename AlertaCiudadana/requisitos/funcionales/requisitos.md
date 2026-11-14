# Requerimientos Funcionales (RF)

## RF-01: Registro de Incidente Urbano
- **ID:** RF-01
- **Descripción:** El sistema debe permitir al ciudadano registrar un incidente urbano especificando tipo de delito, nivel de prioridad, fecha/hora (no futura), ubicación (texto, GPS o clic en mini-mapa), descripción (máx. 500 caracteres), evidencia fotográfica y modalidad anónima o identificada (validando teléfono colombiano de 10 dígitos iniciando en 3), alertando duplicados en un radio de 150 m y generando un folio único `REP-XXXX`.
- **Versión:** 1.2
- **Prioridad:** Alta
- **Responsable:** Sergio Dario Ordoñez Aguilera
- **Estado:** Validado
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given un ciudadano en la vista "Reportar Incidente" con datos válidos y ubicación fijada, When pulsa "Enviar Reporte al Sistema", Then el sistema almacena el caso en `localStorage`, genera un folio único `REP-XXXX` y muestra confirmación visual.

---

## RF-02: Consulta de Estado por Folio
- **ID:** RF-02
- **Descripción:** El sistema debe permitir al ciudadano consultar el estado actual (`Pendiente`, `En Despacho`, `Atendido`), prioridad y último movimiento registrado en la bitácora mediante el ingreso de su código de folio `REP-XXXX`.
- **Versión:** 1.0
- **Prioridad:** Media
- **Responsable:** Juan Camilo Perez Chivata
- **Estado:** Validado
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given un folio existente `REP-1001`, When el usuario lo ingresa en el buscador ciudadano y presiona "Buscar" o `Enter`, Then el sistema muestra el estado actualizado y su último movimiento.

---

## RF-03: Control de Acceso al Centro de Mando (CAD)
- **ID:** RF-03
- **Descripción:** El sistema debe restringir el acceso al módulo Centro de Mando (CAD) mediante la validación de un PIN de operador antes de visualizar los reportes, manteniendo la sesión activa por pestaña (`sessionStorage`) y permitiendo cerrar sesión manualmente.
- **Versión:** 1.1
- **Prioridad:** Alta
- **Responsable:** Jonathan David Bohorquez Maldonado
- **Estado:** En desarrollo (Pendiente remediación CR-SEG-01)
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given un operador sin sesión activa que selecciona "Centro de Mando (CAD)", When ingresa el PIN correcto, Then el sistema habilita el panel operativo; si es incorrecto, deniega el ingreso y notifica el error.

---

## RF-04: Gestión, Filtrado y Despacho de Incidentes en CAD
- **ID:** RF-04
- **Descripción:** El sistema debe permitir al operador visualizar los reportes georreferenciados en un mapa operativo (Leaflet), filtrarlos (por texto, prioridad, estado y tipo), abrir su expediente, agregar notas de seguimiento y actualizar su estado (`Pendiente`, `En Despacho`, `Atendido`) registrando cada cambio en la bitácora.
- **Versión:** 1.0
- **Prioridad:** Alta
- **Responsable:** Sergio Dario Ordoñez Aguilera
- **Estado:** Validado
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given un operador autenticado en el CAD, When cambia el estado de un caso de "Pendiente" a "En Despacho", Then el sistema actualiza los indicadores estadísticos y registra el cambio con fecha y hora en la bitácora.

---

## RF-05: Alerta de SLA y Exportación de Datos
- **ID:** RF-05
- **Descripción:** El sistema debe alertar visualmente (`⚠ SLA`) cuando un reporte de prioridad "Alta" en estado "Pendiente" supere los 30 minutos sin atención (refrescando cada 60 segundos), y permitir exportar la base de datos de reportes en formatos CSV y JSON.
- **Versión:** 1.0
- **Prioridad:** Media
- **Responsable:** Jonathan David Bohorquez Maldonado
- **Estado:** Validado
- **Fecha:** 2026-11-12
- **Criterio de aceptación:** Given un reporte de prioridad "Alta" en estado "Pendiente" con más de 30 minutos transcurridos, When se visualiza en el listado del CAD, Then muestra la etiqueta parpadeante `⚠ SLA` y permite descargar el respaldo en `.csv` o `.json`.