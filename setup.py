from setuptools import setup


setup(
    name="fir",
    version="1.0.0",
    packages=["fir", "fir.commands", "fir.io", "fir.generators"],
    install_requires=["Click"],
    entry_points={
      "console_scripts": [
          "fir = fir.entry:cli",
      ]
    }
)
