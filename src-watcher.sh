#!/usr/bin/env observr
# Install https://github.com/kevinburke/observr/
# Make sure that venv is activated
watch('src/.*') { system('fab build') }
