from conan import ConanFile
from conans.util.files import rmdir

import os, shutil

def deploy(graph, output_folder: str, **kwargs):
    """
    Deploy host dependencies to output_folder + deps/dep_name subfolder
    """
    conanfile: ConanFile = graph.root.conanfile
    deploy_folder = os.path.join(output_folder, 'deps')

    conanfile.output.info(f'Simple host dependency deployment to {deploy_folder}')

    rmdir(deploy_folder)

    for dep in conanfile.dependencies.host.values():
        if not dep.package_folder:
            conanfile.output.info(f'Skipping deploy of {dep.ref.name}, no package folder defined')
            continue

        shutil.copytree(dep.package_folder, os.path.join(deploy_folder, dep.ref.name))
