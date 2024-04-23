"""
Setup of the dukaonesdk module
"""
from setuptools import setup

setup(
    name="dukaonesdk",
    version="1.1.0",
    description="Duka One ventilation SDK entended",
    long_description=(
        "SDK for connection to the Duka One S6W ventilation. "
        "Made for interfacing to home assistant"
    ),
    author="Jens Østergaard Nielsen, Lars Laugesen",
    url="https://github.com/kyllingendk/dukaonesdk-extend",
    packages=["dukaonesdk_extend"],
    license="GPL-3.0",
)
