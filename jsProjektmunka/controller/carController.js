const { getAuthenticatedUser } = require("./authController");

function getCars(req, res, db) {
  const user = getAuthenticatedUser(req, db);
  const onlyMine = req.query.onlyMine === "true";

  let rows;
  if (!user) {
    rows = db
      .prepare(
        `
                SELECT c.*, u.username AS owner_name
                FROM cars c
                JOIN users u ON c.owner_id = u.id
                WHERE c.is_public = 1
                ORDER BY c.id DESC
            `,
      )
      .all();
  } else if (onlyMine) {
    rows = db
      .prepare(
        `
                SELECT c.*, u.username AS owner_name
                FROM cars c
                JOIN users u ON c.owner_id = u.id
                WHERE c.owner_id = ?
                ORDER BY c.id DESC
            `,
      )
      .all(user.id);
  } else {
    rows = db
      .prepare(
        `
                SELECT c.*, u.username AS owner_name
                FROM cars c
                JOIN users u ON c.owner_id = u.id
                WHERE c.is_public = 1 OR c.owner_id = ?
                ORDER BY c.id DESC
            `,
      )
      .all(user.id);
  }

  res.json(rows.map((r) => ({ ...r, isPublic: Boolean(r.is_public) })));
}

function createCar(req, res, db) {
  const user = getAuthenticatedUser(req, db);
  if (!user) {
    return res.status(401).json({ error: "Csak belépve adhatsz hozzá autót." });
  }

  const { brand, model, year, price, description, isPublic } = req.body;
  const imageUrl = req.file
    ? `/uploads/${req.file.filename}`
    : "https://via.placeholder.com/400x250?text=Nincs+kep";

  const result = db
    .prepare(
      `
            INSERT INTO cars (owner_id, brand, model, year, price, description, image, is_public)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        `,
    )
    .run(
      user.id,
      brand.trim(),
      model.trim(),
      Number(year),
      Number(price),
      description.trim(),
      imageUrl,
      isPublic === "true" || isPublic === true ? 1 : 0,
    );

  const created = db
    .prepare(
      `
            SELECT c.*, u.username AS owner_name
            FROM cars c
            JOIN users u ON c.owner_id = u.id
            WHERE c.id = ?
        `,
    )
    .get(result.lastInsertRowid);

  res.status(201).json({ ...created, isPublic: Boolean(created.is_public) });
}

function updateCar(req, res, db) {
  const user = getAuthenticatedUser(req, db);
  if (!user) {
    return res.status(401).json({ error: "Nincs jogosultság." });
  }

  const carId = Number(req.params.id);
  const existing = db.prepare("SELECT * FROM cars WHERE id = ?").get(carId);
  if (!existing) {
    return res.status(404).json({ error: "Az autó nem található." });
  }
  if (existing.owner_id !== user.id) {
    return res
      .status(403)
      .json({ error: "Más felhasználó autóját nem módosíthatod!" });
  }

  const { brand, model, year, price, description, isPublic } = req.body;
  const nextImage = req.file ? `/uploads/${req.file.filename}` : existing.image;

  db.prepare(
    `
        UPDATE cars
        SET brand = ?, model = ?, year = ?, price = ?, description = ?, image = ?, is_public = ?
        WHERE id = ?
    `,
  ).run(
    brand.trim(),
    model.trim(),
    Number(year),
    Number(price),
    description.trim(),
    nextImage,
    isPublic === "true" || isPublic === true ? 1 : 0,
    carId,
  );

  const updated = db
    .prepare(
      `
            SELECT c.*, u.username AS owner_name
            FROM cars c
            JOIN users u ON c.owner_id = u.id
            WHERE c.id = ?
        `,
    )
    .get(carId);

  res.json({ ...updated, isPublic: Boolean(updated.is_public) });
}

function deleteCar(req, res, db) {
  const user = getAuthenticatedUser(req, db);
  if (!user) {
    return res.status(401).json({ error: "Nincs jogosultság." });
  }

  const carId = Number(req.params.id);
  const existing = db.prepare("SELECT * FROM cars WHERE id = ?").get(carId);
  if (!existing) {
    return res.status(404).json({ error: "Az autó nem található." });
  }
  if (existing.owner_id !== user.id) {
    return res
      .status(403)
      .json({ error: "Más felhasználó autóját nem törölheted!" });
  }

  db.prepare("DELETE FROM cars WHERE id = ?").run(carId);
  res.json({ success: true });
}

module.exports = {
  getCars,
  createCar,
  updateCar,
  deleteCar,
};
