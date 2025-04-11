# PROMPT LOG

## Prompt #1: Generate Unit Tests

**Exact Wording**:
"Generate Jest unit tests for the 'createUser' function, covering edge cases like missing fields or invalid email."

**AI Output**:

```js
// createUser.test.js
const { createUser } = require("../app");
describe("createUser", () => {
  test("should create a user with valid data", () => {
    // ...
  });
  test("should fail if missing fields", () => {
    // ...
  });
});
```
