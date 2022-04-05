from setuptools import setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.md").read_text(encoding="utf-8")
version = "0.1.0"


setup(
    name="mycat",
    version=version,
    description="Fast and elegant DataFrame library in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tushushu/mycat",
    author="Tushushu",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="dataframe, machine learning, data analysis",
    packages=["mycat"],
    python_requires=">=3.7, <4",
    install_requires=["ulist==0.9.0"],
    extras_require={
        "publish": ["twine==4.0.0"],
        "CI": [
            "pytest==6.2.5",
            "mypy==0.930",
            "flake8==4.0.1",
        ],
    },
    package_data={"mycat": ["py.typed"]},
    project_urls={
        "Source": "https://github.com/tushushu/mycat",
    },
)
