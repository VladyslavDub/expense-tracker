function openDelete(button) {
        document.getElementById('delete-form').action = button.dataset.url;
        document.getElementById('delete-dialog').showModal();
    }