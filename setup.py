import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="textpack",
    version="0.0.1",
    author="Luke Whyte",
    author_email="lukeawhyte@gmail.com",
    description="Quickly identify and group similar text strings in a large dataset",
    maintainer="ignacioodisio@gmail.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lukewhyte/textpack",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'scipy',
        'numpy',
        'cython',
        'sparse-dot-topn'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
