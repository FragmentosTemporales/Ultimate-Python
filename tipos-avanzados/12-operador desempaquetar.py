punto1 = {"x": 19}
punto2 = {"y": 15}

nuevoPunto = {**punto1, "lala": "hola", **punto2, "z": "mundo"}
print(nuevoPunto)