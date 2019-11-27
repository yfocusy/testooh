
FROM python:3.5

ENV CHROME_DRIVER_VERSION 2.42
ENV CHROME_DRIVER_TARBALL http://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip

RUN \
    echo "==> Install common stuff missing from the slim base image..."   && \
    apt-get update            && \
    apt-get install -y --no-install-recommends \
        gnupg   \
        dirmngr \
        wget    \
        ca-certificates               && \
        rm -rf /var/lib/apt/lists/*   && \
    \
    \eb
    echo "==> Add Google repo for Chrome..."   && \
    wget -q -O- https://dl.google.com/linux/linux_signing_key.pub | apt-key add -  && \
    echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google.list  && \
    \
    \
    echo "==> Install prerequisite stuff..."   && \
    apt-get update            && \
    apt-get install -y --no-install-recommends \
        python3-dev              \
        python3-pip              \
        xvfb                     \
        libfontconfig            \
        libfreetype6             \
        xfonts-scalable          \
        fonts-liberation         \
        fonts-noto-cjk           \
        google-chrome-stable  && \
    \
    \
    echo "==> Install ChromeDriver..."   && \
    wget -qO- $CHROME_DRIVER_TARBALL | zcat > /usr/local/bin/chromedriver  && \
    chown root:root /usr/local/bin/chromedriver  && \
    chmod 0755 /usr/local/bin/chromedriver       && \
    \
    \
    \
    echo "==> Install useful Python stuff..."   && \
    pip3 install --no-cache-dir \
        requests                \
        unittest-xml-reporting  \
        nose                    \
        mockito                 \
        pyshould                \
                                && \
    \
    \
    echo "==> Install behave and related stuff..."   && \
    pip3 install --no-cache-dir \
        behave                  \
        selenium                \
        elementium              \
        capybara-py             \
        xvfbwrapper             && \
    \
    \
    echo "==> Clean up..."      && \
    rm -rf /var/lib/apt/lists/*


ENV PATH /usr/lib/chromium/:$PATH

WORKDIR    /behave
ENV        REQUIREMENTS_PATH  /behave/features/steps/requirements.txt

COPY       wrapper.sh  /tmp
ENTRYPOINT ["/tmp/wrapper.sh"]


