# Business-Valuation
This repository contains the code and presentation material of the Business Valuation with Discounted Cash Flow In Python Series [tutorial](https://youtube.com/playlist?list=PLHSKzVSgP0i1ZwkyrZBQdtC_g6kYVWoe6&si=YJCLTagPy0A_n198) on YouTube. If you already know how to value companies, then for instruction on how to use the model, please refer to the [Part 4](https://www.youtube.com/watch?v=eg61_-cLDhA) and [Part 5](https://youtu.be/30uh1YBrsQ0) of the series. I have built this DCF model based on the valuation methods taught by Dr. Aswath Damodaran at NYU. 

[Here is Business-Valuation-with-Discounted-Cash-Flow-In-Python.pynb in colab.
](https://colab.research.google.com/drive/1XtCNkpbfSoiMXpypcJ3DOzXBZy4jRzn_?usp=sharing)
## What is the series about?
In this series, I will walk you through a Discounted Cash Flow Model implemented in Python to value any cash-generative asset. That will include any business publicly traded companies i.e. stocks of companies on the stock market or privately owned businesses. I will be covering high-level concepts of Valuations and Corporate Finance to set the stage for going over the DCF model in Python. Discounted cash flow a.k.a. DCF refers to a valuation method that estimates the value of an investment using its expected future cash flows. DCF analysis attempts to determine the value of an asset today, based on projections of how much money that investment will generate in the future. In the last session of this series, I will walk you through a Monte Carlo Discounted Cash Flow Simulation to probabilistically deal with the uncertainty of utilizing a DCF model.
The link to the Colab file which contains presentation material, the DCF model, and its underlying code can be found [here](https://colab.research.google.com/drive/1XtCNkpbfSoiMXpypcJ3DOzXBZy4jRzn_?usp=sharing)

## Mapa de oleoductos de Colombia
El repositorio incluye ahora un script ligero para generar un mapa interactivo en formato HTML con las principales líneas de transporte de crudo y derivados en Colombia, indicando para cada oleoducto su capacidad y tarifa de transporte aproximada.

### Requisitos
- Python 3.10+
- No se necesitan dependencias adicionales: el script genera el HTML con librerías estándar y utiliza Leaflet desde una CDN.

### Cómo generar el mapa
```bash
python scripts/generate_colombia_pipeline_map.py
```
El script produce el archivo `outputs/colombia_pipelines_map.html`, que puedes abrir en cualquier navegador moderno para visualizar los trazados, capacidades y tarifas en los popups de cada ducto.
