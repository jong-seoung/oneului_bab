// 검색
$('.result_button').click(function(){
    alert("결과값을 출력합니다.");
    let fd = new FormData();
    
    result_mune = document.getElementsByClassName("menu-active");
    for(i=0; i<result_mune.length; i++){
        a = document.getElementsByClassName("menu-active")[i].id;
        fd.append('result_mune_lst',a);
    }

    fd.append('result_length',result_mune.length);
    

    $.ajax({
        url: "",
        data: fd,
        processData: false,
        contentType: false,
        method: "POST",

        success: function (data){
            console.log("성공");
        },
        error: function (request, status, error){
            console.log("에러");
        },
        complete: function (){
            console.log("완료");
        }
    });
});

// 메뉴 고르기
function checkSelectAll1(select_main)  {
    var select = document.getElementsByName("selectall1")[0];

    select_main.classList.toggle('menu-active');
    select.classList.remove('menu-active');
}

function selectAll1(selectall)  {
    for(i = 0; i < 3; i++){
        var select = document.getElementsByName("choice1")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
}

function checkSelectAll2(select_menu)  {
    var select = document.getElementsByName("selectall2")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
}

function selectAll2(selectall)  {
    for(i = 0; i < 3; i++){
        var select = document.getElementsByName("choice2")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
}

function checkSelectAll3(select_menu)  {
    var select = document.getElementsByName("selectall3")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
}

function selectAll3(selectall)  {
    for(i = 0; i < 3; i++){
        var select = document.getElementsByName("choice3")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
}

function checkSelectAll4(select_menu)  {
    var select = document.getElementsByName("selectall4")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
}

function selectAll4(selectall)  {
    for(i = 0; i < 2; i++){
        var select = document.getElementsByName("choice4")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
}

function checkSelectAll5(select_menu)  {
    var select = document.getElementsByName("selectall5")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
}

function selectAll5(selectall)  {
    for(i = 0; i < 2; i++){
        var select = document.getElementsByName("choice5")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
}