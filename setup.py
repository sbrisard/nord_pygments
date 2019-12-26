from setuptools import setup

setup(name='nord_pygments',
      version=0.0,
      py_modules=['nord_pygments'],
      license='BSD-3',
      entry_points={'pygments.styles': 'nord = nord_pygments:NordStyle'}
)
