const SESSION_KEY = "autoDb_currentUser";

let isRegisterMode = false;
let selectedFile = null;

const getCurrentUser = () => JSON.parse(sessionStorage.getItem(SESSION_KEY));
const setCurrentUser = (user) => {
  if (user) sessionStorage.setItem(SESSION_KEY, JSON.stringify(user));
  else sessionStorage.removeItem(SESSION_KEY);
};

function authHeaders(extra = {}) {
  const user = getCurrentUser();
  return user ? { ...extra, "x-user-id": String(user.id) } : extra;
}

function toggleAuthModal(show) {
  document.getElementById("auth-error").textContent = "";
  document.getElementById("auth-section").classList.toggle("hidden", !show);
}

function switchAuthMode() {
  isRegisterMode = !isRegisterMode;
  document.getElementById("auth-title").textContent = isRegisterMode
    ? "Regisztráció"
    : "Belépés";
  document.getElementById("toggle-auth-mode").textContent = isRegisterMode
    ? "Már van fiókom (Belépés)"
    : "Nincs még fiókom (Regisztráció)";
  document.getElementById("auth-error").textContent = "";
}

document.getElementById("auth-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const username = document.getElementById("username").value.trim();
  const password = document.getElementById("password").value.trim();
  const errorEl = document.getElementById("auth-error");
  errorEl.textContent = "";

  const endpoint = isRegisterMode ? "/api/register" : "/api/login";
  const res = await fetch(endpoint, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  });

  const data = await res.json();
  if (!res.ok) {
    errorEl.textContent = data.error || "Hiba történt.";
    return;
  }

  setCurrentUser(data.user);
  document.getElementById("auth-form").reset();
  toggleAuthModal(false);
  updateUI();
});

function logout() {
  setCurrentUser(null);
  resetCarForm();
  updateUI();
}

document.getElementById("car-image").addEventListener("change", function () {
  const file = this.files[0];
  const preview = document.getElementById("image-preview");
  selectedFile = file || null;

  if (!file) return;
  preview.src = URL.createObjectURL(file);
  preview.classList.remove("hidden");
});


document.getElementById("car-form").addEventListener("submit", async (e) => {
  e.preventDefault();
  const user = getCurrentUser();
  if (!user) return;

  const id = document.getElementById("car-id").value;
  const formData = new FormData();
  formData.append("brand", document.getElementById("car-brand").value.trim());
  formData.append("model", document.getElementById("car-model").value.trim());
  formData.append("year", document.getElementById("car-year").value);
  formData.append("price", document.getElementById("car-price").value);
  formData.append(
    "description",
    document.getElementById("car-desc").value.trim(),
  );
  formData.append(
    "isPublic",
    String(document.getElementById("car-public").checked),
  );
  if (selectedFile) {
    formData.append("image", selectedFile);
  }

  const url = id ? `/api/cars/${id}` : "/api/cars";
  const method = id ? "PUT" : "POST";

  const res = await fetch(url, {
    method,
    headers: authHeaders(),
    body: formData,
  });

  if (res.ok) {
    resetCarForm();
    renderCars();
  } else {
    const err = await res.json();
    alert(err.error || "Mentési hiba.");
  }
});

async function editCar(carId) {
  const res = await fetch("/api/cars", { headers: authHeaders() });
  const cars = await res.json();
  const car = cars.find((c) => c.id === carId);
  if (!car) return;

  document.getElementById("car-id").value = car.id;
  document.getElementById("car-brand").value = car.brand;
  document.getElementById("car-model").value = car.model;
  document.getElementById("car-year").value = car.year;
  document.getElementById("car-price").value = car.price;
  document.getElementById("car-desc").value = car.description;
  document.getElementById("car-public").checked = car.isPublic;
  selectedFile = null;

  const preview = document.getElementById("image-preview");
  preview.src = car.image;
  preview.classList.remove("hidden");

  document.getElementById("form-title").textContent =
    "Autó adatainak módosítása";
  document.getElementById("btn-cancel-edit").classList.remove("hidden");
  window.scrollTo({ top: 0, behavior: "smooth" });
}

async function deleteCar(carId) {
  const res = await fetch(`/api/cars/${carId}`, {
    method: "DELETE",
    headers: authHeaders(),
  });
  if (res.ok) {
    renderCars();
  } else {
    const err = await res.json();
    alert(err.error || "Törlési hiba.");
  }
}

function resetCarForm() {
  document.getElementById("car-form").reset();
  document.getElementById("car-id").value = "";
  selectedFile = null;
  document.getElementById("image-preview").classList.add("hidden");
  document.getElementById("form-title").textContent = "Új autó hozzáadása";
  document.getElementById("btn-cancel-edit").classList.add("hidden");
}


function updateUI() {
  const user = getCurrentUser();
  const userLabel = document.getElementById("current-user-label");
  const btnLogin = document.getElementById("btn-show-login");
  const btnLogout = document.getElementById("btn-logout");
  const carFormSection = document.getElementById("car-form-section");
  const filterControls = document.getElementById("filter-controls");
  const listHeading = document.getElementById("list-heading");

  if (user) {
    userLabel.textContent = `Belépve: ${user.username}`;
    btnLogin.classList.add("hidden");
    btnLogout.classList.remove("hidden");
    carFormSection.classList.remove("hidden");
    filterControls.classList.remove("hidden");
    listHeading.textContent = "Elérhető autók (Publikus + Saját privát)";
  } else {
    userLabel.textContent = "Vendég (nincs belépve)";
    btnLogin.classList.remove("hidden");
    btnLogout.classList.add("hidden");
    carFormSection.classList.add("hidden");
    filterControls.classList.add("hidden");
    document.getElementById("only-my-cars").checked = false;
    listHeading.textContent = "Publikus autók";
  }

  renderCars();
}

async function renderCars() {
  const container = document.getElementById("cars-container");
  const user = getCurrentUser();
  const onlyMine = document.getElementById("only-my-cars").checked;

  const query = onlyMine ? "?onlyMine=true" : "";
  const res = await fetch(`/api/cars${query}`, { headers: authHeaders() });
  const cars = await res.json();

  if (!cars.length) {
    container.innerHTML = "<p>Nincs megjeleníthető autó.</p>";
    return;
  }

  container.innerHTML = cars
    .map((car) => {
      const isOwner = user && car.owner_id === user.id;
      return `
            <article class="car-card">
                <img src="${car.image}" alt="${car.brand} ${car.model}">
                <div class="car-body">
                    <div>
                        <span class="badge ${car.isPublic ? "public" : "private"}">
                            ${car.isPublic ? "Publikus" : "Privát"}
                        </span>
                        <h3 class="car-title">${car.brand} ${car.model} (${car.year})</h3>
                        <div class="car-meta">Feltöltő: <strong>${car.owner_name}</strong></div>
                        <p>${car.description}</p>
                    </div>
                    <div>
                        <div class="car-price">${Number(car.price).toLocaleString("hu-HU")} Ft</div>
                        ${
                          isOwner
                            ? `<div class="btn-group">
                                    <button onclick="editCar(${car.id})">Módosítás</button>
                                    <button class="danger" onclick="deleteCar(${car.id})">Törlés</button>
                                   </div>`
                            : ""
                        }
                    </div>
                </div>
            </article>
        `;
    })
    .join("");
}

updateUI();
