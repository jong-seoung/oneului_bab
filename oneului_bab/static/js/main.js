// 저장 기능
$(document).ready(function() {
    $(".save").click(function(event){
        let food_id = event.target.attributes.getNamedItem('food_id').value;
        let save_id = event.target.id;
        let save_text = $.trim($('#'+save_id).html());

        $.ajax({
            url: "save",
            data: {
                food_id : food_id,
                save_text : save_text
            },
            method: "POST",

            success: function (response){
                if(response.email === null){
                    alert('로그인이 필요한 기능입니다.');
                    location.replace('/login');
                }
                else{
                    console.log("#save_info_detail_"+response.id);
                    $("#save_info_detail_"+response.id).html(response.save_count+"명이 "+response.name+"을 저장하였습니다.");
                    if (save_text == '저장'){
                        $('#'+save_id).html('저장됨');
                    }else{ 
                        $('#'+save_id).html('저장');
                    }
                }
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

// 이전에 저장한 선택된 항목이 있다면, 그 값을 불러와서 초기화한다.
if (localStorage.selectedMenu) {
    var allElements = document.getElementsByTagName("*");
    for (var i = 0; i < allElements.length; i++) {
        var elem = allElements[i];
        elem.classList.remove('menu-active');
    }
    var selectedIds = JSON.parse(localStorage.selectedMenu);
    for (var id in selectedIds) {
        var elem = document.getElementById(id);
        if (elem) {
        elem.classList.add('menu-active');
        }
    }
}

// 선택한 메뉴 항목의 ID와 이름을 저장한다.
function saveSelectedMenu() {
    var selectedIds = {};
    var selectedMenus = document.getElementsByClassName('menu-active');

    for (var i = 0; i < selectedMenus.length; i++) {
        var id = selectedMenus[i].id;
        selectedIds[id] = id;
    }
    localStorage.selectedMenu = JSON.stringify(selectedIds);
}

// 새로고침시 기능
window.onload = function() {
    window.scrollTo({ top: window.scrollY, behavior: 'smooth' });
    localStorage.removeItem('selectedMenu');
    document.cookie = "random_food_list=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
};


// 메뉴 항목 클릭 시 호출되는 함수에서 저장 기능을 추가한다.
$('.result_button').click(function() {
    var paramList = {};
    var result_menu = document.getElementsByClassName('menu-active');
    for (var i = 0; i < result_menu.length; i++) {
        var a = result_menu[i].id;
        paramList[a] = a;
    }
    paramList["clicked_button_id"] = this.id;

    $.ajax({
        url: '',
        data: paramList,
        method: 'POST',

        success: function(data) {
            window.location.reload(true);
        },
        error: function(request, status, error) {
        console.log('에러');
        },
        complete: function() {
        console.log('완료');
        }
    });

    // 선택한 메뉴 항목을 저장한다.
    saveSelectedMenu();
});

function checkSelectAll(select_menu, name)  {
    var select = document.getElementsByName("selectall" + name)[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
}

function selectAll(selectall, name, count)  {
    for(i = 0; i < count; i++){
        var select = document.getElementsByName("choice" + name)[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
}
