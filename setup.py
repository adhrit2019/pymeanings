from setuptools import setup

def readme():
    with open('README.md', 'r') as f:
        return f.read()

setup(name='pymeanings',
      version='1.0',
      description='Getting meanings in a GUI dailog box',
      long_description=readme(),
      url='https://github.com/adhrit2019/pymeanings',
      author='Adhrit Pramanik',
      author_email='adhrit2019@gmail.com',
      license='MIT',
      packages=['pymeanings'],
      install_packages=['PyDictionary', 'tkinter', 'subprocess'],
      zip_safe=False,
      entry_points={
                    'console_scripts':['pymeaning=pymeanings.command_line:main']
      })
