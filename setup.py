from setuptools import setup

setup(
    install_requires=[
        'Cython==0.25.1; python_version<="3.6"',  # This version doesn't work on 3.7+
        'Cython==0.29.19; python_version>="3.7"',
        "cysignals==1.6.5",
        "configparser==3.5.0",
        "kafka==1.3.5",
        "confluent-kafka[avro]==1.3.0",
        "fastavro",  # Whatever's needed by confluent-kafka[avro]
        'avro-python3==1.9.2.1',  # confluent-kafka[avro] defines a dependency on 1.9.2, but only 1.9.2.1 works
        "isort==4.3.21",

        "scipy>=1.2.1, <=1.4.1; python_full_version>='3.6'",
        "numpy==1.17.1",
        "teamcity-messages==1.17",
        "vertica_python>=0.9.1,<=0.10.2",
        "mido >=1.2.8,<=1.2.9",
        "requests==2.22.0, <=2.23.0",
        "python-Levenshtein==0.12.0",
        "enum34>=1.1.6,<=1.1.10; python_version<'3.4'",
        "aubio==0.4.9",
        "future>=0.17.1, <=0.18.2",
        "six>=1.11.0,<=1.14.0",
        "datasketch==1.5.1",
        "jams==0.3.4",
        "python-slugify==3.0.2",
    ],
)
