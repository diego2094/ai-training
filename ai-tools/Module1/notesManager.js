// notesManager.js
// ========================================================================
// EJEMPLO DE PROYECTO PARA LECCIÓN 1 (Assignment): "AI Tools for Faster Coding"
// ========================================================================
//
// Instrucciones:
// 1. En este archivo se implementan varias funciones de ejemplo para manejar
//    'notas' en un array. Luego, se puede agregar una nueva funcionalidad
//    (p.ej. buscar notas) usando un segundo asistente de código (Tabnine, Cursor, etc.).
//
// 2. Tu tarea será observar cuántas líneas el asistente escribe
//    vs. cuántas ajustas manualmente.
//
// ========================================================================

// Array de notas de ejemplo (puede partir vacío o con datos precargados).
let notes = [
  { id: 1, text: "Estudiar JavaScript", tags: ["study", "js"] },
  { id: 2, text: "Hacer la compra", tags: ["home"] },
  { id: 3, text: "Revisar proyecto AI Tools", tags: ["work", "ai"] },
];

// Función para listar todas las notas
function listNotes() {
  return notes;
}

// Función para añadir una nueva nota
function addNote(text, tags = []) {
  const newId = notes.length > 0 ? notes[notes.length - 1].id + 1 : 1;
  const newNote = { id: newId, text, tags };
  notes.push(newNote);
  return newNote;
}

// Función para editar el texto de una nota (búsqueda por ID)
function updateNote(id, newText) {
  const noteIndex = notes.findIndex((n) => n.id === id);
  if (noteIndex === -1) {
    return null; // No se encontró la nota
  }
  notes[noteIndex].text = newText;
  return notes[noteIndex];
}

// TODO: Implementar una nueva función "searchNotes(keyword)" con un
// segundo asistente de código (p.ej. Tabnine, Cursor). Se sugiere que
// busque coincidencias en 'text' y devuelva un array con las notas que
// incluyan el 'keyword' (ignorando mayúsculas/minúsculas).
//
// function searchNotes(keyword) {
//   ...
// }

// Exportar las funciones para usarlas en otro archivo o para test
module.exports = {
  listNotes,
  addNote,
  updateNote,
  // searchNotes,
};
