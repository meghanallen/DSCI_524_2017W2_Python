from distutils.core import setup

setup(
    name='mfMath',
    version='0.9.9999',
    author='Mat Fournier',
    author_email='mat@matfournier.com',
    packages=['math'],
    scripts=['bin/stowe-towels.py','bin/wash-towels.py'],
    url='http://pypi.python.org/pypi/TowelStuff/',
    license='LICENSE.txt',
    description='Useful MaTh related stuff from Mat',
    long_description=open('README.txt').read(),
    install_requires=[],
)