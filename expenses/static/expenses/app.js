const searchForm = document.querySelector('.search');
const searchInput = searchForm.querySelector('input[name="q"]');
let searchTimer;

searchInput.addEventListener('input', () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(runSearch, 300);
});

async function runSearch() {
    const params = new URLSearchParams(new FormData(searchForm));
    const url = `${window.location.pathname}?${params}`;

    const response = await fetch(url);
    const html = await response.text();
    const page = new DOMParser().parseFromString(html, 'text/html');

    document.getElementById('results').innerHTML =
        page.getElementById('results').innerHTML;
    history.replaceState(null, '', url);
}

function openDelete(button) {
  document.getElementById("delete-form").action = button.dataset.url;
  document.getElementById("delete-dialog").showModal();
}

function openEdit(button) {
  const form = document.getElementById("edit-form");
  form.action = button.dataset.url;
  form.elements["title"].value = button.dataset.title;
  form.elements["description"].value = button.dataset.description;
  form.elements["amount"].value = button.dataset.amount;
  form.elements["category"].value = button.dataset.category;
  form.elements["date_of_expenditure"].value =
    button.dataset.date_of_expenditure;
  document.getElementById("edit-dialog").showModal();
}
