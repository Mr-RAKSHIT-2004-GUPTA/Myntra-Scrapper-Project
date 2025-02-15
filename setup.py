from setuptools import setup,find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith("-e")]

setup(
    name='scrapper',
    version = '0.0.1',
    author='rakshit',
    author_email='rakshit2004gupta@gmail.com',
    install_requires = requirements,
    packages = find_packages()
    )