# Registro de Control de Cambios

## CR-01: Confirmación persistente de Folio tras envío de reporte
- **ID:** CR-01
- **Requerimiento afectado:** RF-01 (v1.1 -> v1.2)
- **Solicitante:** Usuario participante en prueba de validación
- **Prioridad:** Media
- **Impacto:** Medio (Interfaz ciudadana, `handleFormSubmit()`, `TC-01`)
- **Estado:** Aprobado
- **Descripción:** Mantener visible en pantalla el folio generado (`REP-XXXX`) con opción de copiado tras enviar el formulario, evitando que el usuario lo pierda cuando desaparece el toast de notificación.

## CR-SEG-01: Remediación de exposición de PIN en cliente
- **ID:** CR-SEG-01
- **Requerimientos afectados:** RF-03 (v1.0 -> v1.1) y creación de RNF-04 (v1.0)
- **Solicitante:** Auditoría de Seguridad
- **Prioridad:** Alta
- **Impacto:** Alto (Autenticación CAD, `checkPin()`, `TC-03`)
- **Estado:** Aprobado
- **Descripción:** Eliminar el PIN estático en texto plano (`PIN = '1234'`) del código fuente cliente e implementar verificación segura con bloqueo temporal tras 3 intentos fallidos.