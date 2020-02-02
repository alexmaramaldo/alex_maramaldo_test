from typing import Tuple

Line = Tuple[int, int]


class Overlap:
    result = None

    def __init__(self, line1: Line, line2: Line):
        super().__init__()
        self.result = self.run(line1, line2)

    def is_number_inside_boundaries(self, number: int, boundaries: Line) -> bool:
        """Check if a number is contained into the specified boundaries

        :param number: The number to check into the boundaries
        :param boundaries: Two numbers tuple whit first element < second element
        :return: True if the number is inside the boundaries, if not, False
        """

        return min(boundaries) <= number <= max(boundaries)

    def overlap_ordered(self, line1: Line, line2: Line) -> bool:
        """Check if two lines in the X axis overlap; the first one must be before or inside the second

        :param line1: Two numbers tuple whit first element < second element
        :param line2: Two numbers tuple whit first element < second element
        :return: True if the lines overlap, if not, False
        """

        return self.is_number_inside_boundaries(line1[0], line2) or self.is_number_inside_boundaries(line1[1], line2)

    def run(self, line1: Line, line2: Line) -> bool:
        """Check if two lines in the X axis overlap

        :param line1: Two numbers tuple whit first element < second element
        :param line2: Two numbers tuple whit first element < second element
        :return: True if the lines overlap, if not, False
        """

        return self.overlap_ordered(line1, line2) or self.overlap_ordered(line2, line1)

    def __str__(self):
        """Return the string representation for the Class
        """
        return str(self.result)
