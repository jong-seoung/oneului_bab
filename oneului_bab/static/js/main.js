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

window.onload = function() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
    localStorage.removeItem('selectedMenu');
    document.cookie = "FoodList_results=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";
};



// 메뉴 항목 클릭 시 호출되는 함수에서 저장 기능을 추가한다.
$('.result_button').click(function() {
    var paramList = {};
    var result_mune = document.getElementsByClassName('menu-active');
    for (var i = 0; i < result_mune.length; i++) {
        var a = result_mune[i].id;
        paramList[a] = a;
    }

    $.ajax({
        url: '',
        data: paramList,
        method: 'POST',

        success: function(data) {
        location.replace('');
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