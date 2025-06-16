// bot/index.js
const mineflayer = require('mineflayer')
const axios = require('axios')

const bot = mineflayer.createBot({
  host: 'Rayz-65Vl.aternos.me',
  port: 34392,
  username: 'RayzBot'
})

bot.on('chat', async (username, message) => {
  if (username === bot.username) return
  if (!message.toLowerCase().includes('rayz')) return

  const res = await axios.post('http://localhost:5000/chat', {
    user: username,
    message: message
  })

  bot.chat(res.data.reply)
})

bot.on('login', () => console.log('Rayz has joined!'))
