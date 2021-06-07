FROM fedora:34
MAINTAINER horky@d3s.mff.cuni.cz
LABEL maintainer="horky@d3s.mff.cuni.cz"

RUN curl "https://download.java.net/java/GA/jdk9/9/binaries/openjdk-9_linux-x64_bin.tar.gz" -o /tmp/openjdk-9_linux-x64_bin.tar.gz \
    && tar -xz -C /opt -f /tmp/openjdk-9_linux-x64_bin.tar.gz \
    && rm -f /tmp/openjdk-9_linux-x64_bin.tar.gz \
    && printf 'export JAVA_HOME="%s"\nexport PATH="$JAVA_HOME/bin:$PATH"\n' "/opt/jdk-9" >/etc/profile.d/java_in_opt.sh

CMD ["/bin/bash"]
