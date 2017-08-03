# Ubuntu Homestead/Laravel  installation script [![Build Status](https://travis-ci.org/GabrielSturtevant/homestead_installer.svg?branch=master)](https://travis-ci.org/GabrielSturtevant/homestead_installer)

This script is for my own personal use. Use it with caution as I have not written it with systems other than my own in mind

The master branch will be tailored to the current Ubuntu LTS release

Current LTS: 16.04


This script can be executed via a curl command. It will run and install laravel and homestead to default locations, but if you need to modify these defaults, you can use environment variables. The following is an example of this functionality:
```
export SCRIPTS_URL='git@github.com:csun-metalab/etd-v3.git' && export SCRIPTS_URL_NAME='etdv3' && export SCRIPTS_DIR_NAME='ETD-V3' && export SCRIPTS_DIR_PATH='Code/Meta' && export SCRIPTS_CORES='2' && curl https://raw.githubusercontent.com/GabrielSturtevant/scripts/master/ubuntuHomestead.py | python3
```

For more information on how to use the environment variables with this script, please see the [wiki](https://github.com/GabrielSturtevant/homestead_installer/wiki/Environment-Variables).
