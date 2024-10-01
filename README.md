# MetaGames Kedro Project

## Overview

Este es un proyecto de Kedro diseñado para gestionar un caso de aprendizaje automático relacionado con la plataforma **MetaGames**. El objetivo principal es automatizar el proceso de preparación de la información y el entrenamiento de modelos para mejorar las recomendaciones de videojuegos para los usuarios.

## Estructura del Proyecto

El proyecto incluye:

- **Notebooks de Jupyter:** Documentos que contienen análisis, visualizaciones y explicaciones detalladas de cada fase del proceso.
- **Automatización del Proceso:** Configuración de pipelines para el manejo de datos y entrenamiento de modelos.
- **Documentación:** Archivos README y otras instrucciones para facilitar la comprensión y uso del proyecto.

## Instrucciones para la Configuración

Para ejecutar este proyecto, siga estos pasos:

1. **Activar el ambiente virtual:**
   ```bash
   venv\Scripts\activate
   ```

2. **Instalar todas las dependencias necesarias:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Abrir el notebook del "Informe Técnico - MetaGames":**
   Navegue a `kedro-project/notebooks` para acceder al informe técnico.

4. **Desactivar el ambiente virtual cuando haya terminado:**
   ```bash
   deactivate
   ```

## Cómo Ejecutar el Pipeline de Kedro

Para ejecutar su proyecto de Kedro, utilice el siguiente comando:

```bash
kedro run
```

Esto ejecutará todas las etapas definidas en el pipeline.

## Cómo Probar Su Proyecto Kedro

Revise los archivos `src/tests/test_run.py` y `src/tests/pipelines/data_science/test_pipeline.py` para instrucciones sobre cómo escribir y ejecutar pruebas. Para ejecutar las pruebas, utilice:

```bash
pytest
```

## Documentación y Recursos

Para obtener más información sobre cómo utilizar Kedro y trabajar con notebooks, consulte la [documentación oficial de Kedro](https://docs.kedro.org). 

### Notebooks y Kedro

Para trabajar con notebooks en su proyecto Kedro, asegúrese de que Jupyter esté instalado:

```bash
pip install jupyter
```

Después de la instalación, puede iniciar un servidor local de Jupyter:

```bash
kedro jupyter notebook
```

### Ignorar Salidas de Notebooks en Git

Para eliminar automáticamente el contenido de las celdas de salida antes de realizar commits en Git, puede usar herramientas como [`nbstripout`](https://github.com/kynan/nbstripout). Por ejemplo, agregue un hook en `.git/config` con:

```bash
nbstripout --install
```

Esto se ejecutará antes de cualquier commit.

## Contribuciones

Si desea contribuir a este proyecto, por favor haga un fork del repositorio y envíe un pull request con sus cambios. Asegúrese de seguir las directrices de codificación y de documentación.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulte el archivo `LICENSE` para más detalles.
