from conans import ConanFile, AutoToolsBuildEnvironment, tools

class NloptConan(ConanFile):
    name = "nlopt"
    version = "2.4.2"
    license = "MIT"
    url = "https://github.com/vthiery/conan-nlopt"
    author = "Vincent Thiery (vjmthiery@gmail.com)"
    ZIP_FOLDER_NAME = "nlopt-%s" % version
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        zip_name = "nlopt-%s.tar.gz" % self.version
        tools.download("http://ab-initio.mit.edu/nlopt/%s" % zip_name, zip_name, retry=2, retry_wait=5)
        tools.unzip(zip_name)

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        with tools.environment_append(env_build.vars):
            with tools.chdir(self.ZIP_FOLDER_NAME):
                env_build.configure()
                env_build.make()
                self.run("sudo make install")

    def package(self):
        self.copy("*.h*", dst="include", src="include", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["nlopt"]
