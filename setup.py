from setuptools import setup
import os
from glob import glob

package_name = 'turtlesim_test'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ginga',
    maintainer_email='gingakennis123@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "publisher = turtlesim_test.publisher:main",
            "subscriber = turtlesim_test.subscriber:main",
            "sub_pub = turtlesim_test.sub_pub:main",
            "teleop_keyboard = turtlesim_test.teleop_keyboard:main",
        ],
    },
)
