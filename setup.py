## ! DO NOT MANUALLY INVOKE THIS setup.py, USE CATKIN INSTEAD

from distutils.core import setup
from catkin_pkg.python_setup import generate_distutils_setup

# fetch values from package.xml
setup_args = generate_distutils_setup(
    packages=[
            'airsim_resources',
            'open3d_resources',
            'gym_airsim'
            ],
    package_dir={"": "src/modules"})


setup(**setup_args)