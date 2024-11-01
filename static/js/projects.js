const deleteTeamBtn = document.querySelectorAll('.delete-team-btn');
const deleteProjectBtn = document.querySelectorAll('.delete-project-btn');
const deleteEpicBtn = document.querySelectorAll('.delete-epic-btn');

document.addEventListener("DOMContentLoaded", function() {

    initEventListeners();

});


function initEventListeners() {

    for (let button of deleteProjectBtn) {
        button.addEventListener('click', (e) => {
            const deleteProjectElement = e.target.closest('.delete-project-btn');
            deleteProject(deleteProjectElement);
        });
    }

    for (let button of deleteTeamBtn) {
        button.addEventListener('click', (e) => {
            const deleteTeamElement = e.target.closest('.delete-team-btn');
            deleteTeam(deleteTeamElement);

        });
    }

    for (let button of deleteEpicBtn) {
        button.addEventListener('click', (e) => {
            const deleteEpicElement = e.target.closest('.delete-epic-btn');
            deleteEpic(deleteEpicElement);
        });
    }

    deleteSelectedMembers();

 
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


function deleteEpic(deleteEpicElement) {
    let projectId = deleteEpicElement.getAttribute("data-project_id");
    let epicId = deleteEpicElement.getAttribute("data-epic_id");
    let epicTitle = deleteEpicElement.getAttribute("data-epic_title");
    let deleteEpicModal = new bootstrap.Modal(document.querySelector('#deleteModal'));

    let deleteModalLabel = document.getElementById('deleteModalLabel');
    let deleteModalBody = document.getElementById('deleteModalBody');
    let deleteConfirm = document.getElementById('deleteConfirm');

    deleteModalBody.innerHTML = `<p>Are you sure you want to delete <strong>${epicTitle}</strong> from this project?</p><p>This action cannot be undone.</p>`;
    deleteModalLabel.textContent = 'Delete Epic?';
    deleteConfirm.href = `delete_epic/${projectId}/${epicId}`;
    deleteEpicModal.show();
}


function deleteSelectedMembers(event) {

    let teamId = event.target.getAttribute("data-team_id");
    let projectId = event.target.getAttribute("data-project_id");

    let selectedMemberIds = [];
    let checkboxes = document.getElementsByName('member_ids');
    
    let projectTeamsModal = bootstrap.Modal.getInstance(document.querySelector('#primaryModal'));
    let deleteTeamMembersModal = new bootstrap.Modal(document.querySelector('#deleteModal'));
    let alertModal = new bootstrap.Modal(document.querySelector('#alertModal'));
    let alertModalClose = document.getElementsByClassName('alert-modal-close');

    let deleteModalLabel = document.getElementById('deleteModalLabel');
    let deleteModalBody = document.getElementById('deleteModalBody');
    let deleteConfirm = document.getElementById('deleteConfirm');

    
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
        return;
    } else if (selectedMemberIds.length === 1) {
        projectTeamsModal.hide();
        deleteTeamMembersModal.show();
        deleteModalBody.innerHTML = '<p>Are you sure you want to delete this member?</p><p>This action cannot be undone.</p>';
        deleteModalLabel.textContent = 'Delete Member?';
        deleteConfirm.href = `delete_member/${projectId}/${teamId}/${selectedMemberIds[0]}`;
    } else {
        projectTeamsModal.hide();
        deleteTeamMembersModal.show();
        deleteModalBody.innerHTML = '<p>Are you sure you want to delete these members?</p><p>This action cannot be undone.</p>';
        deleteModalLabel.textContent = 'Delete Members?';
        deleteConfirm.href = `delete_members/${projectId}/${teamId}/${selectedMemberIds.join(',')}`;

    }
}
