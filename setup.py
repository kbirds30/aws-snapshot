from setuptools import setup

setup(
    name='ec2stop',
    version='0.1',
    author="Keith Birdsall",
    author_email="kbirds30@gmail.com",
    desciption="ec2 stop start create and delete",
    license="GPLv3+",
    packages=['shotty'],
    url="https://github.com/kbirds30/aws-snapshot/blob/master/shotty/shotty.py",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',
)
