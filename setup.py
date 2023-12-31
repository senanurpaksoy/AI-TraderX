from glob import glob
from os.path import basename, splitext

from setuptools import find_packages, setup

VERSION = "0.0.0.1"
README_PATH = "src/Docs/README.md"

# test_requirements = ["behave", "behave-classy", "pytest"]

long_description = ""
with open(README_PATH, "r", encoding="utf-8") as file:
    long_description = file.read()


setup(
    name="AITradeX",
    version=VERSION,
    license="Apache Software License 2.0",
    description="AI-TraderX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="AfpTheDev",
    author_email="ahmetfarukpala@gmail.com",
    url="https://github.com/senanurpaksoy/AI-TraderX",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        # uncomment if you test on these interpreters:
        # "Programming Language :: Python :: Implementation :: IronPython",
        # "Programming Language :: Python :: Implementation :: Jython",
        # "Programming Language :: Python :: Implementation :: Stackless",
        "Topic :: Utilities",
    ],
    project_urls={
        "Changelog": "https://github.com/yedhrab/YPackage/blob/master/docs/CHANGELOG.md",
        "Issue Tracker": "https://github.com/yedhrab/YPackage/issues",
    },
    keywords=[],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    install_requires=["requests"], # Bağlı olduğu paketler, örn: requests
    extras_require={
        # eg:
        #   "rst": ["docutils>=0.11"],
        #   ":python_version=="2.6"": ["argparse"],
    },
    setup_requires=[
        "pytest-runner",
    ],
    entry_points={
        # Komut isteminden çalıştırma
        # örndeğin: ypackage
        # Kullanım: "ypacakge = ypackage.ypackage:main
        "console_scripts": [
            "ygitbookintegration = ypackage.cli.integrate_into_gitbook:main",
            "ygoogledrive = ypackage.cli.gdrive:main",
            "ygooglesearch = ypackage.cli.gsearch:main",
            "yfilerenamer = ypackage.cli.file_renamer:main",
            "ythemecreator = ypackage.cli.theme_creator:main"
        ]
    },
    # tests_require=test_requirements,
)
