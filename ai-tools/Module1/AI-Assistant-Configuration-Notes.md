# AI Assistant Configuration Notes

Este documento describe cómo se configuró el asistente de código en relación con la seguridad, la privacidad y otros aspectos (telemetría, uso de datos, etc.).

## Revisión de Configuraciones y Telemetría

- **Estado actual**:

  - Se ha **deshabilitado** la opción “Enviar fragmentos de código a la nube” (o equivalente).
  - Se ha **deshabilitado** (o reducido) la telemetría si la herramienta ofrecía esta configuración.
  - Hemos verificado que **no** se envían credenciales o variables sensibles al asistente de manera automática.

- **Razón**:
  - Cumplir con las políticas de seguridad de la organización.
  - Minimizar riesgos de exposición de código privado.
  - Controlar costos (si se paga por tokens o llamadas a la API) y uso de datos personales.

## Pasos Realizados

1. **Abrir la configuración del asistente**

   - Ejemplo en VS Code: Extensiones → [Tu asistente] → Configuración/Settings.
   - Ejemplo en IntelliJ/JetBrains: Settings → Plugins → [Tu asistente] → Preferences/Configure plugin.

2. **Desactivar Telemetría y Envío de Código**

   - Buscamos opciones como “Send code to the cloud” o “Telemetry”.
   - Ajustamos a “disabled” o “off”.
   - Guardamos y/o reiniciamos la herramienta según instrucciones.

3. **Verificar Estado Tras Reinicio**

   - Se recargó la IDE.
   - Se comprobó que el asistente sigue funcionando, aunque las sugerencias pueden ser menos personalizadas.

4. **Documentar Configuración**
   - Este archivo (ASSISTANT_CONFIG_NOTES.md) es el registro oficial de los cambios y el porqué se hicieron.

## Consideraciones Adicionales

- **Costo**:

  - Si el asistente cobra por uso de tokens/tiempo, monitoreamos en la cuenta o panel de la herramienta.
  - Podemos establecer alertas o límites en la facturación.

- **Seguridad Avanzada**:

  - Para repositorios muy sensibles, se evalúa un modelo on-premise (autohospedado) para que los datos no salgan de la red.
  - Se usan scripts internos para evitar compartir accidentalmente claves o tokens con la IA.

- **Ética y Responsabilidad**:
  - Asegurarse de revisar manualmente el código sugerido por la IA para evitar violaciones de licencias o uso indebido.
  - No aceptar sugerencias que contengan datos personales o partes de código propietario que no te pertenezcan.

## Referencias

- [GitHub Copilot Docs](https://docs.github.com/en/github/copilot)
- [Tabnine Docs](https://www.tabnine.com/docs)
- [Amazon CodeWhisperer Docs](https://docs.aws.amazon.com/codewhisperer/latest/userguide/what-is.html)

---

### Futuras Mejoras

- Revisar periódicamente la configuración de la herramienta cuando salgan nuevas versiones.
- Considerar la actualización de políticas internas si la organización cambia de proveedor o se modifica la estrategia de privacidad.
