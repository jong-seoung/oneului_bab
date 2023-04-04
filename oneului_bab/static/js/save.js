$(document).ready(function() {
    $(".save").click(function(event){
        let food_id = event.target.attributes.getNamedItem('food_id').value;
        let save_id = event.target.id;
        let save_text = $.trim($('#'+save_id).html());
        console.log(1);
        $.ajax({
            url: "",
            data: {
                food_id : food_id,
                save_text : save_text
            },
            method: "POST",

            success: function (response){
                console.log("성공");
                location.reload();
            },
            error: function (request, status, error){
                console.log("에러");
            },
            complete: function (){
                console.log("완료");
            }
        });
    });
});