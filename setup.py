from setuptools import setup, find_packages


setup(
    name="prettympl",
    version="0.0.1",
    packages=find_packages(),
    author="Minjoon Hong",
    author_email="mjhong0708@naver.com",
    description="Prettier mpl plot",
    install_requires=["matplotlib>=3.3.1", "cycler", "numpy"]
)