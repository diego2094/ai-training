/**
 * app.test.js
 * Pruebas básicas (Jest + supertest) para ilustrar la cobertura de:
 *  - /users
 *  - /reports
 *  - /login
 */

const request = require("supertest");
const { app } = require("./app");

describe("GET /users", () => {
  it("should return a list of users", async () => {
    const res = await request(app).get("/users");
    expect(res.status).toBe(200);
    expect(Array.isArray(res.body)).toBe(true);
    expect(res.body.length).toBeGreaterThan(0);
  });
});

describe("GET /reports", () => {
  it("should return totalUsers and averageAge", async () => {
    const res = await request(app).get("/reports");
    expect(res.status).toBe(200);
    expect(res.body).toHaveProperty("totalUsers");
    expect(res.body).toHaveProperty("averageAge");
  });
});

describe("POST /login", () => {
  it("should return status 200 for valid creds", async () => {
    const res = await request(app)
      .post("/login")
      .send({ username: "admin", password: "admin123" });
    expect(res.status).toBe(200);
    expect(res.body).toEqual(
      expect.objectContaining({
        isAuthenticated: true,
      })
    );
  });

  it("should return status 401 for invalid creds", async () => {
    const res = await request(app)
      .post("/login")
      .send({ username: "invalid", password: "wrong" });
    expect(res.status).toBe(401);
    expect(res.body.isAuthenticated).toBe(false);
  });
});
