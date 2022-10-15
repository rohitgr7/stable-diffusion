from pkg_resources import parse_requirements
from setuptools import setup, find_packages


def _load_requirements(file_path: str = "requirements.txt") -> list:
    with open(file_path) as fp:
        requires = parse_requirements(fp.readlines())
    return [str(r) for r in requires]

setup(
    name='latent-diffusion',
    version='0.0.1',
    author='CompVis',
    author_email='assist.mvl@lrz.uni-muenchen.de',
    url='https://github.com/CompVis/stable-diffusion',
    description='Stable Diffusion',
    long_description='Stable Diffusion is a latent diffusion model conditioned on the (non-pooled) text embeddings',
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    install_requires=_load_requirements(),
)
