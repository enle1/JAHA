from setuptools import setup, find_packages

setup(
    name='calculator',
    version='0.1',
    packages=find_packages(),
    description='A simple calculator package with basic and engineering functionalities',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/calculator',  # GitHub 링크
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)