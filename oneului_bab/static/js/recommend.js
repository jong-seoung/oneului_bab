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
    
    if (name && main && soup && spicy && temperature && weight) {
        $.ajax({
            url: '/recommend/',
            data: {
                'name': name,
                'main': main,
                'soup': soup,
                'spicy': spicy,
                'temperature': temperature,
                'weight': weight,
                },
            method: "POST",
    
            success: function (data){
                location.replace("")
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
