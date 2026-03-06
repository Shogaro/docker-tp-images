FROM python:3.12-slim AS builder
WORKDIR /builder
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install --prefix=/install -r requirements.txt
COPY . .

FROM python:3.12-alpine AS runtime
WORKDIR /app
COPY --from=builder /install /usr/local
COPY . .
EXPOSE 8080
CMD [ "python", "app.py" ]