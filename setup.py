from setuptools import setup, find_packages

setup(
    name="hello_package",  # Package ka naam
    version="0.1.0",    # Version number
    author="Your Name",
    author_email="your.email@example.com",
    description="A simple Python package example",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/my_package",  # Optional
    packages=find_packages(),  # Automatically packages dhundega
    install_requires=[
        # Dependencies yahan list kare, e.g., "requests>=2.25.1"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)