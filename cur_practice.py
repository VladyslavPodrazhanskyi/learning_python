import os

# file_key = (
#     'ANOTHER_OBJECT_NAME_data'
#     '/ingestion_timestamp=2010-10-10T10-10-10'
#     '/BATCH_ID=20201010_101010'
#     '/object_name2_data_20201010_101010.dat'
# )

file_key = "skfjkf"

_, dot_extension = os.path.splitext(file_key)
extension = ' '.strip('.')

print(extension)