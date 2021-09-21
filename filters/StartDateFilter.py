import operator

from filters import AttributeFilter
from models import CloseApproach


class StartDateFilter(AttributeFilter):
    def __init__(self, date):
        super().__init__(operator.ge, date)

    @classmethod
    def get(cls, approach: CloseApproach):
        return approach.time.date()
