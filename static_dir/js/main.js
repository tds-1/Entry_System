
(function ($) {
    "use strict";
    // console.log("we are here");
    
    /*==================================================================
    [ Validate ]*/
    var name = $('.validate-input input[name="name"]');
    var phone_number = $('.validate-input input[name="Phone_Number"]');
    var email = $('.validate-input input[name="email"]');

    // var pass = $('.validate-input input[name="pass"]');
    // var cpass = $('.validate-input input[name="cpass"]');


    $('.validate-form').on('submit',function(){
        // console.log("submit vala");
        var check = true;

        if($(name).val().trim() == ''){
            showValidate(name);
            check=false;
        }

        if($(phone_number).val().trim() == ''){
            showValidate(phone_number);
            check=false;
        }

        if($(email).val().trim().match(/^([a-zA-Z0-9_\-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([a-zA-Z0-9\-]+\.)+))([a-zA-Z]{1,5}|[0-9]{1,3})(\]?)$/) == null) {
            showValidate(email);
            check=false;
        }

        // if($(pass).val() !== $(cpass).val()){
        //     showValidate(pass);
        //     check=false;
        // }
        return check;
    });


    $('.validate-form .input1').each(function(){
        $(this).focus(function(){
           hideValidate(this);
       });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).removeClass('alert-validate');
    }
    
    

})(jQuery);