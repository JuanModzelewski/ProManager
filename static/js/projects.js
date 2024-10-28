const memberList = document.getElementById('member-list');

document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
})


function initializeEventListeners() {
    closeCreateProjectModal();
    deleteProject();
    deleteSelectedMembers();
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
    const deleteConfirmElement = document.getElementById('deleteConfirm');
    const projectId = event.target.getAttribute("data-project_id");
    deleteConfirmElement.href = `delete_project/${projectId}`;
    event.target.blur();
}

function deleteSelectedMembers(event) {
    const deleteConfirmElement = document.getElementById('deleteMemberConfirm');
    const teamId = event.target.getAttribute("data-team_id");
    const projectId = event.target.getAttribute("data-project_id");
    const selectedMemberIds = [];
    const checkboxes = document.getElementsByName('member_ids');
    const projectTeamsModal = bootstrap.Modal.getInstance(document.querySelector('#projectTeamsModal'));
    const deleteProjectModal = new bootstrap.Modal(document.querySelector('#deleteModal'));
    const alertModal = new bootstrap.Modal(document.querySelector('#alertModal'));
    const alertModalClose = document.getElementsByClassName('alert-modal-close');
    
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
        deleteConfirmElement.href = `delete_members/${projectId}/${teamId}/${selectedMemberIds.join(',')}`;
        console.log(deleteConfirmElement.href);
        event.target.blur();
    }
}