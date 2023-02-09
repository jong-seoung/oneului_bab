var g_bSwitch = false;    //페이지 오픈시 물어보기 설정값.[ture:onload시 물어봄.]
        
if( g_bSwitch ) window.onload = fnIconCreate;



function fnIconCreate() {
    if( confirm("바탕화면에 바로가기 아이콘을 만드시겠습니까?") ) {
        var WshShell     = new ActiveXObject("WScript.Shell");
        Desktoptemp      = WshShell.Specialfolders("Desktop");    //path

        var sIconNm      = "오늘의 밥";
        var sName        = WshShell.CreateShortcut(Desktoptemp + "\\" + sIconNm + ".URL");
        sName.TargetPath = "http://127.0.0.1:8000/#";
        sName.Save();
    console('바로가기') 
    }
}
// 메뉴 고르기
function checkSelectAll1(select_menu)  {
    var select = document.getElementsByName("selectall1")[0];

    select_menu.classList.toggle('menu-active');
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