import setuptools

with open('Readme.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='fastapi-buynotes',
    version='0.0.1',
    author='imchrisorz',
    author_email='imchrisorz@gmail.com',
    description='记账App服务端',
    include_package_data=True,
    packages=setuptools.find_packages(),
    python_requires='>=3.6'
)
