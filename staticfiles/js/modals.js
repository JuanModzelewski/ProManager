const deleteTeamMembersBtn = document.querySelectorAll('#delete-members-btn');



for (const button of deleteTeamMembersBtn) {
    button.addEventListener('click', (event) => {
        deleteSelectedMembers(event);
    });
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

document.getElementById('member-search-input').addEventListener('input', function() {
    let button = document.getElementById('edit-team-form-button');
    if (this.value) {
        button.textContent = 'Search and Add';
    } else {
        button.textContent = '{% if request.resolver_match.url_name == "edit_team" %}Update Team{% else %}Create Team{% endif %}';
    }
});