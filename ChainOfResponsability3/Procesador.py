"""
Avoid coupling the sender of a request to its receiver by giving
more than one object a chance to handle the request. Chain the receiving
objects and pass the request along the chain until an object handles it.
"""

import abc

class Procesador():

    """
    Define an interface for handling requests.
    Implement the successor link.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self, siguiente = None):
        self._siguiente = siguiente

    @abc.abstractmethod
    def manejaProcesos(self, nombrePeticion):
        pass
