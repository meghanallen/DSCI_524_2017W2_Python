from distutils.core import setup

setup(
    name='mfMath',
    version='0.9.9999',
    author='Mat Fournier',
    author_email='mat@matfournier.com',
    packages=['mfMath'],
    scripts=['util.py'],
    url='https://github.ubc.ca/mat4nier/DSCI_524_lab1_python',
    license='LICENSE.txt',
    description='Useful MaTh related stuff from Mat',
    long_description=open('README.txt').read(),
    install_requires=[],
)