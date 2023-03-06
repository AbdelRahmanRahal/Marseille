from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.1'
DESCRIPTION = 'Voice assistant bot in the works'
LONG_DESCRIPTION = 'Marseille, a voice assistant bot that can help you with various tasks and answer various questions'

setup(
    name = "Marseille",
    version = VERSION,
    author = "AbdelRahman Rahal",
    # author_email="<mail@neuralnine.com>",
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    long_description = long_description,
    packages = find_packages(),
    install_requires = ['os', 'pillow', 'pyglet', 'pyttsx3', 'speechrecognition', 'sys', 'tkinter'],
    keywords = ['python', 'Marseille', 'voice assistant', 'bot', 'voice assistant bot', 'ai', 'speech recognition'],
    classifiers = [
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)