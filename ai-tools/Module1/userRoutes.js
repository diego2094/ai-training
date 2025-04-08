// userRoutes.js

// Ejemplo de implementación de rutas de usuario según la especificación
// en user_management_spec.md

const express = require("express");
const router = express.Router();

// Array para almacenar temporalmente la lista de usuarios (prototipo).
const users = [];

/**
 * POST /api/users
 * Crea un nuevo usuario según la especificación:
 * - 201 Created si todo va bien
 * - 400 Bad Request si falta algún campo
 */
router.post("/users", (req, res) => {
  const { username, email, password, role } = req.body;

  // Verificar campos requeridos
  if (!username || !email || !password) {
    return res.status(400).json({ error: "Bad request: missing fields" });
  }

  // Crear objeto usuario
  const newUser = {
    id: users.length + 1,
    username,
    email,
    password,
    role: role || "basic", // Ejemplo “vibe coding”: si no llega role, asignamos 'basic'
  };

  // Guardar en el array
  users.push(newUser);

  // Devolver respuesta 201 con el nuevo usuario
  return res.status(201).json({
    message: "User created successfully",
    user: newUser,
  });
});

// Aquí podrías “vibear” (vibe coding) añadiendo endpoints adicionales,
// tal como GET /api/users, DELETE /api/users/:id, etc.

// Exportar router para usarlo en server.js
module.exports = router;
