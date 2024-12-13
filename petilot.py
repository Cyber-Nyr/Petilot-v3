import discord
from discord.ext import commands, tasks
import random
import time

# Configuration du bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Liste de messages amusants aléatoires
fun_messages = [
    "Hé les traders, j'espère que vous respectez vos plans sinon je vais venir m'occuper de vous ! 💼⚡",
    "Trader fatigué = décisions risquées. Dors bien ou je vais te kicker ! 😜",
    "C'est l'heure de faire ta revue de marché, pas de procrastination ! 📈📉",
    "Les émotions ne doivent pas contrôler tes trades, sauf si c'est pour acheter plus de café ! ☕",
    "Un trader qui ne suit pas son plan, c'est comme un bateau sans voile. 🌊",
    "Rappelez-vous : stop-loss, c'est votre meilleur ami, même s'il pique parfois ! ⚠️",
    "Si tu trades après minuit... bonne chance, moi je dors. 😴",
    "Aujourd'hui est un bon jour pour écraser le marché, ou du moins éviter de te faire écraser. 💥",
    "Respecte tes heures de trading, sinon c'est le karma qui va trader pour toi ! 🕒",
    "La patience est une vertu, mais dans le trading, c'est une superpuissance. 🕰️",
    "Chaque bougie a une histoire, mais les tiennes doivent raconter celle du succès ! 🕯️",
    "Si tu ne planifies pas tes trades, tu planifies ton échec. 🛠️",
    "Les bougies rouges ne mordent pas, reste calme et analyse. 🕯️",
    "Les stops, ce n'est pas pour les faibles, c'est pour les sages. 🛑",
    "Tu ne peux pas battre le marché, mais tu peux danser avec lui. 💃",
    "Un trader discipliné est un trader gagnant. 🎯",
    "La prochaine opportunité est toujours à portée de vue, ne force pas les trades. 👀",
    "Le trading, c'est comme le poker : patience et stratégie avant tout. 🃏",
    "Un journal de trading, c'est comme ton GPS : indispensable pour arriver à destination. 📓",
    "Lâche cette souris, va te prendre un café et respire un coup. ☕",
    "Les gains rapides sont souvent suivis de pertes encore plus rapides. Prudence ! ⚡",
    "Si tu perds, ce n'est pas le marché, c'est toi. Analyse et apprends. 📖",
    "Les graphiques ne mentent pas, mais les émotions le font. Reste rationnel. 📊",
    "Un mauvais jour ne définit pas une mauvaise carrière. Reste focus. 🌟",
    "La volatilité, c'est ton alliée, mais seulement si tu sais danser avec elle. 🔥",
    "Trader sans plan, c'est comme naviguer sans boussole. 🧭",
    "Si tu veux gagner gros, apprends à perdre petit. 💡",
    "Les profits aiment la patience, pas la panique. 🐢",
    "Le FOMO (Fear Of Missing Out) est ton pire ennemi. Garde la tête froide. ❄️",
    "Chaque erreur est une leçon déguisée. Accepte-la et avance. 🚀",
    "Un bon trade, c'est un trade planifié, pas un coup de chance. 🎲",
    "Le trading, c'est 10% de stratégie et 90% de discipline. 🧠",
    "Le marché ne dort jamais, mais toi, tu dois le faire. Repose-toi. 🛌",
    "Si le marché te frustre, déconnecte-toi. Tu reviendras plus fort. 💪",
    "Les meilleurs traders ne sont pas ceux qui gagnent le plus, mais ceux qui perdent le moins. ⚖️",
    "Respecte le marché et il te respectera en retour. 🌊",
    "Un bon trader connaît ses limites, un mauvais les teste sans cesse. 🚧",
    "Ne chasse pas les profits, laisse-les venir à toi. 🎣",
    "Une journée sans trade est parfois une excellente journée. 🌅",
    "Les graphiques sont comme des puzzles, assemble-les avec soin. 🧩",
    "La peur et la cupidité sont les pires ennemis d'un trader. Garde l'équilibre. ⚖️",
    "Si tu n'es pas sûr, ne trade pas. L'incertitude coûte cher. 💵",
    "Un trade bien sorti vaut mieux qu'un trade mal tenu. 🏃",
    "Chaque bougie rouge est une opportunité d'achat déguisée. 🕯️",
    "Le marché est patient, sois plus patient que lui. 🐌",
    "Reste curieux, apprends chaque jour et améliore-toi. 🎓",
    "Les outils ne font pas le trader, c'est l'artisan qui compte. 🛠️",
    "La prochaine grande opportunité est toujours à l'horizon. 🌅",
    "Un trader calme est un trader qui gagne. Méditation, ça te dit ? 🧘",
    "Quand tu hésites entre acheter et vendre, fais une pause et réfléchis. 🛑",
    "Les week-ends sont faits pour se reposer, pas pour regretter un trade. 🌞",
    "Un stop trop serré, et tu te fais éjecter avant la fête. 🚀",
    "Si tu trades en colère, tu risques d'amplifier tes pertes. Respire. 🌬️",
    "Chaque trade raté est une leçon. Chaque trade réussi est une validation. ✔️",
    "Ne cours pas après le marché, laisse-le venir à toi. 🐢",
    "Un bon trader sait dire 'non' à un mauvais setup. ❌",
    "La discipline commence par un bon sommeil. 🛌",
    "Un graphique propre donne des idées claires. Garde-le simple. 📉",
    "Les émotions volent des profits. La logique les rapporte. 🧠",
    "Chaque journée de trading est une nouvelle opportunité, pas une revanche. ⏳",
    "Si tu fais toujours les mêmes erreurs, il est temps de changer de stratégie. 🔄",
    "Le trading, c'est un marathon, pas un sprint. 🏃‍♂️",
    "Les rumeurs du marché ne payent pas les factures. Fais confiance à tes analyses. 📊",
    "Un setup parfait n'existe pas. Apprends à gérer l'incertitude. 📐",
    "Les traders impatients payent les traders patients. Sois le second. 🐌",
    "Ton plus grand rival dans le trading, c'est toi-même. 🪞"
]

# ID de l'admin (remplacez par votre ID Discord)
ADMIN_ID = "VOTRE_ID_DISCORD_ICI"

# Événement : quand le bot est prêt
@bot.event
async def on_ready():
    print(f"Bot connecté en tant que {bot.user}")
    daily_greetings.start()
    random_fun_messages.start()
    print("Les tâches planifiées sont activées.")

# Répondre automatiquement aux messages des membres
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignorer les messages du bot lui-même

    if message.content.lower() == "bonjour bot":
        await message.channel.send(f"Bonjour {message.author.name} ! 🌞")
    elif "plan" in message.content.lower():
        await message.channel.send("Plan trading respecté ? Sinon je vais râler ! 😠")

    # Notifier l'admin
    admin = await bot.fetch_user(ADMIN_ID)
    if admin:
        await admin.send(f"{message.author.name} a dit : {message.content}")

    await bot.process_commands(message)  # Permet d'exécuter les commandes

# Tâche quotidienne pour bonjour et bonne nuit
@tasks.loop(minutes=1)
async def daily_greetings():
    current_time = time.strftime("%H:%M")  # Heure actuelle
    channel = discord.utils.get(bot.get_all_channels(), name="général")  # Nom du salon où poster

    if channel:
        if current_time == "08:00":  # Message du matin
            message = random.choice([
                "Bonjour à tous, traders ! Que vos trades soient prospères aujourd'hui ! ☕📈",
                "Réveillez-vous, les marchés n'attendent pas ! Bonne journée à tous ! 🌞📊",
                "Un café dans une main, un plan de trading dans l'autre : bonjour les traders ! ☕🚀",
                "C'est une nouvelle journée pour écraser les graphiques, bon courage à tous ! 🌄📊",
                "Les profits n'attendent pas, en avant les traders ! 🌅💹",
                "Un esprit clair, une stratégie forte : c'est parti pour une journée gagnante ! 💼📈",
                "Préparez vos plans, traders, aujourd'hui on conquiert les marchés ! 🚀💡",
                "Une journée réussie commence avec une bonne préparation. Bonne journée les traders ! 🌟📊",
                "La discipline est clé, mais d'abord un café ! Bon matin les traders ! ☕⚡",
                "Aujourd'hui est un nouveau jour pour faire de grandes choses. Bonne chance à tous ! ✨📈",
                "Chaque bougie compte, alors faites-en une bonne journée ! 🌞📊",
                "Un trader organisé est un trader gagnant. Bon matin à tous ! 📓💡",
                "C'est l'heure de briller sur les marchés, bonne journée à tous ! 🌟📉",
                "Que vos stratégies soient solides et vos gains encore meilleurs. Bonne journée ! 🚀📊",
                "Un nouveau jour, une nouvelle chance d'apprendre et de gagner. Bon matin les traders ! 🎯📈"
            ])
            await channel.send(message)
        elif current_time == "00:00":  # Message du soir
            message = random.choice([
                "Bonne nuit les traders ! Reposez-vous, demain est un nouveau jour pour conquérir les marchés. 🌙✨",
                "Éteignez les écrans, ouvrez les rêves. Bonne nuit à tous ! 💫🛌",
                "Les graphiques attendront demain. Détendez-vous, bonne nuit ! 🕯️🌟",
                "Les rêves sont gratuits, les trades sont risqués : bonne nuit ! 🌌💤",
                "Une bonne nuit de sommeil vaut plus que n'importe quel trade nocturne. 🛌💤",
                "Rechargez vos batteries, demain c'est reparti ! Bonne nuit ! 🌠✨",
                "Un esprit reposé est un esprit gagnant. Bonne nuit les traders ! 🌙💤",
                "Les marchés dorment aussi... ou presque. Prenez soin de vous, bonne nuit ! 🕊️✨",
                "Que vos rêves soient aussi verts que vos trades. Bonne nuit à tous ! 🌟💹",
                "Les profits n'attendent pas les fatigués. Reposez-vous bien ! 🌜📈",
                "Un trader fatigué est un trader risqué. Bonne nuit les champions ! 🛌✨",
                "Les étoiles brillent, tout comme vos idées pour demain. Bonne nuit ! 🌟🚀",
                "Un sommeil réparateur est le secret du succès. Bonne nuit les traders ! 🛏️💡",
                "C'est l'heure de fermer les graphiques et ouvrir les rêves. Bonne nuit à tous ! ✨🌙",
                "Prenez soin de vous ce soir, demain c'est une nouvelle chance de briller. Bonne nuit ! 🌙💫"
            ])
            await channel.send(message)

# Tâche pour envoyer des messages humoristiques aléatoires
@tasks.loop(hours=3)
async def random_fun_messages():
    channel = discord.utils.get(bot.get_all_channels(), name="général")  # Nom du salon où poster

    if channel:
        message = random.choice(fun_messages)
        await channel.send(message)

# Commande fun pour envoyer un message spontané
@bot.command()
async def surprendre(ctx):
    message = random.choice(fun_messages)
    await ctx.send(message)

# Lancer le bot
import os
bot.run(os.getenv("DISCORD_TOKEN"))
