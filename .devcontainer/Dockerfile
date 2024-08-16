# Python and Node base image
FROM nikolaik/python-nodejs:python3.12-nodejs22

# Working directory
WORKDIR /workdir

# Install backend dependencies
COPY ./backend/requirements ./backend/requirements
RUN pip install --upgrade pip && \
    pip install uv && \
    uv pip install --system -r backend/requirements/dev.txt

# Install frontend dependencies
COPY ./frontend/package.json ./frontend/pnpm-lock.yaml ./
RUN npm install -g pnpm
RUN pnpm i

COPY . .