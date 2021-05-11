(function(){
    $('html').addClass('js');
    console.log('hello00');
    var contactForm = {
      container: $('#contact'),
      config: {
        effect: 'slideToggle',
        speed: 200
      },
      
      init: function(config){
        $.extend(this.config, config);
        
        $('#c-btn').on('click', this.show);
      },
  
      show: function(){
        var cf = contactForm,
            container = cf.container,
            config = cf.config;
            console.log('displayed');
                      
  
        if(container.is(':hidden')){
          cf.close.call(container);
          container[config.effect]
          (config.speed);
        }
      },
  
      close: function(){
        var $this = $('#contact'); 
        
        if($this.find('span.close').length) return;
  
        $('<span class=close><i class="fas fa-window-close"></i></span>')
          .prependTo(this)
          .on('click', function(){
          $this[contactForm.config.effect](contactForm.config.speed);
        })
      }
    };
  
  contactForm.init({
    effect: 'fadeToggle',
    speed: 200
  });
  console.log(contactForm);
  })();