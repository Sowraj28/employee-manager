let currentPage = 0;
let searchResults = [];

function renderEmployeePage() {
  const modalBody = document.getElementById("searchResultContent");

  if (searchResults.length === 0) {
    modalBody.innerHTML = `<p style="color:red;">No employee found.</p>`;
    return;
  }

  const emp = searchResults[currentPage];
  modalBody.innerHTML = `
    <div style="padding: 10px;">
      <p><strong>ID:</strong> ${emp.employee_id}</p>
      <p><strong>Name:</strong> ${emp.employee_name}</p>
      <p><strong>Email:</strong> ${emp.employee_email}</p>
      <p><strong>Contact:</strong> ${emp.employee_contact}</p>
      <div class="d-flex justify-content-between mt-3">
        <button class="btn btn-secondary btn-sm" onclick="prevPage()" ${
          currentPage === 0 ? "disabled" : ""
        }>Previous</button>
        <span class="text-white">Result ${currentPage + 1} of ${
    searchResults.length
  }</span>
        <button class="btn btn-secondary btn-sm" onclick="nextPage()" ${
          currentPage === searchResults.length - 1 ? "disabled" : ""
        }>Next</button>
      </div>
    </div>
  `;
}

function nextPage() {
  if (currentPage < searchResults.length - 1) {
    currentPage++;
    renderEmployeePage();
  }
}

function prevPage() {
  if (currentPage > 0) {
    currentPage--;
    renderEmployeePage();
  }
}

function searchEmployee() {
  const query = document
    .getElementById("searchInput")
    .value.trim()
    .toLowerCase();
  if (!query) return;

  fetch("/search-employee/?q=" + encodeURIComponent(query))
    .then((res) => res.json())
    .then((data) => {
      if (data.success && data.employees.length > 0) {
        searchResults = data.employees;
        currentPage = 0;
        renderEmployeePage();
      } else {
        document.getElementById(
          "searchResultContent"
        ).innerHTML = `<p style="color:red;">${data.message}</p>`;
      }
      new bootstrap.Modal(document.getElementById("searchModal")).show();

      // Clear search input after showing results
      document.getElementById("searchInput").value = "";
    });
}
