import os
from glob import glob
from setuptools import setup

package_name = 'hiwonder_acker_driver'

setup(
    name=package_name,
    version='1.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='hiwonder',
    maintainer_email='',
    description='hiwonder acker driver',
    license='unlicense',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'acker_controller = hiwonder_acker_driver.acker_controller_node:main'
        ],
    },
)
