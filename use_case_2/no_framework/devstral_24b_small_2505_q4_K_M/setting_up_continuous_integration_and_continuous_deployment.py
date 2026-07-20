# Create .github/workflows/main.yml

with open(".github/workflows/main.yml", "w") as f:
    f.write('''
name: Node.js Package

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    strategy:
      matrix:
        node-version: [14.x]

    steps:
    - uses: actions/checkout@v2
    - name: Use Node.js ${{ matrix.node-version }}
      uses: actions/setup-node@v2
      with:
        node-version: ${{ matrix.node-version }}
    - run: npm install
    - run: npm test
''')

# Note: This is just a template for CI/CD. You'll need to customize it based on your actual setup and requirements.