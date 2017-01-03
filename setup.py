from setuptools import setup, find_packages
setup(
    name="diskutil_parser",
    version="1.0.1",
    packages=find_packages(),

    # metadata for upload to PyPI
    author="Kenzie Togami",
    author_email="ket1999@gmail.com",
    description="Parses diskutil output on macOS",
    license="MIT",
    keywords="diskutil",
    url="https://github.com/kenzierocks/diskutil_parser",
)
