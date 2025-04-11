/**
 * app.js
 * Microservicio mínimo de Node.js con Express.
 * Se incluye una función userLogin para ejemplificar pruebas unitarias.
 */

const express = require("express");
const app = express();

app.use(express.json());

// Datos simulados (en un entorno real usarías DB)
const VALID_USERNAME = "alice";
const VALID_PASSWORD = "secret";

/**
 * userLogin
 * - Devuelve "Login successful" si las credenciales coinciden con las válidas
 * - De lo contrario, "Invalid credentials"
 * - Lanza error si faltan campos
 */
function userLogin(username, password) {
  if (!username || !password) {
    throw new Error("Missing username or password");
  }
  if (username === VALID_USERNAME && password === VALID_PASSWORD) {
    return "Login successful";
  }
  return "Invalid credentials";
}

// Endpoint GET /healthcheck para integración
app.get("/healthcheck", (req, res) => {
  res.status(200).json({ status: "ok" });
});

// Exportamos la función y la app para pruebas
module.exports = {
  app,
  userLogin,
};

// Iniciamos el servidor si se llama directamente, no en test
if (require.main === module) {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}
