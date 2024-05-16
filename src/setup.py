from setuptools import setup


setup(name='mlpro-int-mujoco',
version='1.0.1',
description='MLPro: Integration MuJoCo',
author='MLPro Team',
author_mail='mlpro@listen.fh-swf.de',
license='Apache Software License (http://www.apache.org/licenses/LICENSE-2.0)',
packages=['mlpro_int_mujoco'],

# Package dependencies for full installation
extras_require={
    "full": [
        "mlpro[full]>=1.4.4",
        "mujoco>=3.1.2",
        "lxml>=4.9.2"
    ],
},

zip_safe=False)