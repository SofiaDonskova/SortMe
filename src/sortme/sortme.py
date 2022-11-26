from abc import ABC, abstractmethod


class BaseSort(ABC):
    @abstractmethod
    def sort(self, o):
        pass


class BubbleSort(BaseSort):
    def sort(self, o):
        # TODO реализовать метод сортировки пузырьком
        raise NotImplementedError('implemented is required')


class GravitySort(BaseSort):
    def sort(self, o):
        # TODO реализовать метод сортировки гравитацией
        raise NotImplementedError('implemented is required')
