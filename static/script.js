document.addEventListener('DOMContentLoaded', () => {
    const chatDisplay = document.getElementById('chat-display');
    const userQueryInput = document.getElementById('user-query');
    const sendButton = document.getElementById('send-button');

    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
        messageDiv.textContent = text;
        chatDisplay.appendChild(messageDiv);
        chatDisplay.scrollTop = chatDisplay.scrollHeight; // Scroll to bottom
    }

    async function handleSendMessage() {
        const query = userQueryInput.value.trim();
        if (!query) return;

        appendMessage(query, 'user');
        userQueryInput.value = '';

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: query }),
            });

            if (!response.ok) {
                // Try to get error message from backend, or use a generic one
                let errorData;
                try {
                    errorData = await response.json();
                } catch (e) {
                    // Not a JSON error response
                }
                const errorMessage = errorData && errorData.error ? errorData.error : `Error: ${response.status} ${response.statusText}`;
                appendMessage(errorMessage, 'bot');
                console.error('Error sending message:', response.statusText);
                return;
            }

            const data = await response.json();
            appendMessage(data.response, 'bot');

        } catch (error) {
            appendMessage('Failed to connect to the server. Please try again later.', 'bot');
            console.error('Fetch error:', error);
        }
    }

    sendButton.addEventListener('click', handleSendMessage);

    userQueryInput.addEventListener('keypress', (event) => {
        if (event.key === 'Enter') {
            handleSendMessage();
        }
    });
});
