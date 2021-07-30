from setuptools import setup
from setuptools_rust import Binding, RustExtension

extras = {}
extras["testing"] = ["pytest"]

setup(
    name="navsearch",
    version="0.1.0a1",
    description="A package for searching Navy instructions",
    author="Colin Dablain",
    author_email="colin.dablain@r3th.ink",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/DayOfThePenguin/navsearch",
    python_requires=">=3.8",
    rust_extensions=[RustExtension(
        "navsearch.rust2py", binding=Binding.PyO3)],
    classifiers=[
        "Development Status: : 3 - Alpha",
        "Programming Language:: Python:: 3.8",
        "License:: OSI Approved:: GNU Affero General Public License v3 or later(AGPLv3+)",
        "Operating System:: OS Independent"
    ],
    install_requires=[
        "psycopg2==2.9.1",
        "pydantic==1.8.2",
        "SQLAlchemy==1.4.20",
    ],
    package_dir={"": "py_src"},
    packages=[
        "navsearch",
        "navsearch.scraper",
    ],
    # rust extensions are not zip safe, just like C-extensions.
    zip_safe=False,
)
