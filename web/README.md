# Web Application
```sh
# sync static web files
rsync -Pav -e "ssh -i $HOME/.ssh/framework.pem" ubuntu@ogre.dgbellomy.com:web/* static/*
```

## AWS EC2 Setup
```sh
sudo apt update
sudo apt-get install -y nginx
```

## Install NodeJS and npm
https://nodejs.org/en/download/package-manager
```
# installs NVM (Node Version Manager)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

# download and install Node.js
nvm install 20

# verifies the right Node.js version is in the environment
node -v # should print `v20.11.1`

# verifies the right NPM version is in the environment
npm -v # should print `10.2.4`
```
