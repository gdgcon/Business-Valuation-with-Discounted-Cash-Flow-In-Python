"""Genera un mapa interactivo con los principales oleoductos colombianos."""
from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import List

DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "colombia_pipelines.csv"
OUTPUT_PATH = Path(__file__).resolve().parents[1] / "outputs" / "colombia_pipelines_map.html"

COLOR_PALETTE = [
    "#003f5c",
    "#58508d",
    "#bc5090",
    "#ff6361",
    "#ffa600",
    "#2f4b7c",
    "#665191",
    "#a05195",
]


def load_data() -> List[dict]:
    with DATA_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = []
        for row in reader:
            row["start_lat"] = float(row["start_lat"])
            row["start_lon"] = float(row["start_lon"])
            row["end_lat"] = float(row["end_lat"])
            row["end_lon"] = float(row["end_lon"])
            row["capacity_bpd"] = int(float(row["capacity_bpd"]))
            row["tariff_usd_per_bbl"] = float(row["tariff_usd_per_bbl"])
            row["length_km"] = float(row["length_km"])
            rows.append(row)
    return rows


def build_html(pipelines: List[dict]) -> str:
    pipelines_json = json.dumps(pipelines, ensure_ascii=False)
    colors_json = json.dumps(COLOR_PALETTE)
    return f"""<!DOCTYPE html>
<html lang=\"es\">
  <head>
    <meta charset=\"utf-8\" />
    <title>Oleoductos de Colombia</title>
    <link
      rel=\"stylesheet\"
      href=\"https://unpkg.com/leaflet@1.9.4/dist/leaflet.css\"
      integrity=\"sha256-sA+rq3kG8zp0wHn6kF2zxb9S+V4Ee7dB37R0C6tGI3s=\"
      crossorigin=\"\"
    />
    <script
      src=\"https://unpkg.com/leaflet@1.9.4/dist/leaflet.js\"
      integrity=\"sha256-o9N1j7kP5JbQ8J3G1Jd3zyuCsQ1Ulu0wG3oJo0i0X+Q=\"
      crossorigin=\"\"
    ></script>
    <style>
      body, html {{ margin: 0; height: 100%; }}
      #map {{ width: 100%; height: 100%; }}
      .leaflet-tooltip {{ font-size: 12px; }}
    </style>
  </head>
  <body>
    <div id=\"map\"></div>
    <script>
      const pipelines = {pipelines_json};
      const colors = {colors_json};
      const map = L.map('map').setView([4.6, -74.2], 5);
      L.tileLayer('https://{{s}}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
        maxZoom: 10,
        attribution: '&copy; OpenStreetMap contributors'
      }}).addTo(map);

      pipelines.forEach((pipeline, idx) => {{
        const color = colors[idx % colors.length];
        const latlngs = [
          [pipeline.start_lat, pipeline.start_lon],
          [pipeline.end_lat, pipeline.end_lon]
        ];

        const popup = `
          <strong>${{pipeline.pipeline}}</strong><br>
          Operador: ${{pipeline.operator}}<br>
          Capacidad: ${{pipeline.capacity_bpd.toLocaleString('es-CO')}} bpd<br>
          Tarifa: USD ${{pipeline.tariff_usd_per_bbl.toFixed(2)}} / bbl<br>
          Longitud: ${{pipeline.length_km}} km<br>
          ${{pipeline.notes}}
        `;

        L.polyline(latlngs, {{ color, weight: 4, opacity: 0.85 }})
          .bindPopup(popup)
          .bindTooltip(`${{pipeline.pipeline}} | ${{pipeline.capacity_bpd.toLocaleString('es-CO')}} bpd`)
          .addTo(map);

        latlngs.forEach((coord, pointIdx) => {{
          const label = pointIdx === 0 ? 'Origen' : 'Destino';
          L.circleMarker(coord, {{ radius: 4, color, fillColor: color, fillOpacity: 0.9 }})
            .bindTooltip(`${{pipeline.pipeline}} - ${{label}}`)
            .addTo(map);
        }});
      }});
    </script>
  </body>
</html>"""


def main() -> None:
    pipelines = load_data()
    html = build_html(pipelines)
    OUTPUT_PATH.parent.mkdir(exist_ok=True, parents=True)
    OUTPUT_PATH.write_text(html, encoding="utf-8")
    print(f"Mapa guardado en: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
