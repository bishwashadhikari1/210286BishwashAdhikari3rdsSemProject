
var wws = new WebSocket('wss://stream.binance.com:9443/ws/BTCUSDT@kline_1m');

wws.onmessage = function(e){
    console.log(message.data);
}



