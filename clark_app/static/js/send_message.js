function send_message(event, token){
    if (event.keyCode === 13) {
        event.preventDefault();
        var type = document.getElementById('message_type').value;
        var item_id = document.getElementById('message_item_id').value;
        var text = document.getElementById('text');
        var workspace_id = document.getElementById('workspace_id').value;
        const headers = new Headers();
        headers.append('Content-Type', 'application/json');
        headers.append('Authorization', 'Token '+token+'');
        fetch('http://127.0.0.1:8000/api/messages/', {
            method: 'POST',
            headers: headers,
            body: JSON.stringify({
                "type":type,
                "item_id":item_id,
                "text":text.value,
                "workspace_id":workspace_id,
            })
        })
            .then(response => {
            if (!response.ok) {
                throw new Error(`Network response was not ok: ${response.statusText}`);
            }
            return response.json();
        })
            .then(data => {
            console.log(data);
        })
            .catch(error => {
            console.error('Error during fetch operation:', error);
        });
        text.value='';
  }
}