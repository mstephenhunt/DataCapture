from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

capture.build_stats()

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