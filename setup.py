from setuptools import setup, find_packages

# Read the requirements from requirements.txt
with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setup(
    name="dsss_homework_2",
    version="0.1",
    packages=find_packages(),
    author="Maedeh Hafezi Moghadas",
    author_email="hafezimaede@yahoo.com",
    description="2nd homework of Data Science Survival skills Lecture",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/maedehafezi/dsss_homework_2",
    install_requires=required_packages,
    python_requires='>=3.6',
)
