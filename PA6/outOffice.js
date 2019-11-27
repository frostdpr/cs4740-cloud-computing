var awsIot = require('aws-iot-device-sdk');// Config
var device = awsIot.device({
   keyPath: "./certs/1944294f1b-private.pem.key",
  certPath: "./certs/1944294f1b-certificate.pem.crt",
    caPath: "./certs/AmazonRootCA1.pem",
      host: "a2oq0mmw1cq24f-ats.iot.us-east-1.amazonaws.com"
});

// Connect
device
  .on('connect', function() {
    console.log('Connected');
// Subscribe to myTopic
    device.subscribe("myTopic");
// Publish to myTopic
    device.publish("myTopic", JSON.stringify({
        status: 'out'
    }));  
  });
