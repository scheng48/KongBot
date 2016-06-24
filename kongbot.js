var Discord = require('discord.io');
var cleverbot = require("cleverbot.io");
var PythonShell = require('python-shell');
var cbot = new cleverbot('DdPQ8z69AtZJRyqX','tfQ0SytsE1RXRKxlxRygPXWvK1qN6RWL');
var bot = new Discord.Client({
    token: "MTk0OTY2MzQxNzM0NzYwNDUx.CktoDg.KU5XnWeVDl3bY7D1_XiUfnAwJ5E",
    autorun: true
});

bot.on('ready', function() {
    cbot.setNick("KongBot");
    console.log(bot.username + " - (" + bot.id + ")" + " is now online!");
    bot.setPresence({
        game: "Pokemons Masters"
    });
});

bot.on('message', function(user, userID, channelID, message, event) {
    
    if (message === "ping") {
        bot.sendMessage({
            to: channelID,
            message: "pong"
        });
    }

    if (message.toLowerCase().includes("kongbot,")){
    cbot.create(function (err, session) {
        var lmsg = "";
      	var query = message.replace("KongBot,","");

      	cbot.ask(query, function (err, response) {
      	      lmsg = response,
              bot.sendMessage({
                  to: channelID,
                  message: "@" + user + ": " + lmsg
              });
        	});
    });
    }
    
    if (message.toLowerCase() === "~sortie"){
        var options = {
          mode: 'text',
          pythonPath: 'C:\\Python27\\python.exe',
          scriptPath: 'C:\\Users\\Christopher Kong\\Documents\\KongBot\\KongBot',
          args: ['~sortie']
        };

        PythonShell.run('worldstateparser.py', options, function (err, results) {
          if (err) throw err;
          // results is an array consisting of messages collected during execution
          bot.sendMessage({
                  to: channelID,
                  message: "@" + user + ": " + results.join("")
              });
        });
    }


});