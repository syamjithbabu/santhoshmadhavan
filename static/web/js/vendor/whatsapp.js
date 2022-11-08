$("#whatsappform").validate({
    submitHandler: function(form) {
        const $form = $("#whatsappform");
  
        const phone = '919605633033';
    
        // get object i.e {key: 'value'} of form
        // let data = {}
        // $form.serializeArray().forEach(v => data[v.name] = v.value)
    
        // make the ?text= payload, 
        // - could use .filter() here too if you dont want empty values
        var name =$('input[name=name]').val()
        var email =$('input[name=email]').val()
        var message =$('#msg').val()
        const text = [
         'Name : ' + name,
         'Email :' +email, 
         'Message : ' +message,


        ].join("\n") // change to what you want sep to be
    
        // make the url
        const action = "https://wa.me/" + phone + "?text=" + encodeURIComponent(text);
        window.location.href=action;

    
        
    }
});