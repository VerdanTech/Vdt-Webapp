#
# If an environment variable file does not already exist,
# create one by copying over the development defaults
#
.PHONY: build
build:
	curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.5/install.sh | bash
	nvm install node
	nvm use node