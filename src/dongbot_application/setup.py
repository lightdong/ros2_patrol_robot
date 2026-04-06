from setuptools import find_packages, setup

package_name = 'dongbot_application'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='vim3',
    maintainer_email='959698824@qq.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            "init_robot_pose = dongbot_application.init_robot_pose:main",
            "get_robot_pose = dongbot_application.get_robot_pose:main",
            "nav_to_pose = dongbot_application.nav_to_pose:main",
            "waypoint_flollower = dongbot_application.waypoint_flollower:main",
        ],
    },
)
