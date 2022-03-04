import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Graphics_Algos",
    version="1.0.0",
    author="V.EswarChand",
    author_email="chandu71202@gmail.com",
    description="A simple package which gives returns the values of the Computer Graphics Algorithms. Such as Bresenhen Line Drawing Algorithm etc",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Chandu71202/Graphics_algos",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keywords='BRESENHEN',
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
)
