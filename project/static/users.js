let table_body = document.querySelector("#users");
let search = document.querySelector("#search");
let userCount = document.querySelector("#user-count");
search.addEventListener("keydown", async (event) => {
  if (event.key === "Enter") {
    const value = Number(search.value);

    if (!Number.isInteger(value)) {
      console.log("Enter a valid integer");
      return;
    }

    const response = await fetch("/api/users");
    const users = await response.json();

    const exists = users.some((user) => user.id === value);

    if (exists) {
      window.location.href = `/member/${value}`;
    } else {
      alert("Member ID does not exist");
    }
  }
});
async function loadUser() {
  const response = await fetch("/api/users");
  const users = await response.json();

  users.forEach((user, index) => {
    const row = document.createElement("tr");

    row.innerHTML = `
      <td>${index + 1}</td>
      <td class="member-id">${user.id}</td>
      <td class="member-name">${user.name}</td>
      <td class="member-email">${user.email}</td>
    `;

    row.addEventListener("click", () => {
      window.location.href = `/member/${user.id}`;
    });

    table_body.append(row);
    userCount.textContent = "" + (index + 1);
  });
}

loadUser();
