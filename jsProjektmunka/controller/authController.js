function register(req, res, db) {
  const { username, password } = req.body;
  if (!username || !password) {
    return res
      .status(400)
      .json({ error: "Felhasználónév és jelszó megadása kötelező." });
  }

  try {
    const result = db
      .prepare("INSERT INTO users (username, password) VALUES (?, ?)")
      .run(username.trim(), password.trim());
    const user = db
      .prepare("SELECT id, username FROM users WHERE id = ?")
      .get(result.lastInsertRowid);
    res.status(201).json({ user });
  } catch (err) {
    if (err.code === "SQLITE_CONSTRAINT_UNIQUE") {
      return res
        .status(409)
        .json({ error: "Ez a felhasználónév már foglalt." });
    }
    res.status(500).json({ error: "Adatbázis hiba a regisztráció során." });
  }
}

function login(req, res, db) {
  const { username, password } = req.body;
  const user = db
    .prepare(
      "SELECT id, username FROM users WHERE username = ? AND password = ?",
    )
    .get(username?.trim(), password?.trim());

  if (!user) {
    return res.status(401).json({ error: "Hibás felhasználónév vagy jelszó." });
  }

  res.json({ user });
}

function getAuthenticatedUser(req, db) {
  const userId = Number(req.header("x-user-id"));
  if (!userId) return null;
  return (
    db.prepare("SELECT id, username FROM users WHERE id = ?").get(userId) ||
    null
  );
}

module.exports = {
  register,
  login,
  getAuthenticatedUser,
};
