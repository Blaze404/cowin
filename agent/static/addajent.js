var questions = [
    {question:"What's the agents name?"},
    {question:"How much money you put?"},
    {question:"Safety Value?", pattern: "[0-9]+"},
    
  ]
  
  /**********
  
    !!!!!
    New Version: https://codepen.io/arcs/pen/rYXrNQ
    !!!!!
    
    Credits for the design go to XavierCoulombeM
    https://dribbble.com/shots/2510592-Simple-register-form
    
    This Pen uses no libraries except fonts and should 
    work on all modern browsers
    
    The answers are stored in the `questions` array
    with the key `value`. 
  
   **********/
  
  ;(function(){
  
    var tTime = 100  // transition transform time from #register in ms
    var wTime = 200  // transition width time from #register in ms
    var eTime = 1000 // transition width time from inputLabel in ms
  
    // init
    // --------------
    var position = 0
  
    putQuestion()
  
    progressButton.addEventListener('click', validate)
    inputField.addEventListener('keyup', function(e){
      transform(0, 0) // ie hack to redraw
      if(e.keyCode == 13) validate()
    })
  
    // functions
    // --------------
  
    // load the next question
    function putQuestion() {
      inputLabel.innerHTML = questions[position].question
      inputField.value = ''
      inputField.type = questions[position].type || 'text'  
      inputField.focus()
      showCurrent()
    }
    
    // when all the questions have been answered
    function done() {
      
      // remove the box if there is no next question
      register.className = 'close'
      
      // add the h1 at the end with the welcome text
      var h1 = document.createElement('h1')
      h1.appendChild(document.createTextNode('Agent ' + questions[0].value + ' is added!'));
      var br = document.createElement('br');
      var home = document.createElement('a');
      home.href = "/stat/"
      home.innerText = "Home";
    //   home.app
      setTimeout(function() {
        register.parentElement.appendChild(h1);
        register.parentElement.appendChild(br);
        register.parentElement.appendChild(home);     
        setTimeout(function() {h1.style.opacity = 1; home.style.opacity=1;}, 50)
      }, eTime)

      // post the form
      parameters = {}
      names = ["name", "amount", "safety"]
      
      for(var i=0; i<questions.length; i++){
        parameters[names[i]] = questions[i].value;
      }

      path = '/stat/agent/';
      console.log(parameters);
      post(path, parameters);
      
    }
  
    // when submitting the current question
    function validate() {
  
      // set the value of the field into the array
      questions[position].value = inputField.value
  
      // check if the pattern matches
      if (!inputField.value.match(questions[position].pattern || /.+/)) wrong()
      else ok(function() {
        
        // set the progress of the background
        progress.style.width = ++position * 100 / questions.length + 'vw'
  
        // if there is a new question, hide current and load next
        if (questions[position]) hideCurrent(putQuestion)
        else hideCurrent(done)
               
      })
  
    }
  
    // helper
    // --------------
  
    function hideCurrent(callback) {
      inputContainer.style.opacity = 0
      inputProgress.style.transition = 'none'
      inputProgress.style.width = 0
      setTimeout(callback, wTime)
    }
  
    function showCurrent(callback) {
      inputContainer.style.opacity = 1
      inputProgress.style.transition = ''
      inputProgress.style.width = '100%'
      setTimeout(callback, wTime)
    }
  
    function transform(x, y) {
      register.style.transform = 'translate(' + x + 'px ,  ' + y + 'px)'
    }
  
    function ok(callback) {
      register.className = ''
      setTimeout(transform, tTime * 0, 0, 10)
      setTimeout(transform, tTime * 1, 0, 0)
      setTimeout(callback,  tTime * 2)
    }
  
    function wrong(callback) {
      register.className = 'wrong'
      for(var i = 0; i < 6; i++) // shaking motion
        setTimeout(transform, tTime * i, (i%2*2-1)*20, 0)
      setTimeout(transform, tTime * 6, 0, 0)
      setTimeout(callback,  tTime * 7)
    }
  
  }())


function post(path, parameters) {
    var form = $('<form></form>');

    form.attr("method", "post");
    form.attr("action", path);

    $.each(parameters, function(key, value) {
        var field = $('<input></input>');

        field.attr("type", "hidden");
        field.attr("name", key);
        field.attr("value", value);

        form.append(field);
    });

    // The form needs to be a part of the document in
    // order for us to be able to submit it.
    $(document.body).append(form);
    form.submit();
}