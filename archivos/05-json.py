import json
from pathlib import Path

# escribir JSON
productos = [
    {"id": 1, "name": "Ropa"},
    {"id": 2, "name": "Saco"},
    {"id": 3, "name": "Linterna"}
]
data = json.dumps(productos)
Path("archivos/productos.json").write_text(data)

# leer JSON
data = Path("archivos/productos.json").read_text(encoding="utf-8")
productos = json.loads(data)

# modificar JSON

productos[0] ["name"] = "Cristian"
Path("archivos/productos.json").write_text(json.dumps(productos))

