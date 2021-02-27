from setuptools import setup, find_packages


setup(
    name="prettympl",
    version="0.0.2",
    packages=find_packages(),
    package_data={
        "prettympl": ["fonts/*/*"],
    },
    include_package_data=True,
    author="Minjoon Hong",
    author_email="mjhong0708@naver.com",
    description="Prettier mpl plot",
    install_requires=["matplotlib>=3.3.1", "cycler", "numpy"]
)