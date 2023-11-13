function  open_popap(){
    const element = document.getElementById('popap');
     element.style.display = 'flex';
}

function  close_popap(){
    const element = document.getElementById('popap');
     element.style.display = 'none';
}

function  open_image(){
    const image_input = document.getElementById('image_input').click();
    console.log(image_input);
}

function collect_confirm_code() {
      var inputs = document.getElementsByClassName('confirm_digit_item');
      var concatenatedString = '';
      for (var i = 0; i < inputs.length; i++) {
        concatenatedString += inputs[i].value;
      }
      document.getElementById('confirm_code').value = concatenatedString;
    }