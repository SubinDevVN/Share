let isAFKEnabled = true;
let lastReplyTimes = {};
const cooldownDuration = 30 * 1000;

async function onCall({ message }) {
    const senderID = message.senderID;
    const img = await global.getStream("https://i.pinimg.com/236x/e1/db/0a/e1db0a3e397f47eef24387bd95064732.jpg");
    const content = message.body.toLowerCase();

    if (message.isGroup) {
        return;
    }

    if (content === "-afk") {
        isAFKEnabled = true; 
        message.reply("Chức năng AFK đã được bật!");
    } else if (content === "-unafk") {
        isAFKEnabled = false; 
        message.reply("Chức năng AFK đã được tắt!");
    } else if (isAFKEnabled && (Date.now() - (lastReplyTimes[senderID] || 0) >= cooldownDuration)) {
        lastReplyTimes[senderID] = Date.now();
        message.react("⏳");
        message.reply({
            body: "- - - - - [🌐 Hệ thống 🌐] - - - - -\n➜ Xin lỗi, hiện tại tôi đang bận ~~\n➜ Vui lòng liên hệ tôi thông qua discord @54t3r.4r393ur hoặc https://discord.gg/EZA47mnVdJ\n➜ Tôi sẽ phản hồi tin nhắn của bạn sớm nhất có thể, xin cảm ơn!",
            attachment: img
        });
    }
}

export default {
    onCall
}
