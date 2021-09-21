import operator

from filters import AttributeFilter
from models import CloseApproach


class DiameterMaxFilter(AttributeFilter):
    def __init__(self, diameter):
        super().__init__(operator.le, diameter)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.neo.diameter
