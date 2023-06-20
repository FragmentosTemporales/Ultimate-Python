from pathlib import Path
from time import ctime

archivo = Path("archivos/archivo-prueba.txt")
#archivo.exist()
#archivo.rename()
#archivo.unlink()

print(archivo.stat())
print("acceso", ctime(archivo.stat().st_atime))
print("acceso", ctime(archivo.stat().st_ctime))
print("acceso", ctime(archivo.stat().st_mtime))