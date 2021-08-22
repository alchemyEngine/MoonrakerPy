import setuptools

with open('README.md', 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="MoonrakerPy",
    version="0.0.1",
    author="Robert Pazdzior",
    author_email="robertp@norbital.com",
    description="A Python package for interface with the Moonraker API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alchemyEngine/MoonrakerPy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],
    python_requires='>=3.8',
    install_requires=['requests >= 2.26.0']
)