// app.js (o server.js)

// EJEMPLO DE PROYECTO PARA LECCIÓN 2: "Documentation-First y Vibe Coding"

// 1. Requerimos Express
const express = require("express");
const app = express();
app.use(express.json());

// DATOS SIMPLES EN MEMORIA (en vez de DB) - ¡Solo para demostrar!
const users = [
  { id: 1, name: "Alice", email: "alice@example.com" },
  { id: 2, name: "Bob", email: "bob@example.com" },
  { id: 3, name: "Charlie", email: "charlie@example.com" },
];

// ==================================================================================
// ENDPOINT A: GET /api/users (DOCUMENTATION-FIRST)
// ==================================================================================
//
// Según ENDPOINT_A_SPEC.md, necesitamos:
// - Query params: page (opcional, default=1), limit (opcional, default=10)
// - Respuesta: array JSON de usuarios paginados + totalCount
// ==================================================================================

app.get("/api/users", (req, res) => {
  // Convertir query params a números y usar valores por defecto
  const page = parseInt(req.query.page) || 1;
  const limit = parseInt(req.query.limit) || 10;

  // Calcular índices de paginación
  const startIndex = (page - 1) * limit;
  const endIndex = startIndex + limit;

  // Extraer la parte correspondiente de la lista de 'users'
  const pagedUsers = users.slice(startIndex, endIndex);

  // Estructurar respuesta
  const response = {
    users: pagedUsers,
    totalCount: users.length,
    currentPage: page,
    limit: limit,
  };

  // Responder con status 200 y la data en formato JSON
  return res.status(200).json(response);
});

// ==================================================================================
// ENDPOINT B: POST /api/users (VIBE CODING)
// ==================================================================================
//
// Sin doc previa, solo con ideas espontáneas. "Chateamos" con la IA en comentarios.
//
// Ejemplo de "vibe coding" approach:
// - Creamos un nuevo usuario con name/email que llega en el body
// - Agregamos validaciones ad-hoc según lo que se nos ocurra
// - Retornamos 201 Created si todo va bien
// - Si no, tal vez 400 Bad Request
// ==================================================================================

app.post("/api/users", (req, res) => {
  // Vibe coding: "Necesito un name y un email"
  const { name, email } = req.body;

  // Validaciones rápidas
  if (!name || !email) {
    // "Vibing" sobre la idea de lanzar un error 400:
    return res.status(400).json({ error: "Name and email are required." });
  }

  // "Siento" que el ID debe ser automático, así que lo calculamos
  const newId = users.length > 0 ? users[users.length - 1].id + 1 : 1;

  const newUser = { id: newId, name, email };
  users.push(newUser);

  // Devolvemos 201 con el usuario creado
  return res.status(201).json({
    message: "User created successfully.",
    user: newUser,
  });
});

// Levantar el servidor
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server listening on http://localhost:${PORT}`);
});
