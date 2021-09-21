import operator

from filters import AttributeFilter
from models import CloseApproach


class DiameterMinFilter(AttributeFilter):
    def __init__(self, diameter):
        super().__init__(operator.ge, diameter)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.neo.diameter
