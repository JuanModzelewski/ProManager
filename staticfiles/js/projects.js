const deleteTeamBtn = document.querySelectorAll('.delete-team-btn');
const deleteProjectBtn = document.querySelectorAll('.delete-project-btn');


document.addEventListener("DOMContentLoaded", function() {

    initEventListeners();

});

function initEventListeners() {

    for (let button of deleteTeamBtn) {
        button.addEventListener('click', (e) => {
            const deleteTeamElement = e.target.closest('.delete-team-btn');
            deleteTeam(deleteTeamElement);

        });
    }

    for (let button of deleteProjectBtn) {
        button.addEventListener('click', (e) => {
            const deleteProjectElement = e.target.closest('.delete-project-btn');
            deleteProject(deleteProjectElement);
        });
    }
}



function deleteProject(deleteProjectElement) {
    let projectId = deleteProjectElement.getAttribute("data-project_id");
    let projectTitle = deleteProjectElement.getAttribute("data-project_title");
    let deleteProjectModal = new bootstrap.Modal(document.querySelector('#deleteModal'));
    
    let deleteModalLabel = document.getElementById('deleteModalLabel');
    let deleteModalBody = document.getElementById('deleteModalBody');
    let deleteConfirm = document.getElementById('deleteConfirm');
    
    deleteModalBody.innerHTML = `<p>Are you sure you want to delete this <strong>${projectTitle}</strong>?</p><p>This action cannot be undone.</p>`;
    deleteModalLabel.textContent = 'Delete Project?';
    deleteConfirm.href = `delete_project/${projectId}`;
    deleteProjectModal.show();
}


function deleteTeam(deleteTeamElement) {
    let projectId = deleteTeamElement.getAttribute("data-project_id");
    let teamId = deleteTeamElement.getAttribute("data-team_id");
    let teamTitle = deleteTeamElement.getAttribute("data-team_title");
    let deleteTeamModal = new bootstrap.Modal(document.querySelector('#deleteModal'));

    let deleteModalLabel = document.getElementById('deleteModalLabel');
    let deleteModalBody = document.getElementById('deleteModalBody');
    let deleteConfirm = document.getElementById('deleteConfirm');

    deleteModalBody.innerHTML = `<p>Are you sure you want to delete <strong>${teamTitle}</strong> from this project?</p><p>This action cannot be undone.</p>`;
    deleteModalLabel.textContent = 'Delete Team?';
    deleteConfirm.href = `delete_team/${projectId}/${teamId}`;
    deleteTeamModal.show();
}
