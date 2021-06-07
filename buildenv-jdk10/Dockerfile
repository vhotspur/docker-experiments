FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN curl "https://download.java.net/java/GA/jdk10/10.0.2/19aef61b38124481863b1413dce1855f/13/openjdk-10.0.2_linux-x64_bin.tar.gz" -o /tmp/openjdk-10.0.2_linux-x64_bin.tar.gz \
    && tar -xz -C /opt -f /tmp/openjdk-10.0.2_linux-x64_bin.tar.gz \
    && rm -f /tmp/openjdk-10.0.2_linux-x64_bin.tar.gz \
    && printf 'export JAVA_HOME="%s"\nexport PATH="$JAVA_HOME/bin:$PATH"\n' "/opt/jdk-10.0.2" >/etc/profile.d/java_opt.sh

CMD ["/bin/bash"]
