from setuptools import setup, find_packages

setup(
    name='lumimedia-sdk',
    version='0.1.0',
    description=(
        'Lightweight Python SDK for basic media upload, compression, '
        'and metadata retrieval.'
    ),
    author='Noa Sasson',
    author_email='your_email@example.com',
    url='https://github.com/rainbowgore/lumimedia-sdk',
    packages=find_packages(exclude=['tests', 'demo', 'docs']),
    install_requires=[
        'requests>=2.25.1',
        'pillow>=8.0.0',
        'python-dotenv>=0.15.0',
        'tqdm>=4.50.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.8',
)