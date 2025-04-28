from setuptools import setup, find_packages

setup(
    name='lumimedia_sdk',
    version='0.1.0',
    description='Lightweight Python SDK for basic media upload, compression, and metadata retrieval.',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pillow',
        'python-dotenv',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.7',
)
