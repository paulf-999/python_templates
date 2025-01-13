# :pencil2: Pull Request Summary

[Summary of the change here.]

## :clipboard: (Optional) Additional Details

[If needed, provide further context or details.]

## :hammer_and_wrench: Type of PR Change

Choose one:

- [ ] **Feature**: A new feature or a change to an existing feature.
- [ ] **Trivial change**: A *minor* change with little/no impact.
- [ ] **Refactoring/housekeeping**: Restructuring existing code, or tidying up the git repo structure.
- [ ] **Bugfix**: A *minor* bug or issue.
- [ ] **Documentation**: Updates or adds documentation.

## :fire: Critical Changes

- [ ] **Release**: A major new code release.
- [ ] **Hotfix**: Addresses a critical bug fix.

---

## :snake: Python Standards Checklist

1. **Coding Standards:**

    Verify adherence to [Payroc's Python coding standards](https://payroc.atlassian.net/wiki/spaces/TEC/pages/2544467994/Python+-+Standard+-+Style+Guide+Coding+Standards), in particular:

   - [ ] Ensure adherence to PEP 8 guidelines.
   - [ ] Check for clear and meaningful variable/function names.
   - [ ] Verify consistent code formatting.

2. **Configuration:**
   - [ ] Ensure that the code is designed to be config-driven where appropriate.
   - [ ] Verify that configurable parameters are clearly defined and documented.
   - [ ] Check for separation of configuration from code logic.

3. **Error Handling:**
   - [ ] Check for proper implementation of error handling mechanisms.
   - [ ] Verify logging of errors for debugging and monitoring.
   - [ ] Ensure user-facing error messages are informative and helpful.

4. **Testing:**
   - [ ] Confirm the presence of unit tests for new/modified code.
   - [ ] Review test coverage for critical functionality.
   - [ ] Check for appropriate test assertions and coverage of edge cases.

5. **Documentation:**
   - [ ] Validate the presence of README updates, if applicable.
   - [ ] Ensure documentation of new dependencies or usage instructions.
   - [ ] Look for inline comments explaining complex logic or design decisions.

## :bulb: Best Practices

- Keep the PR as small as possible, dividing it into different PRs if possible
- Explain reasons behind changes that might not be obvious or seem complex
