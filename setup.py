import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="File-Syncer",
    version="1.0.0",
    author="ZlissX,Oblicx",
    author_email="ZlissX14OblicX@gmail.com",
    description="A robust File-Syncer which will keep File/Folders synchronized between two Directories.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Z14O/File-Syncer",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)