from setuptools import setup, find_packages

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path):
    with open(file_path) as f:
        requirements = f.readlines()
        requirements_without_n = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements_without_n:
            requirements_without_n.remove(HYPHEN_E_DOT)
        return requirements_without_n

setup(
    name="CustomerChurn",
    author="Taha Tariq",
    author_email="tahatariqf@gmail.com",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)