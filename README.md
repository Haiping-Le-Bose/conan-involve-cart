# Involve CART With Conan
Example of involving cart release via conan

## Prerequisites
1. Conan

       haiping@ubuntu:~/Desktop/conan-involve-cart/hello-world$ conan version
         version: 2.7.0
         conan_path: /home/haiping/.local/bin/conan
         python
         version: 3.10.14

         sys_version: 3.10.14 (main, Apr  6 2024, 18:45:05) [GCC 9.4.0]
         sys_executable: /usr/bin/python3.10
         is_frozen: False
         architecture: x86_64

    Python3 should be upgraded and the guidance can be found in https://wiki.bose.com/display/ABSPT/conan+example

2. You must have access to Artifactory, specifically the `asd-conan` conan repository. You will need to set your authentication in these environment variables:
   1. `CONAN_LOGIN_USERNAME` is your Artifactory username, ex: ab12345@bose.com
   2. `CONAN_PASSWORD` is an Artifactory identity token

## Notes
1. By making the example self contained we may have hard coded some things like the conan configuration, note that this is not recommended for project development.
2. The conan home is configured by the .conanrc file to be the `.conan2` folder in this repository.
3. We use cmake in these examples, but conan can integrate with any build tool.

