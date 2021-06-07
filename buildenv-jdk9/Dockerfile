
FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN dnf install -y ca-certificates git \
    && dnf clean all \
    && curl "https://download.java.net/java/GA/jdk9/9/binaries/openjdk-9_linux-x64_bin.tar.gz" -o "/tmp/jdk-9.tar.gz" \
    && tar -xz -C /opt -f "/tmp/jdk-9.tar.gz" \
    && rm -f "/tmp/jdk-9.tar.gz" \
    && printf 'export JAVA_HOME="%s"\nexport PATH="$JAVA_HOME/bin:$PATH"\n' "/opt/jdk-9" >/etc/profile.d/java_from_opt.sh \
    && ln -sf /etc/pki/java/cacerts /opt/jdk-9/lib/security/ \
    && /opt/jdk-9/bin/java -version


CMD ["/bin/bash"]

