from setuptools import setup, find_packages

setup(
    name = "floretta",
    version='0.0.1dev',
    description='a python package',
    auther='GorZ3rk',
    author_email='melodymaa28@hotmail.com',
    packages=find_packages(include=['floretta', 'floretta.*']),
    install_requires=[
        'PyYAML',
        'pandas',
        'numpy>=1.14.5'
    ],
    extras_require={'plotting': ['matplotlib>=2.2.0', 'jupyter']},
    setup_requires=['pytest-runner', 'flake8'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['my-command=floretta.floretta:main']
    },
    package_data={'floretta': ['data/schema.json']}
)