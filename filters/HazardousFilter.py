from filters import AttributeFilter
import operator

from models import CloseApproach


class HazardousFilter(AttributeFilter):
    def __init__(self, hazardous):
        super().__init__(operator.eq, hazardous)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.neo.hazardous
