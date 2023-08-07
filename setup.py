from setuptools import setup

setup(
    name='ffconverter',
    version='0.1',
    description='File Format Converter',
    url='https://github.com/avijayal/file-format-converter',
    author='avijayal',
    author_email='3002.vijayalakshmi@gmail.com',
    license='MIT',
    packages=['ffconverter'],
    install_requires=['pandas<=2.0.3'],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['ffc=ffconverter:main'],
    }
)
