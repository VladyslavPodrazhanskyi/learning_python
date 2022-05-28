import logging

a = 5
b = 0

try:
  c = a / b
except Exception as e:
  # print(e)  # division by zero
  # logging.error("Exception occurred")   # ERROR:root:Exception occurred
  logging.error("Exception occurred", exc_info=True)  # ERROR:root:Exception occurred + whole text of exception
