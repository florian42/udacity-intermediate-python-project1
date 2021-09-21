import operator

from filters import AttributeFilter
from models import CloseApproach


class VelocityMaxFilter(AttributeFilter):
    def __init__(self, velocity):
        super().__init__(operator.le, velocity)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.velocity
