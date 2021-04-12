/*
 * Scripting for html pages goes here. Using JQuery.
 */
$(function() {
    "use strict";
    console.log("in javascript");

    // Clinical  features - replace with load CSV
    let availableTags = ["pain", "paralysis", "cough", "fever"];

    // Configure autocomplete for #tags ui-widget
    $('#tags')
    .on("keydown", function(event) {
        if (event.keyCode === $.ui.keyCode.TAB && 
            $(this).autocomplete("instance").menu.active) {
            event.preventDefault();
        }
    })
    .autocomplete({
        minLength: 0,
        source: function(request, response) {
            response($.ui.autocomplete.filter(availableTags, extractLast(request.term)));
        },
        focus: function() {
            return false;
        },
        select: function(event, ui) {
            let terms = split(this.value);
            terms.pop();
            terms.push(ui.item.value);
            terms.push("");
            this.value = terms.join(", ");
            return false;
        }
    });
    
    // Fetch json
      fetch('/test')
          .then(function (text) {
              let textBlock = 'GET response text: \n' + text + '\n' + JSON.stringify(text) + '\n';
              document.querySelector("#mylog").textContent = textBlock;
          })

    // Simple helper functions
    function split(val) {
        return val.split(/, \s*/);
    }

    function extractLast(term) {
        return split(term).pop();
    }
});
