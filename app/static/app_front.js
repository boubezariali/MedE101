/*
 * Scripting for html pages goes here.
 */
(function() {
    "use strict";
    console.log("in javascript");
    
    
    // fetch json
      fetch('/test')
          .then(function (text) {
              let textBlock = 'GET response text: \n' + text + '\n' + JSON.stringify(text) + '\n';
              document.querySelector("#mylog").textContent = textBlock;
          })
})();