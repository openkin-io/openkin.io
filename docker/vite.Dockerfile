FROM node:20 AS base
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_PATH:$PATH"
RUN corepack enable
COPY . /app
WORKDIR /app

FROM base AS deps
RUN --mount=type=cache,id=pnpm,target=/pnpm/store pnpm install --prod --frozen-lockfile

FROM base
COPY --from=deps /app/node_modules /app/node_modules

EXPOSE 5173

CMD [ "pnpm", "run", "dev" ]
