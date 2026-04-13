from setuptools import setup, find_packages
import os

REPO_AND_PACKAGE_NAME = "omemdb"

with open(os.path.join(REPO_AND_PACKAGE_NAME, "version.py")) as f:
    version = f.read().split("=")[1].strip().strip("'").strip('"')

def read_requirements(path):
    with open(path, "r") as f:
        return [
            line.strip()
            for line in f
            if not line.strip().startswith("#") and line.strip()
        ]

setup(
    name=REPO_AND_PACKAGE_NAME,
    version=version,
    packages=find_packages(exclude="tests"),
    author="Openergy team",
    author_email="contact@openergy.fr",
    long_description=open("README.md").read(),
    install_requires=requirements,
    url=f"https://github.com/openergy/{REPO_AND_PACKAGE_NAME}",
    classifiers=[
        "Programming Language :: Python",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Natural Language :: French",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    package_data={REPO_AND_PACKAGE_NAME: ["*.txt"]},
    include_package_data=True
)
