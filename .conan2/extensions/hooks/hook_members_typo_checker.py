# Look for potential typos in the members of the conanfile.
#
# From https://github.com/conan-io/hooks/blob/master/hooks/members_typo_checker.py
# Updated for conan v2

import inspect
from difflib import get_close_matches

from conan import ConanFile


def pre_export(conanfile: ConanFile):
    def get_base_members(conanfile):
        return [m[0] for m in inspect.getmembers(conanfile) if not m[0].startswith('_')]

    base_members = get_base_members(ConanFile)
    base_members.extend(["extension_properties",
                        "languages",
                        "options_description",
                        "package_id_embed_mode",
                        "package_id_non_embed_mode",
                        "package_id_python_mode",
                        "package_id_unknown_mode",
                        "python_requires",
                        "python_requires_extend",
                        "required_conan_version",
                        "source_buildenv",
                        "test_package_folder"])

    # This is a mock property in v2, and will be removed at some point. Conan will warn that
    # it is deprecated, so we can skip checking it here.
    base_members.extend(["env_info"])

    def get_members(conanfile):
        # We use a different function on the conanfile because members
        # `user` and `channel` throw an Exception on access when they're empty
        return [m for m in dir(conanfile) if not m.startswith('_')]

    for member in get_members(conanfile):
        if member in base_members:
            continue

        matches = get_close_matches(
            word=member, possibilities=base_members, n=5, cutoff=0.80)
        if len(matches) == 0:
            continue

        conanfile.output.warning("The '%s' member looks like a typo. Similar to:" % member)
        for match in matches:
            conanfile.output.warning("    %s" % match)
