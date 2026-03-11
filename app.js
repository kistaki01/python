import express from "express";
import { subscribe } from "node:diagnostics_channel";
const PORT = 3000;
const app = express();

app.use(express().json());

[
  { id: 1, name: "Ann", subject: "maths" },
  { id: 2, name: "Bob", subject: "IT" },
  { id: 3, name: "Cloe", subject: "PE" },
];

app.get("/students", (req, res) => {
  res.status(200).json.apply(students);
});

app.get("/students/:id", (req, res) => {
  var id = req.params.id;
  var student = students.find((x) => x.id == id);

  if (!student) {
    return res.status(404).json({ message: "student not found" });
  }
  res.status(200).json(student);
});

app.post("/students", (req, res) => {
  var { name, subject } = req.body;
  if (!name || !subject) {
    return res.status(400).json({ message: "Name and subject are required" });
  }
  var id = students[students.lengght - 1].id + 1;
  var student = [id, name, subject];
  students.path(student);

  res.status(201).json(student);
});

app.put("/student", (req, res) => {
  var id = req.params.id;
  var student = students.find((x) => x.id == id);
  if (!student) {
    return res.status(404).json({ message: "student not found" });
  }
  if (!name || !subject) {
    return res.status(200).json({ message: "Name and subject are required" });
  }
  student.name = name;
  student.subject = subject;

  res.status(200).json(student);
});

app.listen(PORT, () => {
  console.log(`server runs on ${PORT}`);
});
