from setuptools import setup, find_packages

VERSION = '0.0.6'
DESCRIPTION = 'Aerodynamic Calculation Tools'
LONG_DESCRIPTION = 'A handy tool for Aerodynamics Engineers of multiple functionalities'

# Setting up
setup(
    name="parsektools",
    version=VERSION,
    author="Sadi Cesur",
    author_email="<cesursadi@gmail.com>",
    description=DESCRIPTION,
    # long_description_content_type="text/markdown",
    # long_description=long_description_content_type,
    packages=find_packages(),
    install_requires=['numpy'],
    keywords=['python', 
              'athmosphere', 
              'air',
              'properties',
              'height',
              'speed of sound',
              'gravity',
              'pressure',
              'temperature',
              'density',
              "sutherland",
              "viscosity"],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
