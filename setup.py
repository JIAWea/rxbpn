from setuptools import setup

setup(
    name='rxbpn',
    version='0.0.1',
    description='A back-pressured RxPy extension with request n',
    url='https://github.com/JIAWea/rxbpn',
    author='Ray Wong',
    author_email='',
    license='BSD 3-Clause',
    packages=[
        'rxbpn',
    ],
    zip_safe=True,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords=['rx reactive extension back-pressure backpressure flowable request-n'],
    python_requires='>=3.7',
)
