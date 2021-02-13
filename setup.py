from setuptools import setup, find_packages
from prettympl import __version__


setup(
    name="prettympl",
    version=__version__,
    packages=find_packages(),
    author="Minjoon Hong",
    author_email="mjhong0708@naver.com",
    description="Prettier mpl plot",
    install_requires=["matplotlib>=3.3.1", "cycler", "numpy"]
)