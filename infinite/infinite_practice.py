#  In summary, sys.float_info.max represents the largest finite floating-point number
#  that your system can represent,
#  while float('inf') represents positive infinity,
#  which is a value greater than any finite floating-point number.
#  Use them based on your specific needs in your Python code.
import sys


print(float('inf'))         # inf
print(float('inf') > 0)     # inf

print(sys.float_info.max)       # 1.7976931348623157e+308
print(sys.float_info.min)       # 2.2250738585072014e-308
print(sys.float_info.min > 0)   # true

print(-float('inf'))            # -inf
print(-sys.float_info.max)      # -1.7976931348623157e+308
print(-sys.float_info.max)

print(float('inf') > sys.float_info.max)  # true
print(-float('inf') < -sys.float_info.max)  # true
