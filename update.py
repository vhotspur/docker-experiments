#!/usr/bin/env python3

VERSIONS = [
    {
        "name": "jdk8",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "package": "java-1.8.0-openjdk-devel",
    },
    {
        "name": "jdk9",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk9/9/binaries/openjdk-9_linux-x64_bin.tar.gz",
        "basedir": "jdk-9",
    },
    {
        "name": "jdk10",
        "maintainer": "horky@d3s.mff.cuni.cz",
        "tarball": "https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_linux-x64_bin.tar.gz",
        "basedir": "jdk-10.0.2",
    },
]

DOCKERFILE_TEMPLATE_FROM_PACKAGE = '''
FROM fedora:34
MAINTAINER {maintainer_email}
LABEL maintainer="{maintainer_email}"

RUN dnf install -y ca-certificates git \\
    && dnf install -y {package} \\
    && dnf clean all


CMD ["/bin/bash"]

'''

DOCKERFILE_TEMPLATE_FROM_TARBALL = """
FROM fedora:34
MAINTAINER {maintainer_email}
LABEL maintainer="{maintainer_email}"

RUN dnf install -y ca-certificates git \\
    && dnf clean all \\
    && curl "{tarball_url}" -o "/tmp/{tarball_basename}.tar.gz" \\
    && tar -xz -C /opt -f "/tmp/{tarball_basename}.tar.gz" \\
    && rm -f "/tmp/{tarball_basename}.tar.gz" \\
    && printf 'export JAVA_HOME="%s"\\nexport PATH="$JAVA_HOME/bin:$PATH"\\n' "/opt/{tarball_basedir}" >/etc/profile.d/java_from_opt.sh \\
    && ln -sf /etc/pki/java/cacerts /opt/jdk-9/lib/security/ \\
    && /opt/{tarball_basedir}/bin/java -version


CMD ["/bin/bash"]

"""

def update_version(dockerfile, config):
    if 'package' in config:
        dockerfile.write(DOCKERFILE_TEMPLATE_FROM_PACKAGE.format(
            maintainer_email=config['maintainer'],
            package=config['package'],
        ))
    else:
        dockerfile.write(DOCKERFILE_TEMPLATE_FROM_TARBALL.format(
            maintainer_email=config['maintainer'],
            tarball_basename=config['basedir'],
            tarball_basedir=config['basedir'],
            tarball_url=config['tarball'],
        ))

def main():
    for ver in VERSIONS:
        with open('buildenv-{}/Dockerfile'.format(ver['name']), 'w') as f:
            update_version(f, ver)

if __name__ == '__main__':
    main()
