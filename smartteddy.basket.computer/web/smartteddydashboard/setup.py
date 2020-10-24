import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SmartTeddy",
    version="0.0.1",
    author="Smart Teddy - The Hague University of Applied Sciences",
    author_email="smartteddy41@outlook.com",
    description=" Detecting incidents with seniors on early stage dementia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/smart-teddy-project-hhs/SmartTeddy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
