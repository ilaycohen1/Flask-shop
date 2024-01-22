
function getSecuredDetails(event) {
    
    const user_id = event.currentTarget.getAttribute('data-user-user_id');
    
    fetch(`/admin/users_manager/secured_details/${user_id}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById(`securedDetails${user_id}`).innerHTML = `
                <strong>Password:</strong> ${data.password}<br>
                <strong>Security Question:</strong> ${data.safety_question}<br>
                <strong>Security Answer:</strong> ${data.safety_ans}`;
        }
        )
    }

document.querySelectorAll('.securedDetails').forEach(button => {
button.addEventListener('click', getSecuredDetails)}
)


