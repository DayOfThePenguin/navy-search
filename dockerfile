FROM apache/tika:latest-full

ARG USER_ID
ARG GROUP_ID

RUN addgroup --gid $GROUP_ID user
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID user
USER user

ENV PATH="/home/user/.local/bin:$PATH"

WORKDIR /home/user