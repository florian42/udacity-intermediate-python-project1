import operator

from filters import AttributeFilter
from models import CloseApproach


class DistanceMaxFilter(AttributeFilter):
    def __init__(self, distance):
        super().__init__(operator.le, distance)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.distance
