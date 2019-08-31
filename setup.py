import setuptools
import toml


def get_install_requirements():
    try:
        with open ('Pipfile', 'r') as fh:
            pipfile = fh.read()
        pipfile_toml = toml.loads(pipfile)
    except FileNotFoundError:
        return []
    try:
        required_packages = pipfile_toml['packages'].items()
    except KeyError:
        return []
    return ["{0}{1}".format(pkg,ver) if ver != "*" else pkg for pkg,ver in required_packages]


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="legistar",
    version="1.0.0",
    author="Russ Biggs",
    author_email="russbiggs@gmail.com",
    description="Legistar HTTP API wrapper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/russbiggs/legistar",
    packages=setuptools.find_packages(exclude=["tests"]),
    install_requires=get_install_requirements(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable"
    ],
)