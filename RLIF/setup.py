from setuptools import find_packages, setup

setup(
    name="RLIF",
    version="2025.04.07",
    author="Sy Nguyen",
    author_email="",
    description="Reinforcement learning using SAC & Imitation learning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Syaagain/RLIF",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8, <3.11",
    install_requires=[
    "absl-py==1.4.0",
    "appdirs==1.4.4",
    "cachetools==5.3.0",
    "certifi==2023.5.7",
    "charset-normalizer==3.1.0",
    "click==8.1.3",
    "cloudpickle==2.2.1",
    "colorama==0.4.4",
    "commonmark==0.9.1",
    "cycler==0.11.0",
    "decorator==4.4.2",
    "docker-pycreds==0.4.0",
    "docstring-parser==0.15",
    "farama-notifications==0.0.4",
    "fastapi==0.115.8",
    "filelock==3.12.0",
    "fonttools==4.38.0",
    "gitdb==4.0.10",
    "gitpython==3.1.31",
    "glfw==1.12.0",
    "google-auth-oauthlib==0.4.6",
    "google-auth==2.18.0",
    "grpcio==1.54.0",
    "gym-notices==0.0.8",
    "gym==0.23.1",
    "gymnasium==0.28.1",
    "huggingface-hub==0.11.1",
    "idna==3.4",
    "imageio-ffmpeg==0.3.0",
    "imageio==2.28.1",
    "jax-jumpy==1.0.0",
    "kiwisolver==1.4.4",
    "markdown==3.3.7",
    "markupsafe==2.1.2",
    "matplotlib==3.5.3",
    "moviepy==1.0.3",
    "mujoco==2.3.3",
    "numpy==1.24.4",
    "oauthlib==3.2.2",
    "opencv-python==4.11.0.86",
    "packaging==23.1",
    "pandas==1.3.5",
    "pathtools==0.1.2",
    "pathlib2==2.3.6",
    "pillow==9.5.0",
    "prettytable==3.14.0",
    "proglog==0.1.10",
    "protobuf==3.20.3",
    "psutil==5.9.5",
    "pyasn1-modules==0.3.0",
    "pyasn1==0.5.0",
    "pydantic==2.10.6",
    "pygame==2.1.0",
    "pygments==2.15.1",
    "pyopengl==3.1.6",
    "pyparsing==3.0.9"
],

    entry_points={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    keywords="reinforcement learning,imitation learning, human feedback, AI",
)
