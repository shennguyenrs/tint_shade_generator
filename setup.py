"""
Setup for Tint and Shade Generator
"""

from setuptools import setup, find_packages

setup(
    name="Tint and Shade Generator",
    version="0.1.0",
    description="A simple script to generate tint and shade from HEX code color",
    url="https://github.com/shennguyenrs/tint_shade_generator",
    author="An Nguyen",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3 and above",
    ],
    keywords="tint color, shade color, rgb color, hex color, script",
    packages=find_packages(include=["tint_shade_generator", "tint_shade_generator.*"]),
    install_requires=[
        "argparse"
    ]
)
