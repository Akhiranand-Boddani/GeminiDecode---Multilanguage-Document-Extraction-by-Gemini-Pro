from setuptools import setup, find_packages

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gemini-decode",
    version="1.0.0",
    author="GeminiDecode Team",
    author_email="example@example.com",
    description="A tool for extracting structured information from multilingual documents using Google's Gemini Pro Vision API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/geminidecode",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "gemini-decode=app:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.md", "LICENSE", ".streamlit/*"],
    },
)