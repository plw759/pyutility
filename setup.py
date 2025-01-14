'''
Description:
Author: Jiaqi Gu (jqgu@utexas.edu)
Date: 2021-11-29 04:15:29
LastEditors: Jiaqi Gu (jqgu@utexas.edu)
LastEditTime: 2023-04-03 20:08:33
'''

from setuptools import setup, find_packages

setup(
    name="pyutils",
    version="0.0.2",
    description="Python/Pytorch Utility",
    url="https://github.com/JeremieMelo/pyutility",
    author="Jiaqi Gu",
    author_email="jqgu@utexas.edu",
    license="MIT",
    install_requires=[
        "numpy>=1.19.2",
        "torchvision>=0.9.0.dev20210130",
        "tqdm>=4.56.0",
        "setuptools>=52.0.0",
        "torch>=1.8.0",
        "matplotlib>=3.3.4",
        "svglib>=1.1.0",
        "scipy>=1.5.4",
        "scikit-learn>=0.24.1",
        "torchsummary>=1.5.1",
        "pyyaml>=5.1.1",
        "tensorflow>=2.5.0",
    ],
    python_requires=">=3",
    include_package_data=True,
    packages=find_packages(),
)
