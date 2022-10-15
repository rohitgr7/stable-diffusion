from pkg_resources import parse_requirements
from setuptools import setup, find_packages


def _load_requirements(file_path: str = "requirements.txt") -> list:
    with open(file_path) as fp:
        requires = parse_requirements(fp.readlines())
    return list(requires)

setup(
    name='latent-diffusion',
    version='0.0.1',
    description='',
    packages=find_packages(),
    install_requires=_load_requirements(),
)