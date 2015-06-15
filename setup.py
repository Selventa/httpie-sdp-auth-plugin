from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass

setup(
    name='sdp-api-auth',
    description='SDPAuth plugin for HTTPie.',
    long_description='Provides an authentication module to authenticate API URLs for SDP.',
    version='0.1.0',
    author='Anthony Bargnesi',
    author_email='abargnesi@selventa.com',
    license='MIT',
    url='https://github.com/Selventa/sdp-api-auth',
    download_url='https://github.com/Selventa/sdp-api-auth',
    py_modules=['sdp_api_auth'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'sdp_api_auth = sdp_api_auth:SDPAuthPlugin'
        ]
    },
    install_requires=[
        'httpie>=0.7.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Environment :: Plugins',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Utilities'
    ],
)
