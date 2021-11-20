docker build -t import_test .

cat <<EOF > env.list
rds_host=sfjhsfhost
rds_user=sfkjuser
EOF

docker run --env-file ./env.list --rm -v $(pwd)/app/:/app import_test python /app/environ_check.py

docker rmi import_test