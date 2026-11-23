const express = require("express");
const Database = require("better-sqlite3");
const multer = require("multer");
const path = require("path");
const fs = require("fs");

const authController = require("./controller/authController");
const carController = require("./controller/carController");

const app = express();
const PORT = 3000;

const dbDir = path.join(__dirname, "database");
const uploadsDir = path.join(__dirname, "uploads");
if (!fs.existsSync(dbDir)) fs.mkdirSync(dbDir);
if (!fs.existsSync(uploadsDir)) fs.mkdirSync(uploadsDir);

app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));
app.use("/uploads", express.static(uploadsDir));

const storage = multer.diskStorage({
  destination: (req, file, cb) => cb(null, uploadsDir),
  filename: (req, file, cb) => {
    const ext = path.extname(file.originalname).toLowerCase();
    cb(null, `car_${Date.now()}_${Math.round(Math.random() * 1e6)}${ext}`);
  },
});
const upload = multer({
  storage,
  fileFilter: (req, file, cb) => {
    if (file.mimetype.startsWith("image/")) cb(null, true);
    else cb(new Error("Csak képfájl tölthető fel!"));
  },
});

const db = new Database(path.join(dbDir, "cars.db"));

db.exec(`
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        owner_id INTEGER NOT NULL,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        year INTEGER NOT NULL,
        price INTEGER NOT NULL,
        description TEXT NOT NULL,
        image TEXT,
        is_public INTEGER NOT NULL DEFAULT 1,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE CASCADE
    );
`);

const userCount = db.prepare("SELECT COUNT(*) AS count FROM users").get().count;
if (userCount === 0) {
  const insertUser = db.prepare(
    "INSERT INTO users (username, password) VALUES (?, ?)",
  );
  const admin = insertUser.run("admin", "123");
  const bela = insertUser.run("bela", "123");

  const insertCar = db.prepare(`
        INSERT INTO cars (owner_id, brand, model, year, price, description, image, is_public)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    `);

  insertCar.run(
    admin.lastInsertRowid,
    "Audi",
    "RS6 Avant",
    2022,
    42000000,
    "V8 biturbó, megkímélt állapotban, végig vezetett szervizkönyvvel.",
    "https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?auto=format&fit=crop&w=800&q=80",
    1,
  );
  insertCar.run(
    bela.lastInsertRowid,
    "Toyota",
    "Supra GR",
    2021,
    21500000,
    "Sportkipufogóval, garázsban tartott hétvégi autó.",
    "https://images.unsplash.com/photo-1626668893632-6f3a4466d22f?auto=format&fit=crop&w=800&q=80",
    1,
  );
  insertCar.run(
    admin.lastInsertRowid,
    "Porsche",
    "911 GT3",
    2023,
    85000000,
    "Privát gyűjtemény darabja – csak belépés után látható.",
    "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=800&q=80",
    0,
  );
}

app.post("/api/register", (req, res) => authController.register(req, res, db));
app.post("/api/login", (req, res) => authController.login(req, res, db));

app.get("/api/cars", (req, res) => carController.getCars(req, res, db));
app.post("/api/cars", upload.single("image"), (req, res) =>
  carController.createCar(req, res, db),
);
app.put("/api/cars/:id", upload.single("image"), (req, res) =>
  carController.updateCar(req, res, db),
);
app.delete("/api/cars/:id", (req, res) =>
  carController.deleteCar(req, res, db),
);

app.listen(PORT, () => {
  console.log(`Szerver fut: http://localhost:${PORT}`);
});
