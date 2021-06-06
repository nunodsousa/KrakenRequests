from setuptools import setup

setup(name='KrakenRequests',
      version='0.1',
      description='Static Kraken Requests',
      url='https://github.com/nunodsousa/KrakenRequests',
      author='Nuno de Sousa',
      author_email='nunodsousa@simia-tech.com',
      license='MIT',
      packages=['KrakenRequests'],
      install_requires=['requests', 'pandas'],
      zip_safe=False)
