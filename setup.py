from setuptools import setup, find_packages

setup(
    name='tsol',
    version='0.1',
    py_modules=['tsol'],
    include_package_data=True,
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