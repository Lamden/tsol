from setuptools import setup, find_packages

setup(
    name='tsol',
    version='0.1.2',
    py_modules=['tsol'],
    include_package_data=True,
    description = 'Templated Solidity for smart contracts.',
    author = 'Lamden GmbH',
    author_email = 'team@lamden.io',
    url = 'https://github.com/lamden/tsol',
    download_url = 'https://github.com/lamden/tsol/archive/0.1.tar.gz',
    keywords = ['ethereum', 'solidity', 'cryptocurrency'],
    packages=find_packages(),
    install_requires=[
         'click',
         'requests',
         'Jinja2',
         'py-solc'
    ],
    entry_points='''
        [console_scripts]
        tsol=tsol:cli
    ''',
)
  