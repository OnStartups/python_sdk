from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agentdotai",
    version="0.1.0",
    author="Andrei Oprisan",
    author_email="andrei@agent.ai",
    description="A Python client for the Agent.ai API",
    long_description="A Python client for the Agent.ai API, allowing you to interact with the API using Python, such as running actions and agents.",
    long_description_content_type="text/markdown",
    url="https://github.com/OnStartups/python_sdk",
    packages=find_packages(where='agentdotai'),
    package_dir={'': 'agentdotai'},
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7'
)
