#!/usr/bin/env python3

VERSIONS = [
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

DOCKERFILE_TEMPLATE = '''
FROM fedora:34
MAINTAINER {maintainer_email}
LABEL maintainer="{maintainer_email}"

RUN curl "{tarball_url}" -o "/tmp/{tarball_basename}.tar.gz" \\
    && tar -xz -C /opt -f "/tmp/{tarball_basename}.tar.gz" \\
    && rm -f "/tmp/{tarball_basename}.tar.gz" \\
    && printf 'export JAVA_HOME="%s"\\nexport PATH="$JAVA_HOME/bin:$PATH"\\n' "/opt/{tarball_basedir}" >/etc/profile.d/java_from_opt.sh

CMD ["/bin/bash"]

'''

def update_version(dockerfile, config):
    dockerfile.write(DOCKERFILE_TEMPLATE.format(
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
