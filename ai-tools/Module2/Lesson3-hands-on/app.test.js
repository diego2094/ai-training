/**
 * app.test.js
 * Archivo de pruebas con Jest + supertest.
 * Se ejemplifica:
 *  - Pruebas unitarias sobre userLogin
 *  - Pruebas de integración de un endpoint (GET /healthcheck)
 */

const request = require("supertest");
const { app, userLogin } = require("./app");

// PRUEBAS UNITARIAS PARA userLogin
describe("userLogin function", () => {
  test('returns "Login successful" for valid credentials', () => {
    const result = userLogin("alice", "secret");
    expect(result).toBe("Login successful");
  });

  test('returns "Invalid credentials" for wrong password', () => {
    const result = userLogin("alice", "wrong");
    expect(result).toBe("Invalid credentials");
  });

  test("throws an error if username or password is missing", () => {
    expect(() => userLogin("alice")).toThrow("Missing username or password");
  });
});

// PRUEBAS DE INTEGRACIÓN PARA /healthcheck
describe("GET /healthcheck", () => {
  test('should return status 200 and {status: "ok"}', async () => {
    const res = await request(app).get("/healthcheck");
    expect(res.status).toBe(200);
    expect(res.body).toEqual({ status: "ok" });
  });
});
