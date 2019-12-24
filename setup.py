from setuptools import setup

setup(name='pygnord',
      version=0.0,
      py_modules=['pygnord'],
      license='BSD-3',
      entry_points={'pygments.styles': 'nord = pygnord:NordStyle'}
)
