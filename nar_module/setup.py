from setuptools import setup, find_packages

REQUIRED_PACKAGES = [
    'google-cloud-storage==1.10.0'
    #'tensorflow==1.8'
]

setup(
    name='chameleon_nar',
    version='0.5.0',
    description='CHAMELEON - ACR module',
    url='https://github.com/gabrielspmoreira/chameleon_recsys',
    # Author details
    author='Gabriel de Souza Pereira Moreira',
    author_email='gspmoreira [at] gmail.com',
    # Choose your license
    license='MIT',
    install_requires=REQUIRED_PACKAGES,
    #extras_require={
        ##'prediction':  ['google-api-python-client']
    #},
    packages=find_packages()
)
