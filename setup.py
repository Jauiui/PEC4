from setuptools import setup, find_packages

setup(
    name="firearm_analysis",
    version="0.1",
    description=open("README.md").read(),
    author="Javier Martínez Rodríguez",
    url="https://github.com/tuusuario/nombre-del-repositorio"
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "folium",
        "selenium",
        "requests",
        "unittest",
        "visualization"],
    entry_points={
        "console_scripts": ["firearm_analysis = python_files.main:main",],},
    python_used=">=3.10.12",
)

# Bibliografía: https://gist.github.com/discdiver/bfa7a23fb3147442dd1229cd482103dd
# https://github.com/pypa/setuptools/blob/main/docs/userguide/quickstart.rst