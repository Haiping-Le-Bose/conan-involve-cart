# Global Conan Configuration
This repository contains our global configuration, including:
- remotes (package repositories)
- recipe settings (settings.yml)
- core configuration (global.conf)
- profiles
- hooks
- custom deployers

# Profiles
See [conan profiles](CONAN_PROFILES.md) for information on profile definition and organization.

- Default build profile - `x86_64-linux-gcc11-release`
- Default host profile - `x86_64-linux-gcc11-release`

## Build Configuration Profiles
- `aarch64le-qnx-neutrino-qcc8.3-debug`
- `aarch64le-qnx-neutrino-qcc8.3-release`
- `x86_64-linux-gcc11-debug`
- `x86_64-linux-gcc11-release`

## Tool Profiles
- `tools/cmake-makefiles`
- `tools/make`

# Remotes
This is a list of repositories containing conan packages.
BE AWARE -- they are examined in the order defined, which can affect package resolution.

# Hooks
The following hooks are implemented:
- Detect and warn about the use of external conancenter remote
- Detect and warn about potential typos of conanfile class members

# Deployers
Custom deployers, see [deployers](https://docs.conan.io/2/reference/extensions/deployers.html) for the built-in ones.
- `simple_host_deploy` - Deploy host dependencies in a simple structure `deps/dep_name/`

# Setup

## Install Conan
With Python 3 installed, execute
`pip install conan==2.2.2`

## Install this repository's conan configuration
`conan config install git@github.com:BoseCorp/asd-conan-config.git`

## Authenticate to Artifactory remotes
Login to Artifactory (https://artifactory.bose.com/ui/login/).
Under your profile generate a new Identity token.

Execute `conan remote auth '*'` to authenticate against each configured conan remote. For Artifactory remotes provide your username (ab12345@bose.com) and the Identity token as your password.

> [!NOTE]
> The `conancenter` remote will be used while we build out the infrastructure. This remote does not require authentication, so you can ignore any errors.

Verify the remotes are authenticated with `conan remote list-users`

### Backup source authentication
We have configured Artifactory as a backup cache for sources downloaded from external locations.

The backup cache requires an authentication token, which is expected to come from the `ARTIFACTORY_TOKEN` or `CONAN_PASSWORD` environment variable (an Artifactory token).
