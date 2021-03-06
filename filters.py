"""Provide filter_classes for querying close approaches and limit the generated results.

The `create_filters` function produces a collection of objects that is used by
the `query` method to generate a stream of `CloseApproach` objects that match
all of the desired criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.

This function can be thought to return a collection of instances of subclasses
of `AttributeFilter` - a 1-argument callable (on a `CloseApproach`) constructed
from a comparator (from the `operator` module), a reference value, and a class
method `get` that subclasses can override to fetch an attribute of interest from
the supplied `CloseApproach`.

The `limit` function simply limits the maximum number of values produced by an
iterator.

You'll edit this file in Tasks 3a and 3c.
"""
import operator
from abc import ABC

from models import CloseApproach


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter(ABC):
    """A general superclass for filter_classes on comparable attributes.

    An `AttributeFilter` represents the search criteria pattern comparing some
    attribute of a close approach (or its attached NEO) to a reference value. It
    essentially functions as a callable predicate for whether a `CloseApproach`
    object satisfies the encoded criterion.

    It is constructed with a comparator operator and a reference value, and
    calling the filter (with __call__) executes `get(approach) OP value` (in
    infix notation).

    Concrete subclasses can override the `get` classmethod to provide custom
    behavior to fetch a desired attribute from the given `CloseApproach`.
    """

    def __init__(self, op, value):
        """Construct a new `AttributeFilter` from an binary predicate and a reference value.

        The reference value will be supplied as the second (right-hand side)
        argument to the operator function. For example, an `AttributeFilter`
        with `op=operator.le` and `value=10` will, when called on an approach,
        evaluate `some_attribute <= 10`.

        :param op: A 2-argument predicate comparator (such as `operator.le`).
        :param value: The reference value to compare against.
        """
        self.op = op
        self.value = value

    def __call__(self, approach) -> bool:
        """Invoke `self(approach)`."""
        result = self.op(self.get(approach), self.value)
        return result

    @classmethod
    def get(cls, approach):
        """Get an attribute of interest from a close approach.

        Concrete subclasses must override this method to get an attribute of
        interest from the supplied `CloseApproach`.

        :param approach: A `CloseApproach` on which to evaluate this filter.
        :return: The value of an attribute of interest, comparable to `self.value` via `self.op`.
        """
        raise UnsupportedCriterionError

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})"


class DateFilter(AttributeFilter):
    """Determines if a `CloseApproach` occurs on given `date`."""

    def __init__(self, date):
        """Create a new `DateFilter`."""
        super().__init__(operator.eq, date)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the date from a `CloseApproach`."""
        return approach.time.date()


class DiameterMaxFilter(AttributeFilter):
    """Determines if the diameter of a `CloseApproach` is less then or equal to `diameter`."""

    def __init__(self, diameter):
        """Create a new `DiameterMaxFilter`."""
        super().__init__(operator.le, diameter)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the diameter from a `CloseApproach`."""
        return approach.neo.diameter


class DiameterMinFilter(AttributeFilter):
    """Determines if the diameter of a `CloseApproach` is greater then or equal to `diameter`."""

    def __init__(self, diameter):
        """Create a new `DiameterMinFilter`."""
        super().__init__(operator.ge, diameter)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the diameter from a `CloseApproach`."""
        return approach.neo.diameter


class DistanceMaxFilter(AttributeFilter):
    """Determines if the distance of a `CloseApproach` is less then or equal to `distance`."""

    def __init__(self, distance):
        """Create a new `DistanceMaxFilter`."""
        super().__init__(operator.le, distance)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the distance from a `CloseApproach`."""
        return approach.distance


class DistanceMinFilter(AttributeFilter):
    """Determines if the distance of a `CloseApproach` is greater then or equal to `distance`."""

    def __init__(self, distance):
        """Create a new `DistanceMinFilter`."""
        super().__init__(operator.ge, distance)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the distance from a `CloseApproach`."""
        return approach.distance


class EndDateFilter(AttributeFilter):
    """Determines if a `CloseApproach` occurs before a given `date`."""

    def __init__(self, date):
        """Create a new `EndDateFilter`."""
        super().__init__(operator.le, date)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the date from a `CloseApproach`."""
        return approach.time.date()


class HazardousFilter(AttributeFilter):
    """Determines if a `CloseApproach` is potentially hazardous or not."""

    def __init__(self, hazardous):
        """Create a new `HazardousFilter`."""
        super().__init__(operator.eq, hazardous)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get if a `CloseApproach` is potentially hazardous."""
        return approach.neo.hazardous


class StartDateFilter(AttributeFilter):
    """Determines if a `CloseApproach` occurs after a given `date`."""

    def __init__(self, date):
        """Create a new `StartDateFilter`."""
        super().__init__(operator.ge, date)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the date from a `CloseApproach`."""
        return approach.time.date()


class VelocityMaxFilter(AttributeFilter):
    """Determines if the velocity of a `CloseApproach` is less then or equal to `velocity`."""

    def __init__(self, velocity):
        """Create a new `VelocityMaxFilter`."""
        super().__init__(operator.le, velocity)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the velocity from a `CloseApproach`."""
        return approach.velocity


class VelocityMinFilter(AttributeFilter):
    """Determines if the velocity of a `CloseApproach` is greater then or equal to `velocity`."""

    def __init__(self, velocity):
        """Create a new `VelocityMinFilter`."""
        super().__init__(operator.ge, velocity)

    @classmethod
    def get(cls, approach: CloseApproach):
        """Get the velocity from a `CloseApproach`."""
        return approach.velocity


def create_filters(
    date=None,
    start_date=None,
    end_date=None,
    distance_min=None,
    distance_max=None,
    velocity_min=None,
    velocity_max=None,
    diameter_min=None,
    diameter_max=None,
    hazardous=None,
):
    """Create a collection of filter_classes from user-specified criteria.

    Each of these arguments is provided by the main module with a value from the
    user's options at the command line. Each one corresponds to a different type
    of filter. For example, the `--date` option corresponds to the `date`
    argument, and represents a filter that selects close approaches that occurred
    on exactly that given date. Similarly, the `--min-distance` option
    corresponds to the `distance_min` argument, and represents a filter that
    selects close approaches whose nominal approach distance is at least that
    far away from Earth. Each option is `None` if not specified at the command
    line (in particular, this means that the `--not-hazardous` flag results in
    `hazardous=False`, not to be confused with `hazardous=None`).

    The return value must be compatible with the `query` method of `NEODatabase`
    because the main module directly passes this result to that method. For now,
    this can be thought of as a collection of `AttributeFilter`s.

    :param date: A `date` on which a matching `CloseApproach` occurs.
    :param start_date: A `date` on or after which a matching `CloseApproach` occurs.
    :param end_date: A `date` on or before which a matching `CloseApproach` occurs.
    :param distance_min: A minimum nominal approach distance for a matching `CloseApproach`.
    :param distance_max: A maximum nominal approach distance for a matching `CloseApproach`.
    :param velocity_min: A minimum relative approach velocity for a matching `CloseApproach`.
    :param velocity_max: A maximum relative approach velocity for a matching `CloseApproach`.
    :param diameter_min: A minimum diameter of the NEO of a matching `CloseApproach`.
    :param diameter_max: A maximum diameter of the NEO of a matching `CloseApproach`.
    :param hazardous: Whether the NEO of a matching `CloseApproach` is potentially hazardous.
    :return: A collection of filter_classes for use with `query`.
    """
    filters = []
    if date:
        filters.append(DateFilter(date))
    if start_date:
        filters.append(StartDateFilter(start_date))
    if end_date:
        filters.append(EndDateFilter(end_date))
    if distance_min:
        filters.append(DistanceMinFilter(distance_min))
    if distance_max:
        filters.append(DistanceMaxFilter(distance_max))
    if velocity_min:
        filters.append(VelocityMinFilter(velocity_min))
    if velocity_max:
        filters.append(VelocityMaxFilter(velocity_max))
    if diameter_min:
        filters.append(DiameterMinFilter(diameter_min))
    if diameter_max:
        filters.append(DiameterMaxFilter(diameter_max))
    if hazardous is not None:
        filters.append(HazardousFilter(hazardous))

    return tuple(filters)


def limit(iterator, n=None):
    """Produce a limited stream of values from an iterator.

    If `n` is 0 or None, don't limit the iterator at all.

    :param iterator: An iterator of values.
    :param n: The maximum number of values to produce.
    :yield: The first (at most) `n` values from the iterator.
    """
    for index, value in enumerate(iterator):
        if n == 0 or n is None:
            yield value
        elif index < n and n > 0:
            yield value
