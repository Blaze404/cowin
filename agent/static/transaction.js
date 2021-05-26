
function appendUserRow(id, user) {
    var html = "<div id=\"opt-row." + id + "\" class=\"form-group row \">\n" +
        "            <div class=\"col-4 ui-widget\">\n" +
        "                <input required type=\"text\" class=\"form-control tags\" id=\"opt-type." + id + "\" name=\"agent." + id + "\" placeholder=\"Agent\" value=\"" + user.type + "\">\n" +
        "            </div>\n" +
        "            <div class=\"col-4\">\n" +
        "                <input required type=\"text\" class=\"form-control\" id=\"opt-name." + id + "\" name=\"amount." + id + "\" placeholder=\"Amount\" value=\"" + user.name + "\">\n" +
        "            </div>\n" +
     
        "             <button type=\"button\" onclick=\"delRow(" + id + ")\" class=\"btn btn-danger\">Delete</button>\n" +
        "        </div>";
    $("#form-placeholder").append(html);
    // autocompleteF();
    $( function() {
        
        $( ".tags" ).autocomplete({
          source: availableTags,
          change: function(event, ui) {
            if(!ui.item){
                //http://api.jqueryui.com/autocomplete/#event-change -
                // The item selected from the menu, if any. Otherwise the property is null
                //so clear the item for force selection
                $(event.target).val("");
            }
          },
          focus: function (event, ui) {
            return false;
        }

        });
      } );
}

function delRow(id) {
    var element = document.getElementById("opt-row." + id);
    element.parentNode.removeChild(element);
}

$(document).ready(function () {
    var count = 0;
    $("#btn-add").click(function () {
        appendUserRow(count++, {
            type: "",
            name: "",
        })
    });

    $( function() {
       
        $( ".tags" ).autocomplete({
          source: availableTags,
          change: function(event, ui) {
            if(!ui.item){
                //http://api.jqueryui.com/autocomplete/#event-change -
                // The item selected from the menu, if any. Otherwise the property is null
                //so clear the item for force selection
                $(event.target).val("");
            }
          },
          focus: function (event, ui) {
            return false;
            }
        });
      } );

    //   autocompleteF();
});