from setuptools import setup

setup(
    # Basic info
    name='alert_generator',
    author='Scality',
    author_email='eng-all@scality.com',
    description='.',
    install_requires=[
        'ruamel.yaml'
    ],
    packages=['alert_generator'],
    # Packages and depencies
    # Scripts
    entry_points={
        'console_scripts': [
            'gen-alert = alert_generator.alert_generator:main'],
    },

)
