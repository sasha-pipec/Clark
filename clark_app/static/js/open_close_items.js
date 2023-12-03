function toggleChatList(clickedElement) {
    var chatsList = clickedElement.parentNode;
    var chatItems = chatsList.querySelectorAll('.chat_item');
    var clickedIndex = Array.prototype.indexOf.call(chatItems, clickedElement);

    function toggleItemWithDelay(index) {
        setTimeout(function() {
            if (index !== clickedIndex) {
                chatItems[index].classList.toggle('collapsed');
            }
            if (index < chatItems.length - 1) {
                toggleItemWithDelay(index + 1);
            }
        }, 80);
    }
    toggleItemWithDelay(1);
}