from setuptools import setup, find_packages


setup(
    name='fsa-svc',
    author='Natalia Maximo',
    author_email='iam@natalia.dev',
    version='0.1',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=[
        'pyfsa',
        'flask',
        'gunicorn',
        'flask-json-schema',
        'python-dotenv',
    ],
    tests_require=['pytest-cov', 'pytest', 'flake8', 'mypy'],
    extras_require={
        'tests': ['pytest-cov', 'pytest', 'flake8', 'mypy'],
    },
)
