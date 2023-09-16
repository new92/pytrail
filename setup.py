from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf8') as readme:
    long_description = readme.read()

setup(
    name='pytrail',
    version='0.1.0',
    license='MIT',
    description='The pytrail module simplifies the process of fetching movie trailers programmatically. It offers a user-friendly interface to search for and retrieve the latest trailers for a wide range of movies. Integrate this module into your projects to effortlessly access and showcase movie trailers, enhancing your movie-related applications and websites.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='new92',
    author_email='new92github@gmail.com',
    maintainer='new92',
    maintainer_email='new92github@gmail.com',
    keywords='python movies trailer cinema',
    url='https://www.github.com/new92/pytrail',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    python_requires='>=3.6',
    project_urls={
        'Github Repository': 'https://github.com/new92/pytrail'
    }
)