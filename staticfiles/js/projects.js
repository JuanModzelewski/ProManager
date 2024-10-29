var deleteModalLabel = document.getElementById('deleteModalLabel');
var deleteModalBody = document.getElementById('deleteModalBody');
var deleteConfirm = document.getElementById('deleteConfirm');


var project_id = document.getAttribute("data-project_id");


document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
})


function initializeEventListeners() {
    closeCreateProjectModal();
    deleteProject();
    deleteSelectedMembers();
    deleteTeam();
}
// Close the modal and redirect to projects page after form is submitted
closeCreateProjectModal()

function closeCreateProjectModal() {
    const projectFormElement = document.querySelector('form');
    projectFormElement.addEventListener('htmx:beforeRequest', (event) => {
        const modalInstance = bootstrap.Modal.getInstance(document.querySelector('#projectModal'));
        modalInstance.hide();
    });
}

function deleteProject(event) {
    let projectId = event.target.getAttribute("data-project_id");
    let projectTitle = event.target.getAttribute("data-project_title");

    deleteModalBody.innerHTML = `<p>Are you sure you want to delete this <strong>${projectTitle}</strong>?</p><p>This action cannot be undone.</p>`;
    deleteModalLabel.textContent = 'Delete Project?';
    deleteConfirm.href = `delete_project/${projectId}`;

    event.target.blur();
}

function deleteSelectedMembers(event) {

    let teamId = event.target.getAttribute("data-team_id");
    let projectId = event.target.getAttribute("data-project_id");

    let selectedMemberIds = [];
    let checkboxes = document.getElementsByName('member_ids');
    
    let projectTeamsModal = bootstrap.Modal.getInstance(document.querySelector('#projectTeamsModal'));
    let deleteProjectModal = new bootstrap.Modal(document.querySelector('#deleteModal'));
    let alertModal = new bootstrap.Modal(document.querySelector('#alertModal'));
    let alertModalClose = document.getElementsByClassName('alert-modal-close');

    
    for (let i = 0; i < checkboxes.length; i++) {
        if (checkboxes[i].checked) {
            selectedMemberIds.push(checkboxes[i].value);
        }
    }
    if (selectedMemberIds.length === 0) {
        projectTeamsModal.hide();
        alertModal.show();
        for (let i = 0; i < alertModalClose.length; i++) {
            alertModalClose[i].addEventListener('click', function() {
                alertModal.hide();
                projectTeamsModal.show();
            });
        }
        event.target.blur();
        return;
    } else {
        projectTeamsModal.hide();
        deleteProjectModal.show();
        deleteModalBody.innerHTML = '<p>Are you sure you want to delete these members?</p><p>This action cannot be undone.</p>';
        deleteModalLabel.textContent = 'Delete Members?';
        deleteConfirm.href = `delete_members/${projectId}/${teamId}/${selectedMemberIds.join(',')}`;
        event.target.blur();
    }
}


function deleteTeam(event) {
    let projectId = event.target.getAttribute("data-project_id");
    let teamId = event.target.getAttribute("data-team_id");
    let teamTitle = event.target.getAttribute("data-team_title");
    deleteModalBody.innerHTML = `<p>Are you sure you want to delete this <strong>${teamTitle}</strong>?</p><p>This action cannot be undone.</p>`;
    deleteModalLabel.textContent = 'Delete Team?';
    deleteConfirm.href = `delete_team/${projectId}/${teamId}`;
    event.target.blur();
}