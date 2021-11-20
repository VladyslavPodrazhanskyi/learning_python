import os

print(os.environ)


rds_host = os.environ.get('rds_host')
rds_user = os.environ.get('rds_user')
# rds_name = os.environ.get('rds_name')

print("db_host:")
print(rds_host)
print("rds_user = " + rds_user)
# print("\n rds_name = " + rds_name)
