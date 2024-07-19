// Webhook URL
const webhookUrl = '%WEBHOOK%';

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
