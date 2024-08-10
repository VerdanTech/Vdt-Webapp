FROM node:alpine

# Use whichever container directory you want as long
# as you make sure to use it consistently in further
# configuration. I'll just use '/app' here for simplicity.
WORKDIR /workdir

# Install frontend dependencies
COPY ./package.json ./pnpm-lock.yaml .
RUN npm install -g pnpm
RUN pnpm install

COPY . .

# Using the --host 0.0.0.0 option (which is passed to Vite)
# was the only way I could get the dev/HMR mode to be
# accessible from outside the container.
CMD npm run dev -- --host 0.0.0.0
