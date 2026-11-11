
def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    pendientes = sorted(packages)
    resultado = []

    while pendientes:
        ready = []

        for paquete in pendientes:
            listo = 1
            necesita = packages[paquete]

            for requerimiento in necesita:
                if requerimiento in packages and requerimiento not in resultado:  ##ya que si el requerimiento no esta es ningun paquete se puede instalar
                    listo = 0

            if listo == 1:
                ready.append(paquete)

        if ready == []:
            return []

        resultado += ready

        for paquete in ready:
            pendientes.remove(paquete)

    return resultado
