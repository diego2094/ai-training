/**
 * app.js
 *
 * Basado en prompt_instructions.md, este archivo ilustra:
 * - Servidor Express
 * - Endpoints /users (GET, POST)
 * - Documentación Swagger via JSDoc y swagger-jsdoc
 * - Autenticación JWT básica
 */

// Importaciones
const express = require("express");
const swaggerUi = require("swagger-ui-express");
const swaggerJsdoc = require("swagger-jsdoc");
const jwt = require("jsonwebtoken");

const app = express();
app.use(express.json());

// -----------------------------------------------------------------------------
// 1) CONFIGURACIÓN DE SWAGGER
// -----------------------------------------------------------------------------
const options = {
  definition: {
    openapi: "3.0.0",
    info: {
      title: "Microservice Demo",
      version: "1.0.0",
      description: "API Documentation for our minimal Node.js microservice",
    },
  },
  // Podrías usar un archivo separado, pero aquí se lee el propio app.js
  apis: ["./app.js"],
};
const swaggerSpec = swaggerJsdoc(options);

// Montamos la ruta para la documentación
app.use("/api-docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));

// -----------------------------------------------------------------------------
// 2) DATOS DE EJEMPLO E INFORMACIÓN DE AUTENTICACIÓN
// -----------------------------------------------------------------------------
const SECRET_KEY = "MY_SUPER_SECRET"; // En producción, usar process.env.SECRET_KEY
let users = [{ id: 1, name: "Alice" }];

// -----------------------------------------------------------------------------
// 3) MIDDLEWARE DE AUTENTICACIÓN JWT
// -----------------------------------------------------------------------------
function authMiddleware(req, res, next) {
  const authHeader = req.headers["authorization"];
  if (!authHeader) {
    return res.status(401).json({ error: "No token provided" });
  }
  const token = authHeader.split(" ")[1]; // Asume "Bearer <token>"
  try {
    const decoded = jwt.verify(token, SECRET_KEY);
    req.user = decoded;
    next();
  } catch (err) {
    return res.status(401).json({ error: "Invalid token" });
  }
}

// -----------------------------------------------------------------------------
// 4) ENDPOINTS
// -----------------------------------------------------------------------------

/**
 * @openapi
 * /users:
 *   get:
 *     summary: Retrieve a list of users
 *     responses:
 *       200:
 *         description: A JSON array of users
 */
app.get("/users", (req, res) => {
  res.json(users);
});

/**
 * @openapi
 * /users:
 *   post:
 *     summary: Create a new user (requires JWT auth)
 *     responses:
 *       201:
 *         description: User created
 *       401:
 *         description: Unauthorized
 */
app.post("/users", authMiddleware, (req, res) => {
  const { name } = req.body;
  if (!name) {
    return res.status(400).json({ error: "Name is required" });
  }
  const newUser = { id: users.length + 1, name };
  users.push(newUser);
  return res.status(201).json(newUser);
});

// -----------------------------------------------------------------------------
// 5) PUERTO E INICIO DEL SERVIDOR
// -----------------------------------------------------------------------------
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
  console.log(`Swagger docs: http://localhost:${PORT}/api-docs`);
});
