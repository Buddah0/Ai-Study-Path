# Contributing

Thank you for your interest in contributing to the AI Course Prerequisite Validator. We welcome bug reports, feature requests, documentation improvements, and code contributions.

Please read this document before opening issues or submitting pull requests.

---

## How to get started

1. **Fork the repository** and create a feature branch from `main`:
   - `git checkout -b feat/your-feature`
2. **Run tests** and linters locally before submitting a PR.
3. **Open an issue** first for larger features or design changes to discuss approach.

---

## Developer Certificate of Origin (DCO) Sign-off

We require that all commits included in pull requests are signed off using the Developer Certificate of Origin (DCO). This is a lightweight way to assert that you have the right to contribute the code and that you agree to the contribution terms.

**How to sign off a commit**

- Add a sign-off when committing locally:
  - `git commit -s -m "Short description of change"`
- Or add the sign-off to an existing commit:
  - `git commit --amend -s --no-edit`
- The sign-off line looks like:
  - `Signed-off-by: Your Name <your.email@example.com>`

**Why DCO**  
DCO helps keep contributor provenance clear and preserves the project’s ability to manage licensing and commercial options in the future.

---

## Commit Message Guidelines

- Use a short, imperative subject line (max 72 characters).
- Provide a body if needed to explain the reasoning.
- Include `Signed-off-by` either via `-s` or in the commit body.

**Example**
feat(parser): add CourseLeaf HTML parser
Add a parser for CourseLeaf catalogs with unit tests and sample data.
Signed-off-by: Jane Developer jane@example.com

---

## Pull Request Process

1. Push your branch to your fork and open a PR against `main`.
2. Link the PR to the issue (if applicable).
3. Ensure CI passes (tests, lint, DCO check).
4. A maintainer will review and request changes or merge.

---

## Code Style and Tests

- **Language**: Python for backend prototypes; follow PEP8.
- **Testing**: Add unit tests for new features. Tests live in `tests/`.
- **Formatting**: Use `black` for Python and `prettier` for frontend code.
- **Type hints**: Use Python type hints where appropriate.

---

## DCO Enforcement Workflow

We run an automated DCO check on PRs. If your commits are missing a sign-off, the check will fail and you will need to add the sign-off and push again.

**GitHub Action** (add to `.github/workflows/dco.yml`):

```yaml
name: DCO Check

on:
  pull_request:
    types: [opened, synchronize, reopened]

jobs:
  dco:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: DCO check
        uses: peter-evans/dco@v2
        with:
          # Fail the check if any commit is missing a sign-off
          require-signoff: true
