// 이전에 저장한 선택된 항목이 있다면, 그 값을 불러와서 초기화한다.
if (localStorage.selectedMenu) {
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
    localStorage.removeItem('selectedMenu');
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

// 메뉴 항목 선택 시 호출되는 함수에서 저장 기능을 추가한다.
function checkSelectAll1(select_main) {
    var select = document.getElementsByName('selectall1')[0];

    select_main.classList.toggle('menu-active');
    select.classList.remove('menu-active');

    // 선택한 메뉴 항목을 저장한다.
    saveSelectedMenu();
}

function selectAll1(selectall)  {
    for(i = 0; i < 3; i++){
        var select = document.getElementsByName("choice1")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
    saveSelectedMenu();
}

function checkSelectAll2(select_menu)  {
    var select = document.getElementsByName("selectall2")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
    saveSelectedMenu();
}

function selectAll2(selectall)  {
    for(i = 0; i < 3; i++){
        var select = document.getElementsByName("choice2")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
    saveSelectedMenu();
}

function checkSelectAll3(select_menu)  {
    var select = document.getElementsByName("selectall3")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
    saveSelectedMenu();
}

function selectAll3(selectall)  {
    for(i = 0; i < 3; i++){
        var select = document.getElementsByName("choice3")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
    saveSelectedMenu();
}

function checkSelectAll4(select_menu)  {
    var select = document.getElementsByName("selectall4")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
    saveSelectedMenu();
}

function selectAll4(selectall)  {
    for(i = 0; i < 3; i++){
        var select = document.getElementsByName("choice4")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
    saveSelectedMenu();
}

function checkSelectAll5(select_menu)  {
    var select = document.getElementsByName("selectall5")[0];

    select_menu.classList.toggle('menu-active');
    select.classList.remove('menu-active');
    saveSelectedMenu();
}

function selectAll5(selectall)  {
    for(i = 0; i < 2; i++){
        var select = document.getElementsByName("choice5")[i];
        select.classList.remove('menu-active');
    }
    selectall.classList.add('menu-active');
    saveSelectedMenu();
}