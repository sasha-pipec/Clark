var socket;

function show_profile(current_email, email, photo){
    const current_email_inp = document.getElementById('current_email');
    current_email_inp.value = current_email;
    const email_inp = document.getElementById('email');
    email_inp.value = email;
    const image = document.getElementById('profile_image');
    image.src = photo;
    const email_block = document.getElementById('email_profile');
    email_block.textContent = email;
    const btn = document.getElementById('direct_btn');
    if(current_email!==email){
        btn.style.display = "flex";
        btn.style.margin = "auto";
        btn.style.marginTop = "20px";
    }else{
       btn.style.display = "none";
    }
}

function select_active_item(html_id, item_id, type, workspace_id, item_name, token, email){
    const exit_channel = document.getElementById('exit_channel');
    if(type!=="channel"){
        exit_channel.textContent = " ";
    }else{
        exit_channel.href = exit_channel.href.replace("/0/", "/"+item_id+"/");
        exit_channel.textContent = "выйти";
    }
    const container = document.getElementById('container_main');
    container.style.opacity = 100;
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
                if(user_image==null){
                    user_image = "http://127.0.0.1:8000/static/images/anonim_user.jpg";
                }
                console.log(user_image);
            messages_html+='<div class="message_block">'+
                                '<div class="message_block_left">'+
                                    '<img src="'+user_image+'" alt="" class="message_avatar" onclick="show_profile('+"'"+email+"','"+user_email+"','"+user_image+"'"+')">'+
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
        if(socket instanceof WebSocket){
            socket.close();
        }
        socket = new WebSocket('ws://127.0.0.1:8000/ws/chat/'+type+'_'+item_id);
        socket.onmessage = function (e) {
                const data = JSON.parse(e.data);
                const messages = document.getElementById('messages');
                var photo = data['author_image'];
                if(data['author_image']==null){
                    photo = "http://127.0.0.1:8000/static/images/anonim_user.jpg/";
                }
                messages.innerHTML+='<div class="message_block">'+
                                '<div class="message_block_left">'+
                                    '<img src="'+photo+'" alt="" class="message_avatar">'+
                                '</div>'+
                                '<div class="message_block_right">'+
                                    '<div class="message_info">'+
                                        '<div class="message_author">'+
                                            '<p class="author_name">'+data['author_email']+'</p>'+
                                            '<p class="message_created_at">'+data['created_at']+'</p>'+
                                        '</div>'+
                                        '<div class="message_text">'+
                                            '<p class="message_text_inner">'+
                                                data['text']+
                                            '</p>'+
                                        '</div>'+
                                        '<div class="message_threads">'+
                                        '</div>'+
                                    '</div>'+
                                '</div>'+
                            '</div>';
            };
    })
        .catch(error => {
        console.error('Error during fetch operation:', error);
    });
}

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
        var options = {
              year: 'numeric',
              month: 'long',
              day: 'numeric',
            };
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
            socket.send(JSON.stringify({
                'author_image': data['author']['image'],
                'author_email': data['author']['email'],
                'created_at':new Date(data['created_at']).toLocaleDateString("ru", options),
                'text':data['text']
            }));

        })
            .catch(error => {
            console.error('Error during fetch operation:', error);
        });
        text.value='';
  }
}

function open_channel_popap(){
    const popap = document.getElementById('channel_popap');
    if(popap.classList.contains("vision")){
        popap.classList.remove("vision");
    }else{
        popap.classList.add("vision");
    }
}

function  open_popap(){
    const element = document.getElementById('popap');
     element.style.display = 'flex';
}

function  close_popap(){
    const element = document.getElementById('popap');
     element.style.display = 'none';
}

function get_invite_code(){
    const invite = document.getElementById('invite');
    alert("Код для подключения: "+"http://"+window.location.hostname+":8000"+invite.name);
}