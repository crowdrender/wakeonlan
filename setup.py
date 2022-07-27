############################  LICENSE  #########################

# Copyright (C) <2013-2021> Crowd Render Pty Limited, Sydney Australia


# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# You can contact the author at info at
# crowdrender dot com dot au

################################################################

from setuptools import setup


setup(
    name="wakeonlan",
    version="0.0.1",
    description="Super simple command line utility for waking hosts over a local network.",
    url="https://github.com/crowdrender/wakonlan",
    author="Crowdrender",
    author_email="info@crowdrender.com.au",
    license="MIT",
    install_requires=[
        "netifaces",
    ],
    zip_safe=False,
    entry_points={"console_scripts": ["wol=wol:main"]},
)
