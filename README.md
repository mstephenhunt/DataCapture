# DataCapture

The `main.py` program provides an example. To run:
```
$ python main.py
```

## Sample Usage:
```python
from DataCapture import DataCapture

capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

capture.build_stats()

capture.less(4) # => 2
capture.greater(4) # => 2
capture.between(3, 6) # => 4
```