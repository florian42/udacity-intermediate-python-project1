import operator

from filters import AttributeFilter
from models import CloseApproach


class EndDateFilter(AttributeFilter):
    def __init__(self, date):
        super().__init__(operator.le, date)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.time.date()
