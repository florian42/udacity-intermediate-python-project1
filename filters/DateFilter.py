import operator

from filters.AttributeFilter import AttributeFilter
from models import CloseApproach


class DateFilter(AttributeFilter):
    def __init__(self, date):
        super().__init__(operator.eq, date)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.time.date()
