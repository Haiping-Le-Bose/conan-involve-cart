# Check if conancenter remote is defined and advise to remove it.

import json, subprocess

from conan import ConanFile

def get_remotes():
    remotes = subprocess.run(['conan', 'remote', 'list', '--format', 'json'], capture_output=True, check=True, text=True).stdout
    return json.loads(remotes)

def pre_generate(conanfile: ConanFile):
    for remote in get_remotes():
        if remote['name'] == 'conancenter' or remote['url'].startswith('https://center.conan.io'):
            conanfile.output.warning((f"Remote {remote['name']} with url {remote['url']} detected in remotes."
                                       " Please remove it, this external repository should not be used."
                                      f" Use 'conan remote remove {remote['name']}' to remove it."))
