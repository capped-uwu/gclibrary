// Webhook URL
const webhookUrl = 'https://discordapp.com/api/webhooks/1260033305168842783/1kDj09DozGl6YN986QabG10R6JW8aNvlCTSkyBkaIHiKbYHHSyMD_fummVuXDS9DQBtM';

// 送信するデータ
const data = {
    content: 'Injected.'
};

// fetchを使用してWebhookにPOSTリクエストを送信
fetch(webhookUrl, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
})
.then(response => response.json())
.then(data => {
    console.log('Success:', data);
})
.catch((error) => {
    console.error('Error:', error);
});
