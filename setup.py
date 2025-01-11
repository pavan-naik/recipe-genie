from setuptools import setup, find_packages

setup(
    name="recipe-genie",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "gradio",
        "transformers",
        "torch",
        "huggingface-hub"
    ],
)