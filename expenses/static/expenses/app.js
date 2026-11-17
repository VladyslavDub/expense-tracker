function openDelete(button) {
        document.getElementById('delete-form').action = button.dataset.url;
        document.getElementById('delete-dialog').showModal();
    }

function openEdit(button) {
    const form = document.getElementById('edit-form');
    form.action = button.dataset.url;
    form.elements['title'].value = button.dataset.title;
    form.elements['description'].value = button.dataset.description;
    form.elements['amount'].value = button.dataset.amount;
    form.elements['category'].value = button.dataset.category;
    form.elements['date_of_expenditure'].value = button.dataset.date_of_expenditure;
    document.getElementById('edit-dialog').showModal();
}