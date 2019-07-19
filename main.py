# capture = DataCapture()
# capture.add(3)
# capture.add(9)
# capture.add(3)
# capture.add(4)
# capture.add(6)
# stats = capture.build_stats()
# stats.less(4) # should return 2 (only two values 3,3 are less than 4)
# stats.between(3, 6) # should return 4 (3,3,4 and 6 are between 3 and 6)
# stats.greater(4) # should return 2 (6 and 9 are the only two values greater than 4)

from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

# print(capture._value_counts)
capture.build_stats()
# print(capture._sorted_values)

print("Less than 4: " + str(capture.less(4)))
print("Greater than 4: " + str(capture.greater(4)))
print("Between 3 and 6: " + str(capture.between(3, 6)))

try:
    capture.add('a')
except TypeError as error:
    print(error)

try:
    capture.add(-1)
except ValueError as error:
    print(error)

try:
    capture.less(100)
except LookupError as error:
    print(error)