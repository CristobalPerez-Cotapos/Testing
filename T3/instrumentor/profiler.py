import threading

# Clase que representa la estructura de un profiler
class Profiler:
    __singleton_lock = threading.Lock()
    __singleton_instance = None

    # Usamos un singleton para no crear instancias a cada rato
    @classmethod
    def getInstance(cls):
        with cls.__singleton_lock:
            if not cls.__singleton_instance:
                cls.__singleton_instance = cls()
        return cls.__singleton_instance

    # Al resetear actualizamos la instancia de singleton a None
    @classmethod
    def reset(cls):
        cls.__singleton_instance = None

    @classmethod
    def record(cls, *other):
        pass