var deleteModalLabel = document.getElementById('deleteModalLabel');
var deleteModalBody = document.getElementById('deleteModalBody');
var deleteConfirm = document.getElementById('deleteConfirm');


document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
})

function initializeEventListeners() {
    deleteTeam();
}

function deleteTeam(event) {
    deleteModalBody.innerHTML = `<p>Are you sure you want to delete this team?</p><p>This action cannot be undone.</p>`;
    deleteModalLabel.textContent = 'Delete Team?';
    event.target.blur();
};