import setuptools

setuptools.setup(
    include_package_data=True,
    name='zyco',
    version='0.0.1',
    description='Zyco Games Project',
    url='https://gitlab.com/User_Group_ID_100/python_projects/-/tree/main/src/CLI?ref_type=heads',
    author='Abhisar',
    author_email='abhisarvaish.ec1003@gmail.com',
    packages=setuptools.find_packages(),
    install_requires=['inquirer', 'yaspin', 'pyfiglet', 'pyttsx3'],
    scripts=['zyco/main.py'],
    entry_points={
      'console_scripts': [
         'zyco=zyco.main:main',
      ],
    }
)
