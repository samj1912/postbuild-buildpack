# postBuild Buildpack

![Version](https://img.shields.io/badge/dynamic/json?url=https://cnb-registry-api.herokuapp.com/api/v1/buildpacks/sam/postbuild&label=Version&query=$.latest.version)

This is a [Cloud Native Buildpack](https://buildpacks.io) that checks if a `postBuild` executable exists and runs it in the application directory.
## Usage

The buildpack will automatically run a `postBuild` script present in your application directory. For example, create a file called `postBuild` in your application directory with the contents - 

```bash
#!/bin/bash

echo "Hello World"
ls -l
```

```bash
pack build --buildpack sam/post-build myapp
```

