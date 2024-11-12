#!/usr/bin/env python

from distutils.core import setup
  
package_name = 'behavior_selector2'  
setup(
    name=package_name,
    version='0.0.0',
    packages=['rqt_pkg'],
    package_dir={'': 'src'},
    install_requires=['setuptools'],
    tests_require=['pytest'],
    zip_safe=True.
    maintainer='Brett',
    maintainer_email='brett@todo.todo',
    description='GUI for selecting global flight mode',
    license='MIT',
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name), glob('resource/*')),
        (os.path.join('share', package_name), ['plugin.xml']),
        (os.path.join('lib', package_name), glob('behavior_selector2/*.py')),
    ],
    entry_points={
        'console_scripts': [
            'button_module = behavior_selector2.button_module',
            'behavior_selector = behavior_selector2.behavior_selector.main',
        ],
    },
)

