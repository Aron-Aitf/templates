FROM python:3-slim-bookworm

WORKDIR /main

COPY . .

RUN pip install --no-cache-dir --upgrade --root-user-action ignore pip && pip install --no-cache-dir --root-user-action ignore "fastapi[standard]" sqlmodel psycopg2-binary semver pydantic_extra_types

CMD ["fastapi", "run", "src/main.py", "--workers", "17"]

