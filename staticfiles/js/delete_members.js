const deleteTeamMembersBtn = document.querySelectorAll('#delete-members-btn');


document.addEventListener("DOMContentLoaded", function() {

    initEventListeners();

});

function initEventListeners() {

    for (const button of deleteTeamMembersBtn) {
        button.addEventListener('click', (event) => {
            deleteSelectedMembers(event);
        });
    }
    
}



function deleteSelectedMembers(event) {

    let teamId = event.target.getAttribute("data-team_id");
    let projectId = event.target.getAttribute("data-project_id");

    let selectedMemberIds = [];
    let checkboxes = document.getElementsByName('member_ids');
    
    let projectTeamsModal = bootstrap.Modal.getInstance(document.querySelector('#projectTeamsModal'));
    let deleteTeamMembersModal = new bootstrap.Modal(document.querySelector('#deleteModal'));
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
        return;
    } else {
        projectTeamsModal.hide();
        deleteTeamMembersModal.show();
        deleteModalBody.innerHTML = '<p>Are you sure you want to delete these members?</p><p>This action cannot be undone.</p>';
        deleteModalLabel.textContent = 'Delete Members?';
        deleteConfirm.href = `delete_members/${projectId}/${teamId}/${selectedMemberIds.join(',')}`;

    }
}