# GitHub Action to API Docker



```yaml
name: Upload Website

on:
  push:
    branches:
    - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master

    - name: Declare some variables
      id: vars
      shell: bash
      run: |
        echo "##[set-output name=branch;]$(echo ${GITHUB_REF#refs/heads/})"
        echo "::set-output name=sha_short::$(git rev-parse --short HEAD)"
        echo "::set-output name=dc_b64::$(cat docker-compose.yml | base64 -w 0)"

    - name: Update stack API Docker
      uses: roanfranklin/api-docker-action@main
      env:
        URL: https://apidocker.mydomains.com.br
        USERNAME: ${{ secrets.USERNAME }}
        PASSWORD: ${{ secrets.PASSWORD }}
        STACK: webapp
        ISBASE64: True
        ENVIRONMENT: WEBAPP_IMAGE_TAG=${{ steps.vars.outputs.sha_short }};VAR1=ASD;VAR2=OIU
        DOCKERCOMPOSE: ${{ steps.vars.outputs.dc_b64 }}
```


## License

This project is distributed under the [MIT license](LICENSE.md).
