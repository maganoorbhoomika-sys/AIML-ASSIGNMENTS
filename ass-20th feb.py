##Assignment Name : NumPy Speed Test

##Compare Python lists vs NumPy arrays with 1M numbers, measure execution time, write 3 observations.

import time
import numpy as np

# Create 1 million numbers
size = 1_000_000

# -------- Python List --------
start = time.time()

py_list = list(range(size))
py_result = [x * 2 for x in py_list]

end = time.time()
list_time = end - start

print("Python List Time:", list_time)

# -------- NumPy Array --------
start = time.time()

np_array = np.arange(size)
np_result = np_array * 2

end = time.time()
numpy_time = end - start

print("NumPy Array Time:", numpy_time)

''''NumPy arrays execute operations faster than Python lists because they are implemented in optimized C code.

NumPy performs vectorized operations, meaning it processes the entire array at once instead of looping through each element like Python lists.

Memory usage is more efficient in NumPy, since arrays store elements of the same data type, while Python lists store objects with extra overhead.''''''