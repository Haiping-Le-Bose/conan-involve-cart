from conan import ConanFile
from conan.tools.cmake import CMake, CMakeDeps, CMakeToolchain, cmake_layout

class HelloWorldRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("release_rd8295/0.0.4@bosecorp")

    def build_requirements(self):
        # self.tool_requires("cmake/3.27.5@conan-center-index")
        # self.tool_requires("make/4.4@conan-center-index")
        return

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def layout(self):
        cmake_layout(self)
