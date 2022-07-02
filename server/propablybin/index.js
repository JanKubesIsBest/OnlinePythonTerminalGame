const express = require('express');
const app = express();
const PORT = 3000
const http = require('http');
const server = http.createServer(app);

const { Server } = require("socket.io");
const io = new Server(server);

app.get('/', (req, res) => {
  res.sendFile(__dirname + "/html/main.html");
});

io.on('connection', (socket) => {
    console.log("User connected")

    socket.on("disconnect", () => {
        console.log("user disconnected")
    })
})

server.listen(PORT, () => {
  console.log('listening on http://localhost:' + PORT);
});