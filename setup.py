from setuptools import setup, find_packages

setup(
    name='zplot-tools',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'matplotlib',
        'numpy',
        'pandas',
    ],
    package_data={
        'styles': ['mpl_styles/*.mplstyle']
    },
    author='Zaitam',
    description='A collection of matplotlib styles and useful utilities',
    url='https://github.com/zaitam/zplot-tools',
)
