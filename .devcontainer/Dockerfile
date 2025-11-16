FROM mcr.microsoft.com/vscode/devcontainers/typescript-node AS base

WORKDIR /workspace

ENV PNPM_HOME="/workspace/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable pnpm

COPY . .