/*
 * Scripting for html pages goes here. Using JQuery.
 */
$(function () {
    "use strict";

    window.addEventListener('load', init);

    function init() {
        console.log('init');
        let submitButton = id("symptom_form");
        // submitButton.addEventListener("submit", passUserInput);
    }

    function passUserInput(evt) {
        evt.preventDefault();
        console.log("passUserInput");
        let inputSymp = id("symptom").value;
        // TODO: Handle error
        console.log(inputSymp);
    }

    // Clinical  features - replace with load CSV
    let availableTags = ["pain", "paralysis", "cough", "fever"];

    // Configure autocomplete for #tags ui-widget
    $('#tags')
        .on("keydown", function (event) {
            if (event.keyCode === $.ui.keyCode.TAB &&
                $(this).autocomplete("instance").menu.active) {
                event.preventDefault();
            }
        })
        .autocomplete({
            minLength: 0,
            source: function (request, response) {
                response($.ui.autocomplete.filter(availableTags, extractLast(request.term)));
            },
            focus: function () {
                return false;
            },
            select: function (event, ui) {
                let terms = split(this.value);
                terms.pop();
                terms.push(ui.item.value);
                terms.push("");
                this.value = terms.join(", ");
                return false;
            }
        });

    // Simple helper functions
    function split(val) {
        return val.split(/, \s*/);
    }

    function extractLast(term) {
        return split(term).pop();
    }

    function id(idName) {
        return document.getElementById(idName);
    }
});
