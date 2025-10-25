const roleSelect = document.getElementById("role");
const studentField = document.getElementById("studentField");
const instructorField = document.getElementById("instructorField");

roleSelect.addEventListener("change", function () {
  if (this.value === "student") {
    studentField.classList.remove("hidden");
    instructorField.classList.add("hidden");
  } else if (this.value === "instructor") {
    instructorField.classList.remove("hidden");
    studentField.classList.add("hidden");
  }
});