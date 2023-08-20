import setuptools

setuptools.setup(
    include_package_data=True,
    name='basic',
    version='0.0.1',
    description='Basic Project',
    url='https://gitlab.com/User_Group_ID_100/python_projects/-/tree/main/src/CLI?ref_type=heads',
    author='Abhisar',
    author_email='abhisarvaish.ec1003@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['yaspin'],
    scripts=['basic/main.py'],
    entry_points={
      'console_scripts': [
         'basic=basic.main:main',
      ],
    }
)
