
document.addEventListener('DOMContentLoaded', function() {
    
    initEventlisteners();

})


function initEventlisteners() {

    closeCreateProjectModal()

    deleteProject()
    
}
// Close the modal and redirect to projects page after form is submitted
closeCreateProjectModal()

function closeCreateProjectModal() {
    const projectFormElement = document.querySelector('form');
    projectFormElement.addEventListener('htmx:beforeRequest', (event) => {
        const modalInstance = bootstrap.Modal.getInstance(document.querySelector('#modal'));
        modalInstance.hide();
    });
}

function deleteProject(event) {
    const deleteConfirmElement = document.getElementById('deleteConfirm');
    const projectId = event.target.getAttribute("data-project_id");
    deleteConfirmElement.href = `delete_project/${projectId}`;
    event.target.blur();
}

