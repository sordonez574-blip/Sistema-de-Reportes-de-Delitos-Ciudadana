import pandas as pd
import matplotlib.pyplot as plt

# Lista de solicitudes de cambio (CR) del proyecto AlertaCiudadana
cambios = [
    {
        "id": "CR-00A",
        "requisito": "RF-01",
        "descripcion": "Localización Colombia (líneas 123, 155, 165) y flujo de 3 estados",
        "version_anterior": "0.9",
        "version_nueva": "1.0",
        "prioridad": "Alta",
        "impacto": "Alto",
        "estado": "Aprobado"
    },
    {
        "id": "CR-00B",
        "requisito": "RF-04",
        "descripcion": "Mini-mapa ciudadano, consulta por folio, bitácora y exportación CSV/JSON",
        "version_anterior": "1.0",
        "version_nueva": "1.1",
        "prioridad": "Alta",
        "impacto": "Alto",
        "estado": "Aprobado"
    },
    {
        "id": "CR-01",
        "requisito": "RF-01",
        "descripcion": "Comprobante persistente de folio, barra de progreso y confirmación GPS",
        "version_anterior": "1.1",
        "version_nueva": "1.2",
        "prioridad": "Alta",
        "impacto": "Medio",
        "estado": "Aprobado"
    },
    {
        "id": "CR-SEG-01",
        "requisito": "RNF-04",
        "descripcion": "Hash SHA-256 para PIN CAD y bloqueo de 60s tras 3 intentos fallidos",
        "version_anterior": "1.1",
        "version_nueva": "1.2",
        "prioridad": "Crítica",
        "impacto": "Alto",
        "estado": "Aprobado"
    },
    {
        "id": "CR-02",
        "requisito": "RF-06",
        "descripcion": "Notificaciones push por SMS al ciudadano ante cambio de estado",
        "version_anterior": "1.2",
        "version_nueva": "2.0",
        "prioridad": "Media",
        "impacto": "Alto",
        "estado": "Rechazado"
    },
    {
        "id": "CR-03",
        "requisito": "RF-01",
        "descripcion": "Adjuntar evidencia en video MP4 de hasta 50 MB en localStorage",
        "version_anterior": "1.2",
        "version_nueva": "2.0",
        "prioridad": "Baja",
        "impacto": "Alto",
        "estado": "Rechazado"
    },
    {
        "id": "CR-04",
        "requisito": "RF-04",
        "descripcion": "Sincronización en nube con backend REST/PostgreSQL para despacho regional",
        "version_anterior": "1.2",
        "version_nueva": "2.0",
        "prioridad": "Media",
        "impacto": "Alto",
        "estado": "Pendiente"
    }
]

# Conversión a DataFrame de Pandas
df = pd.DataFrame(cambios)

# Cálculo automático de métricas requeridas
total_cambios = len(df)
aprobados = (df["estado"] == "Aprobado").sum()
rechazados = (df["estado"] == "Rechazado").sum()
pendientes = (df["estado"] == "Pendiente").sum()
por_prioridad = df["prioridad"].value_counts()
req_modificados = df["requisito"].value_counts()

print("=== TABLA DE CONTROL DE CAMBIOS (DATAFRAME) ===")
print(df[["id", "requisito", "version_anterior", "version_nueva", "prioridad", "impacto", "estado"]].to_string(index=False))

print("\n=== MÉTRICAS AUTOMÁTICAS ===")
print(f"- Cantidad total de cambios : {total_cambios}")
print(f"- Cambios aprobados         : {aprobados}")
print(f"- Cambios rechazados        : {rechazados}")
print(f"- Cambios pendientes        : {pendientes}")
print("\n- Cambios por prioridad:")
print(por_prioridad.to_string())
print("\n- Requerimientos más modificados:")
print(req_modificados.to_string())

# Generación de 3 gráficos estadísticos
fig, axes = plt.subplots(1, 3, figsize=(15, 4.5))
fig.suptitle("Control de Cambios - Sistema AlertaCiudadana", fontsize=13, fontweight="bold")

# Gráfico 1: Cambios por Estado
conteo_estado = df["estado"].value_counts().reindex(["Aprobado", "Pendiente", "Rechazado"], fill_value=0)
colores_estado = ["#10b981", "#f59e0b", "#ef4444"]
bars1 = axes[0].bar(conteo_estado.index, conteo_estado.values, color=colores_estado, edgecolor="#1e293b")
axes[0].set_title("Cambios por Estado")
axes[0].set_ylabel("Cantidad de CR")
axes[0].set_ylim(0, max(conteo_estado.values) + 1)
for b in bars1:
    axes[0].text(b.get_x() + b.get_width()/2, b.get_height() + 0.1, int(b.get_height()), ha="center", fontweight="bold")

# Gráfico 2: Distribución por Prioridad
orden_prio = ["Crítica", "Alta", "Media", "Baja"]
conteo_prio = df["prioridad"].value_counts().reindex(orden_prio, fill_value=0)
colores_prio = ["#7f1d1d", "#dc2626", "#f59e0b", "#3b82f6"]
axes[1].pie(
    conteo_prio[conteo_prio > 0],
    labels=conteo_prio[conteo_prio > 0].index,
    autopct="%1.1f%%",
    startangle=140,
    colors=[colores_prio[orden_prio.index(k)] for k in conteo_prio[conteo_prio > 0].index]
)
axes[1].set_title("Distribución por Prioridad")

# Gráfico 3: Requerimientos más modificados
bars3 = axes[2].barh(req_modificados.index[::-1], req_modificados.values[::-1], color="#2563eb", edgecolor="#1e293b")
axes[2].set_title("Requerimientos Más Modificados")
axes[2].set_xlabel("Cantidad de CR")
axes[2].set_xlim(0, max(req_modificados.values) + 1)
for b in bars3:
    axes[2].text(b.get_width() + 0.1, b.get_y() + b.get_height()/2, int(b.get_width()), va="center", fontweight="bold")

plt.tight_layout()
plt.savefig("control_cambios_alertaciudadana.png", dpi=150)
plt.show()