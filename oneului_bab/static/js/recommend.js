var input = document.querySelector('#image_uploads');
var preview = document.querySelector('.preview');

input.style.opacity = 0;
input.style.height = 0;

input.addEventListener('change', updateImageDisplay);

function updateImageDisplay() {
    while(preview.firstChild) {
        preview.removeChild(preview.firstChild);
    }

    const curFiles = input.files;
    if(curFiles.length === 0) {
        const para = document.createElement('p');
        para.textContent = '';
        preview.appendChild(para);
    } else {
        const list = document.createElement('ol');
        preview.appendChild(list);

        for(const file of curFiles) {
        const listItem = document.createElement('li');
            if(validFileType(file)) {
                const image = document.createElement('img');
                image.src = URL.createObjectURL(file);

                listItem.appendChild(image);
            } 
        list.appendChild(listItem);
        }
    }
}

const fileTypes = [
    "image/apng",
    "image/bmp",
    "image/gif",
    "image/jpeg",
    "image/pjpeg",
    "image/png",
    "image/svg+xml",
    "image/tiff",
    "image/webp",
    "image/x-icon"
    ];

function validFileType(file) {
    return fileTypes.includes(file.type);
}

function returnFileSize(number) {
    if(number < 1024) {
        return number + 'bytes';
    } else if(number >= 1024 && number < 1048576) {
        return (number/1024).toFixed(1) + 'KB';
    } else if(number >= 1048576) {
        return (number/1048576).toFixed(1) + 'MB';
    }
}

function sendData() {
    var name = document.querySelector('.recommend_name').value;
    var main = document.querySelector('[name=main]').value;
    var soup = document.querySelector('[name=soup]').value;
    var spicy = document.querySelector('[name=Spicy]').value;
    var temperature = document.querySelector('[name=temperature]').value;
    var weight = document.querySelector('[name=weight]').value; 
    let image = document.querySelector('#image_uploads').files[0];

    if (name && main && soup && spicy && temperature && weight) {
        var formData = new FormData();
        formData.append('name', name);
        formData.append('main', main);
        formData.append('soup', soup);
        formData.append('spicy', spicy);
        formData.append('temperature', temperature);
        formData.append('weight', weight);
        formData.append('image', image);


        $.ajax({
            url: '/recommend/',
            data: formData,
            method: "POST",
            processData: false,
            contentType: false,
            success: function (response)    {
                if(response.email === null){
                    alert('로그인이 필요한 기능입니다.');
                    location.replace('user/login');
                }
                else {
                    alert('추천해주셔서 감사합니다.');
                    location.reload();
                }
            },
            error: function (request, status, error){
                console.log("에러");
            },
            complete: function (){
                console.log("완료");
            }
        });
    }
    else if(!name || !main || !soup || !spicy || !temperature || !weight) {
        alert('모든 옵션을 선택해주세요!');
    }
}
