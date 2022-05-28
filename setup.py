from setuptools import setup, find_packages

setup(
    name="adl-sap-grc-etl",
    version='1.0.0',
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(exclude=("src.test",)),
    scripts=[],
    classifiers=["Programming Language :: Python :: 3"],
    install_requires=[
        'boto3==1.16.38',
        'fake-awsglue',
        'pyspark~=2.4.3',
        'joblib==0.17.0',
        'pytest==6.2.5',
        'pyspark-test'
    ],
    python_requires='==3.7.*',
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
