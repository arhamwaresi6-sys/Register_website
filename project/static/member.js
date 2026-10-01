let dltBtn = document.querySelector("#delete-btn");
let editBtn = document.querySelector("#edit-btn");
let submitBtn = document.querySelector("#submitBtn");
let modalMessage = document.querySelector(".confirm-text");
let modal = document.querySelector(".delete-modal");
let route = "/";

dltBtn.addEventListener("click", async () => {
  route = "/delete";
  document.getElementById("deleteModal").classList.add("show");
});
editBtn.addEventListener("click", async () => {
  route = "/edit_check";
  document.getElementById("deleteModal").classList.add("show");
});
function closeDeleteModal() {
  document.getElementById("deleteModal").classList.remove("show");
}
submitBtn.addEventListener("click", async () => {
  let password = document.querySelector("#pass").value;
  let member_id = Number(document.querySelector("#pass").dataset.id);
  const response = await fetch(route, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      password: password,
      id: member_id,
    }),
  });
  if (response.ok) {
    let data = await response.json();
    if (data.message === "Nope") {
      if (data.message === "Nope") {
        modalMessage.textContent = "Password is wrong.";
        modalMessage.classList.add("active");
      }
    }

    if (data.message === "Done") {
      modal.innerHTML = `
        <div class="result-box">
            <div class="success-icon">✓</div>
            <h2>Done</h2>
            <p>Member deleted successfully.</p>
        </div>
    `;

      if (data.from == "delete") {
        setTimeout(() => {
          window.location.href = "/users";
        }, 1200);
      } else if (data.from == "edit_check") {
        setTimeout(() => {
          window.location.href = `/edit_member/${member_id}`;
        }, 1200);
      }
    }
  }
});
const form = document.querySelector("#deleteForm");

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  let password = document.querySelector("#pass").value;
  let member_id = Number(document.querySelector("#pass").dataset.id);

  const response = await fetch(route, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      password: password,
      id: member_id,
    }),
  });

  const data = await response.json();

  if (data.message === "Nope") {
    modalMessage.textContent = "Wrong password.";
    modalMessage.classList.add("active");
  }

  if (data.message === "Done") {
    modal.innerHTML = `
        <div class="result-box">
            <div class="success-icon">✓</div>
            <h2>Done</h2>
            <p>Member deleted successfully.</p>
        </div>
    `;
    if (data.from == "delete") {
      setTimeout(() => {
        window.location.href = "/users";
      }, 1200);
    } else if (data.from == "edit_check") {
      setTimeout(() => {
        window.location.href = `/edit_member/${member_id}`;
      }, 1200);
    }
  }
});
