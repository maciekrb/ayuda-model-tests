import io
import os
import setuptools
from subprocess import call

name = "ayuda-test-run"
description = "Test runner for Ayuda playlog logic"
version = "0.0.1"

# Should be one of:
# 'Development Status :: 3 - Alpha'
# 'Development Status :: 4 - Beta'
# 'Development Status :: 5 - Production/Stable'
release_status = "Development Status :: 3 - Alpha"
dependencies = ["pydantic>=0.21", "pytest>=4.4.1", "pytest-cov>=2.6.1"]
extras = {"test": ["coverage", "pytest", "pytest-cov"]}

# Boilerplate below this line
package_root = os.path.abspath(os.path.dirname(__file__))


class RunTests(setuptools.Command):
    """Run all tests."""

    description = "run tests"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run all tests!"""
        errno = call(["py.test", "--cov=ayuda", "--cov-report=term-missing", "tests/"])
        raise SystemExit(errno)


setuptools.setup(
    name=name,
    version=version,
    description=description,
    long_description="N/A",
    author="AdMobilize Team",
    author_email="devel@admobilize.com",
    classifiers=[
        release_status,
        "Intended Audience :: Developers",
        "Unlicensed",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    platforms="Posix; MacOS X; Windows",
    packages=setuptools.find_packages(),
    install_requires=dependencies,
    extras_require=extras,
    cmdclass={"test": RunTests},
    python_requires=">=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*",
    zip_safe=True,
)
