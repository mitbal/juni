import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="juni",
    version="0.0.1",
    author="M Iqbal Tawakal",
    author_email="mit.iqi@gmail.com",
    description="A small library for creating pretty heatmaps of daily data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    license="MIT",
    url="https://github.com/mitbal/juni/",
    keywords=[
        "heatmap",
        "visualisation",
        "calendar",
        "daily",
        "matplotlib",
        "github plot",
        "month plot",
        "date plot",
        "plot",
        "plotting",
    ],
    classifiers=[
        "Topic :: Scientific/Engineering :: Visualization",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "matplotlib==3.9.0",
        "numpy==1.26.4",
    ],
    python_requires=">=3.6",
)
