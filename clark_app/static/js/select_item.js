function select_active_item(html_id, item_id, type, workspace_id, item_name, token){
    const message_type = document.getElementById('message_type');
    message_type.value = type;
    const message_item_id = document.getElementById('message_item_id');
    message_item_id.value = item_id;
    const heade_chat = document.getElementById('header_title');
    heade_chat.textContent = item_name;
    var channels = document.getElementsByClassName('chat_item');
    for (var i = 0; i < channels.length; i++) {
        if (channels[i].id == html_id) {
            channels[i].classList.add('active');
            continue;
        }
        channels[i].classList.remove('active');
    }
    const headers = new Headers();
    headers.append('Content-Type', 'application/json');
    headers.append('Authorization', 'Token '+token+'');
    fetch('http://127.0.0.1:8000/api/messages/?item_id='+item_id+'&type='+type+'&workspace_id='+workspace_id+'',{
        method: 'GET',
        headers: headers,
    })
        .then(response => {
        if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.statusText}`);
        }
        return response.json();
    })
        .then(data => {
        console.log(item_id);
        const messages = document.getElementById('messages');
        var messages_html = "";
        messages.innerHTML = "";
         var options = {
              year: 'numeric',
              month: 'long',
              day: 'numeric',
            };
        data['messages'].forEach(item => {
            var user_image = item['author']['image'];
            var user_email = item['author']['email'];
            var created_at = item['created_at'];
            var text = item['text'];
            messages_html+='<div class="message_block">'+
                                '<div class="message_block_left">'+
                                    '<img src="'+user_image+'" alt="" class="message_avatar">'+
                                '</div>'+
                                '<div class="message_block_right">'+
                                    '<div class="message_info">'+
                                        '<div class="message_author">'+
                                            '<p class="author_name">'+user_email+'</p>'+
                                            '<p class="message_created_at">'+new Date(created_at).toLocaleDateString("ru", options)+'</p>'+
                                        '</div>'+
                                        '<div class="message_text">'+
                                            '<p class="message_text_inner">'+
                                                text+
                                            '</p>'+
                                        '</div>'+
                                        '<div class="message_threads">'+
                                        '</div>'+
                                    '</div>'+
                                '</div>'+
                            '</div>';
        });
        messages.innerHTML = messages_html;
        console.log(messages_html);
    })
        .catch(error => {
        console.error('Error during fetch operation:', error);
    });
}