class StringCompare:
    result = None

    def __init__(self, string_1: str, string_2: str):
        self.result = self.run(string_1, string_2)

    def compare(self, string_1: str, string_2: str) -> int:
        """Compare 2 version strings
        :param string_1: Version string; dot separated numbers;
        :param string_2: Version string; dot separated numbers;
        :return:
        positive number: If the first version is greater than the second
        negative number: If the first version is smaller than the second
        zero: If the versions are equals
        """
        string_1, string_2 = (map(int, v.split('.'))
                              for v in [string_1, string_2])
        string_1, string_2 = zip(
            *map(lambda grp1, grp2: (grp1 or 0, grp2 or 0), string_1, string_2))

        for i in range(len(string_1)):
            if string_1[i] != string_2[i]:
                return string_1[i] - string_2[i]
        return 0

    def run(self, string_1: str, string_2: str) -> str:
        """Compare 2 version strings and Returns the result in either of three selected pre-formated strings
        :param string_1: Version string; dot separated numbers;
        :param string_2: Version string; dot separated numbers;
        :return:
        '{string_1}' is equal to '{string_2}': If the comparison returns 0
        '{string_1}' is smaller than '{string_2}': If the comparison returns -1
        '{string_1}' is greater than '{string_2}': If the comparison returns 1
        """
        answer = self.compare(string_1, string_2)

        result = f"'{string_1}' is equal to '{string_2}'"
        if answer < 0:
            result = f"'{string_1}' is less than '{string_2}'"
        elif answer > 0:
            result = f"'{string_1}' is greater than '{string_2}'"

        return result

    def __str__(self):
        """Return the string representation for the Class
        """
        return self.result
