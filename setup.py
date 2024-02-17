import setuptools

with open("requirements.txt", "r") as req:
    requirements = req.read().splitlines()

setuptools.setup(
    name="dispander",
    version="0.5.0",
    author="1ntegrale9",
    author_email="1ntegrale9uation@gmail.com",
    description="Discord Message URL Expander",
    long_description="Discord Message URL Expander",
    long_description_content_type="text/markdown",
    url="https://github.com/DiscordBotPortalJP/dispander",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=requirements,
)
