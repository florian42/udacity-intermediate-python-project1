import operator

from filters import AttributeFilter
from models import CloseApproach


class VelocityMinFilter(AttributeFilter):
    def __init__(self, velocity):
        super().__init__(operator.ge, velocity)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.velocity
