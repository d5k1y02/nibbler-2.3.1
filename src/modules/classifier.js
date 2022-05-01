"use strict";

let {PythonShell} = require('python-shell')

function classify() {

    let options = {
      mode: 'text',
      pythonOptions: ['-u'], // get print results in real-time
      args: [fenbox.value]
      };
      
let pyshell = new PythonShell('CriteriaPredictor.py', options);

// sends a message to the Python script via stdin
pyshell.send('hello');

pyshell.on('message', function (message) {
  // received a message sent from the Python script (a simple "print" statement)
  pred = parseInt(message)
  console.log(message);
});

    PythonShell.run('CriteriaPredictor.py', options, function (err) {
        if (err) throw err;
        console.log('finished');
      });
}

module.exports = classify;