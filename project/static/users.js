let table_body = document.querySelector("#users");

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
  });
}

loadUser();
