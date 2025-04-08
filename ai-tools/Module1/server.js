// server.js

// Servidor básico para probar las rutas de usuario

const express = require("express");
const app = express();
const userRoutes = require("./userRoutes");

// Middleware para parsear JSON
app.use(express.json());

// Montamos las rutas en /api
app.use("/api", userRoutes);

// Iniciamos servidor en puerto 3000
app.listen(3000, () => {
  console.log("Server running on http://localhost:3000");
});
