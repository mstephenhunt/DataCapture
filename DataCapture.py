class DataCapture:
    """
    I'm running under the assumption here that when you do any search
    on the list of values that you're only able to search on values
    that you've previously provided via add()
    """
    _total_values = 0
    _value_counts = [0] * 999 # initialize all counts to 0
    _stat_values = [{}] * 999

    def _value_type_check(self, value_to_check):
        """
        Re-useable error checking for values passed into functions
        """
        if type(value_to_check) is not int:
            raise TypeError("Values passed must be integers")
        if value_to_check < 0 or value_to_check > 999:
            raise ValueError("Values passed must be >0 and <1000")

    def _value_in_list_check(self, value_to_check):
        """
        Re-useable error checking to ensure passed value is in list
        """
        if self._stat_values[value_to_check] == {}:
            raise LookupError("Value provided not added to list")

    def add(self, value_to_add):
        """
        Here we increase the count of values, where the
        value indicates the index to increase.
        """
        self._value_type_check(value_to_add)

        self._value_counts[value_to_add] += 1
        self._total_values += 1

    def build_stats(self):
        """
        In this method we iterate through the list of value
        counts to build our ordered list
        """
        less_than_count = 0
        for value, count in enumerate(self._value_counts):
            if count > 0:
                self._stat_values[value] = {
                    "less_than": less_than_count,
                    "greater_than": self._total_values - less_than_count - count,
                    "count": count
                }

                less_than_count += count

    def less(self, search_value):
        """
        Get the count of values less than the provided
        """
        self._value_type_check(search_value)
        self._value_in_list_check(search_value)

        return self._stat_values[search_value]["less_than"]

    def greater(self, search_value):
        """
        Get the count of values greater than the provided
        """
        self._value_type_check(search_value)
        self._value_in_list_check(search_value)

        return self._stat_values[search_value]["greater_than"]

    def between(self, lower_value, upper_value):
        """
        Get the count of values between these two provided, 
        inclusive
        """
        self._value_type_check(lower_value)
        self._value_in_list_check(lower_value)
        self._value_type_check(upper_value)
        self._value_in_list_check(upper_value)

        num_of_between_values = (
            self.greater(lower_value) - 
            self.greater(upper_value) +
            self._stat_values[lower_value]["count"])

        return num_of_between_values
