from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = os.environ.get("TOKEN")

# Main Menu
main_menu_keyboard = [
    ["G12 အောင်လက်မှတ်/အမှတ်စာရင်း"],
    ["တက္ကသိုလ်လျှောက်/ကျောင်းအပ်/မေဂျာပြောင်း"],
    ["ဘွဲ့လက်မှတ် နှင့် အမှတ်စာရင်း"],
    ["နိုတြီဘာသာပြန် & တရားရုံးကျမ်းကျိန်လွှာ"],
    ["တက္ကသိုလ်ဝင်စာမေးပွဲ G12 ဖြေဆိုခွင့်လျှောက်ထား"],
    ["ကျောင်းစာအုပ်ဝယ်ယူ/ပို့ဆောင်"]
]

# G12 Submenus
submenu_g12 = [["G12 အောင်လက်မှတ်"], ["G12 အမှတ်စာရင်း"], ["⬅ Back"]]

submenu_g12_certificate = [
    ["အောင်လက်မှတ်ထုတ်ချင်လို့ပါ"],
    ["အောင်လက်မှတ် ဘယ်လောက်ကျမလဲ"],
    ["အောင်လက်မှတ် ဘာတွေလိုအပ်မလဲ"],
    ["အောင်လက်မှတ် ဘယ်လောက်ကြာမလဲ"],
    ["⬅ Back"]
]

submenu_g12_mark = [
    ["အမှတ်စာရင်းထုတ်ချင်ပါတယ်"],
    ["အမှတ်စာရင်း ဘယ်လောက်ကြာမလဲ"],
    ["အမှတ်စာရင်း ဘာတွေလိုအပ်မလဲ"],
    ["⬅ Back"]
]

# တက္ကသိုလ်လျှောက် submenu
submenu_uni = [
    ["တက္ကသိုလ်ဝင်ခွင့်လျှောက်ချင်လို့ပါ"],
    ["တက္ကသိုလ်ဝင်ခွင့်လျှောက်လွှာ ဝန်ဆောင်ခ"],
    ["တက္ကသိုလ်ဝင်ခွင့်လျှောက်လွှာ လိုအပ်ချက်များ"],
    ["⬅ Back"]
]

main_menu = ReplyKeyboardMarkup(main_menu_keyboard, resize_keyboard=True)
g12_menu = ReplyKeyboardMarkup(submenu_g12, resize_keyboard=True)
g12_cert_menu = ReplyKeyboardMarkup(submenu_g12_certificate, resize_keyboard=True)
g12_mark_menu = ReplyKeyboardMarkup(submenu_g12_mark, resize_keyboard=True)
uni_menu = ReplyKeyboardMarkup(submenu_uni, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🙏 မင်္ဂလာပါ၊ MKS Bot မှ ကြိုဆိုပါတယ်။\nမိမိလိုချင်သော Menu ကို ရွေးပါ။",
        reply_markup=main_menu
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📋 Main Menu", reply_markup=main_menu)

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    # Main Menu
    if text == "G12 အောင်လက်မှတ်/အမှတ်စာရင်း":
        await update.message.reply_text("G12 အောင်လက်မှတ်/အမှတ်စာရင်း ကိုရွေးပါ။", reply_markup=g12_menu)
    elif text == "တက္ကသိုလ်လျှောက်/ကျောင်းအပ်/မေဂျာပြောင်း":
        await update.message.reply_text("တက္ကသိုလ်လျှောက်/ကျောင်းအပ်/မေဂျာပြောင်း မီနူး", reply_markup=uni_menu)
    elif text == "ဘွဲ့လက်မှတ် နှင့် အမှတ်စာရင်း":
        await update.message.reply_text("🤗 ဘွဲ့လက်မှတ် နှင့် အမှတ်စာရင်း နှင့် စပ်လျဉ်း၍ အသေးစိတ်သိရှိလိုပါက ဆက်သွယ်ရန်: 09890303270 (Phone/Viber/Telegram)", reply_markup=main_menu)
    elif text == "နိုတြီဘာသာပြန် & တရားရုံးကျမ်းကျိန်လွှာ":
        await update.message.reply_text("🤗 နိုတြီဘာသာပြန် & တရားရုံးကျမ်းကျိန်လွှာ နှင့် စပ်လျဉ်း၍ အသေးစိတ်သိရှိလိုပါက ဆက်သွယ်ရန်: 09890303270 (Phone/Viber/Telegram)", reply_markup=main_menu)
    elif text == "တက္ကသိုလ်ဝင်စာမေးပွဲ G12 ဖြေဆိုခွင့်လျှောက်ထား":
        await update.message.reply_text("🤗 တက္ကသိုလ်ဝင်စာမေးပွဲ G12 ဖြေဆိုခွင့်လျှောက်ထားမှုနှင့် စပ်လျဉ်း၍ အသေးစိတ်သိရှိလိုပါက ဆက်သွယ်ရန်: 09890303270 (Phone/Viber/Telegram)", reply_markup=main_menu)
    elif text == "ကျောင်းစာအုပ်ဝယ်ယူ/ပို့ဆောင်":
        await update.message.reply_text("🤗 ကျောင်းသုံးစာအုပ်ဝယ်ယူ/အရောက်ပို့ဆောင်ပေးခြင်းနှင့် စပ်လျဉ်း၍ အသေးစိတ်သိရှိလိုပါက ဆက်သွယ်ရန်: 09890303270 (Phone/Viber/Telegram)", reply_markup=main_menu)

    # G12 Certificate Menu
    elif text == "G12 အောင်လက်မှတ်":
        await update.message.reply_text("🔰 ဆယ်တန်း G12 အောင်လက်မှတ် မေးခွန်းများ:", reply_markup=g12_cert_menu)
    elif text == "အောင်လက်မှတ်ထုတ်ချင်လို့ပါ":
        await update.message.reply_text("🤗 အရင်ကအောင်လက်မှတ်မူရင်းထုတ်ဘူးလား။ တစ်ခါမှ မထုတ်ရသေးဘူးဆိုရင် မူရင်းထုတ်လို့ရပါတယ်။ မူရင်းထုတ်ပြီးတာ (၆) ကျော်ရင် မိတ္တူ ပြန်လျှောက်လို့ရပါမယ်။", reply_markup=g12_cert_menu)
    elif text == "အောင်လက်မှတ် ဘယ်လောက်ကျမလဲ":
        await update.message.reply_text("🤗 အောင်လက်မှတ်မူရင်း ၁၂,၀၀၀/- (ပို့ခမပါ) ယူပါတယ်။ မူရင်းထုတ်ပြီးသားဖြစ်လို့ မိတ္တူပြန်လျှောက်ပေးရရင် ၂၀,၀၀၀/- (ပို့ခမပါ) ယူပါတယ်။", reply_markup=g12_cert_menu)
    elif text == "အောင်လက်မှတ် ဘာတွေလိုအပ်မလဲ":
        await update.message.reply_text(
            "🤗 လိုအပ်ချက်များ:\n"
            "- အမည်\n- မှတ်ပုံတင်အမှတ်\n- ခုံအမှတ်\n- အောင်မြင်ခဲ့သည့် ခုနှစ်\n- စာစစ်ဌာန\n- ဖခင်အမည်\n- မိခင်အမည်\n- မွေးသက္ကရာဇ်\n\n"
            "📬 ပို့ပေးရမည့်လိပ်စာ အတိအကျ:\n- စာလက်ခံမည့်သူအမည်\n- ဖုန်းနံပါတ်\n- အိမ်အမှတ်\n- လမ်းအမည်\n- ရပ်ကွက်အမည်\n- မြို့နယ်အမည်\n\n"
            "📸 ဓါတ်ပုံရိုက်ပေးပို့ရန်:\n- ဘွဲ့လက်မှတ်ဆိုဒ် အရွယ် ဓါတ်ပုံ\n- နိုင်ငံသားစီစစ်ရေးကဒ်(ရှေ့/နောက်) (သို့) အိမ်ထောင်စုစာရင်း (ရှေ့/နောက်) ပုံ",
            reply_markup=g12_cert_menu
        )
    elif text == "အောင်လက်မှတ် ဘယ်လောက်ကြာမလဲ":
        await update.message.reply_text("🤗 ရုံးဖွင့်ရက် (၁) ရက်၊ (၂) ရက်အတွင်းရပါတယ်။", reply_markup=g12_cert_menu)

    # G12 Mark Menu
    elif text == "G12 အမှတ်စာရင်း":
        await update.message.reply_text("🔰 ဆယ်တန်း G12 အမှတ်စာရင်း မေးခွန်းများ:", reply_markup=g12_mark_menu)
    elif text == "အမှတ်စာရင်းထုတ်ချင်ပါတယ်":
        await update.message.reply_text("🤗 အောင်သည်ဖြစ်စေ၊ ကျရှုံးသည်ဖြစ်စေ အမှတ်စာရင်းလိုသလောက်ထုတ်လို့ရပါတယ်။ (၁) စောင် ၅၀၀၀/- (၅) စောင်အထက်ဆိုရင် ၅၀၀၀/- (ပို့ခမပါ) ယူပါတယ်။", reply_markup=g12_mark_menu)
    elif text == "အမှတ်စာရင်း ဘယ်လောက်ကြာမလဲ":
        await update.message.reply_text("🤗 ရုံးဖွင့်ရက် ၂:၀၀ အတွင်းမှာယူပါက နေ့ခြင်းပြီးရပါတယ်။", reply_markup=g12_mark_menu)
    elif text == "အမှတ်စာရင်း ဘာတွေလိုအပ်မလဲ":
        await update.message.reply_text(
            "🤗 လိုအပ်ချက်များ:\n"
            "- အမည်\n- ခုံအမှတ်\n- အောင်မြင်ခဲ့သည့် ခုနှစ်\n- စာစစ်ဌာန\n- ထုတ်ယူလိုသည့် စောင်ရေ\n\n"
            "📬 ပို့ပေးရမည့်လိပ်စာ အတိအကျ:\n- စာလက်ခံမည့်သူအမည်\n- ဖုန်းနံပါတ်\n- အိမ်အမှတ်\n- လမ်းအမည်\n- ရပ်ကွက်အမည်\n- မြို့နယ်အမည်",
            reply_markup=g12_mark_menu
        )

    # တက္ကသိုလ်လျှောက် submenu
    elif text == "တက္ကသိုလ်ဝင်ခွင့်လျှောက်ချင်လို့ပါ":
        await update.message.reply_text("🤗 ယခင်က တက္ကသိုလ်ဝင်ခွင့်လျှောက် ထားခဲ့ဘူးခြင်းမရှိရင် လျှောက်ပေးလို့ရပါတယ်။", reply_markup=uni_menu)
    elif text == "တက္ကသိုလ်ဝင်ခွင့်လျှောက်လွှာ ဝန်ဆောင်ခ":
        await update.message.reply_text(
            "🤗 တက္ကသိုလ်ဝင်ခွင့်လျှောက်လွှာ တင်ပြီးသည်အထိ ဝန်ဆောင်မှုပေးပါတယ်။\n"
            "ဝန်ဆောင်ခ ၂၀၀၀၀/- (ကျပ်နှစ်သောင်း) ယူပါတယ်။\n"
            "အမှတ်စာရင်းမူရင်းပြပြီး အဆင့်မြင့်ပညာဦးစီးဌာနမှာ တက္ကသိုလ်လျှောက်လွှာ ထုတ်ဘူးလား ဆိုတာ စစ်ဆေးရပါတယ်။\n"
            "ယခင်က တက္ကသိုလ်လျှောက်လွှာ မထုတ်ဘူးမှ လျှောက်လွှာထုတ်လို့ရပါတယ်။\n"
            "အမှတ်စာရင်းမူရင်းကို စာစစ်ဌာနမှာ ထုတ်ရပါတယ်။ အမှတ်စာရင်းထုတ်ခ ထပ်မပေးရပါ။ ဝန်ဆောင်ခထဲမှာ အပြီးအစီးပါပါတယ်။",
            reply_markup=uni_menu
        )
    elif text == "တက္ကသိုလ်ဝင်ခွင့်လျှောက်လွှာ လိုအပ်ချက်များ":
        await update.message.reply_text(
            "🤗 တက္ကသိုလ်ဝင်ခွင့်လျှောက်လွှာအတွက် လိုအပ်ချက်များ:\n"
            "- အမှတ်စာရင်းမူရင်း\n"
            "- ကျောင်းသား၏ ပါ့စ်ပို့ ဓါတ်ပုံ\n"
            "- မှတ်ပုံတင် (ရှေ့/နောက်)\n"
            "- သန်းကောင်စာရင်း (ရှေ့/နောက်)\n"
            "- ခုံအမှတ်\n"
            "- စာစစ်ဌာန\n"
            "- အမှတ်ပေါင်း\n"
            "- အောင်မြင်သည့် ခုနှစ်\n"
            "- လျှောက်ထားလိုသည့် တက္ကသိုလ် / ဘာသာ (ဦးစားပေး အမှတ်စဉ်အလိုက် တန်းစီထည့်သွင်းရန်)\n"
            "- နေ့သင်တန်း / အဝေးသင် ဖော်ပြရန်\n\n"
            "ကျောင်းသား / ဖခင် / မိခင် / ညီ/ အစ်ကို / မောင် / နှမ တစ်ဦးချင်းစီ:\n"
            "- အမည်\n"
            "- မှတ်ပုံတင်အမှတ်\n"
            "- မွေးသက္ကရာဇ်\n"
            "- လူမျိုး\n"
            "- ဘာသာ\n"
            "- အလုပ်အကိုင်\n"
            "- မွေးဖွားရာမြို့နယ်\n"
            "- နေရပ်လိပ်စာ\n"
            "- ဖုန်းနံပါတ်",
            reply_markup=uni_menu
        )

    elif text == "⬅ Back":
        await update.message.reply_text("📋 Main Menu", reply_markup=main_menu)
    else:
        await update.message.reply_text("မိမိလိုချင်သော မီနူးကို ရွေးပါ။", reply_markup=main_menu)

if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("menu", menu))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Bot is running...")
    app.run_polling()
