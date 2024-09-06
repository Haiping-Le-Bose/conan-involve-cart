# conan-by-example
Examples to learn conan concepts

## Prerequisites
We have tried to make each example as self contained as possible, but there still are a few prerequisites:
1. Conan must be installed. You can install any version `2.2.2` or newer in your Python environment by running `pip install conan=2.2.2`
2. You must have access to Artifactory, specifically the `asd-conan` conan repository. You will need to set your authentication in these environment variables:
   1. `CONAN_LOGIN_USERNAME` is your Artifactory username, ex: ab12345@bose.com
   2. `CONAN_PASSWORD` is an Artifactory identity token

## Notes
1. By making the examples self contained we may have hard coded some things like the conan configuration, note that this is not recommended for project development.
2. Check each examples `README` for information about the example.
3. For all examples the conan home is configured by the .conanrc file to be the `.conan2` folder in this repository.
4. We use cmake in these examples, but conan can integrate with any build tool
