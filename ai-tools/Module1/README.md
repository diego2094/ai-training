# Comparison: Documentation-First vs. Vibe Coding

## Endpoint A: GET /api/users

- Created using `ENDPOINT_A_SPEC.md`.
- Observations:
  - Clarity from the start, less confusion about params (`page`, `limit`).
  - The AI assistant aligned well with the specification.

## Endpoint B: POST /api/users

- Created via "vibe coding" (no prior doc).
- Observations:
  - Quicker to prototype, but sometimes I needed more back-and-forth with the AI to clarify fields.
  - Freed me to experiment or add features spontaneously (e.g., the ID generation logic).

## Potential Improvements

- Both approaches can coexist: start with essential doc for bigger endpoints, then vibe additional features.
- The AI might need more context for advanced validations or error handling.
