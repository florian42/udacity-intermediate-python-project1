import operator

from filters import AttributeFilter
from models import CloseApproach


class DistanceMinFilter(AttributeFilter):
    def __init__(self, distance):
        super().__init__(operator.ge, distance)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.distance
