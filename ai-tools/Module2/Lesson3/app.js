/**
 * app.js
 *
 * Microservicio base con algunos endpoints para ilustrar:
 * 1. /users (ejemplo existente)
 * 2. /reports (Task #1)
 * 3. Refactor user auth (Task #2, con JWT hipotético)
 * 4. (Opcional) DB optimization (Task #3) usando un array simulando queries
 */

const express = require("express");
const app = express();

app.use(express.json());

// Datos simulados
let users = [
  { id: 1, name: "Alice", age: 30 },
  { id: 2, name: "Bob", age: 25 },
  { id: 3, name: "Charlie", age: 35 },
];

// Endpoint existente: GET /users
app.get("/users", (req, res) => {
  res.status(200).json(users);
});

/**
 * Task #1: /reports endpoint
 * Retorna estadísticas simples de los usuarios
 * Ejemplo: { totalUsers: 3, averageAge: 30 }
 */
app.get("/reports", (req, res) => {
  const totalUsers = users.length;
  const avgAge = users.reduce((sum, u) => sum + u.age, 0) / (users.length || 1);

  res.json({
    totalUsers,
    averageAge: parseFloat(avgAge.toFixed(2)),
  });
});

/**
 * Task #2: (Simulado) Refactor user auth
 * Podrías incluir un middleware con JWT
 * Aquí sólo mostramos un campo "isAuthenticated" a modo de demostración
 */
app.post("/login", (req, res) => {
  const { username, password } = req.body;
  // Lógica básica (placeholder) - en realidad usarías bcrypt + jwt
  if (username === "admin" && password === "admin123") {
    return res.status(200).json({
      message: "Login successful",
      isAuthenticated: true,
    });
  }
  return res.status(401).json({
    message: "Invalid credentials",
    isAuthenticated: false,
  });
});

/**
 * Task #3: (Opcional) "Optimize DB Queries"
 * Aquí fingimos tener un endpoint que filtra usuarios según edad mínima
 * Podrías 'optimizarlo' con índice o métodos de búsqueda
 */
app.get("/users/filter/:minAge", (req, res) => {
  const minAge = parseInt(req.params.minAge, 10);
  const filtered = users.filter((u) => u.age >= minAge);
  res.json(filtered);
});

// Export y server
module.exports = { app, users };

if (require.main === module) {
  const PORT = process.env.PORT || 3000;
  app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
  });
}
