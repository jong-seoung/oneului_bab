document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('#textarea');

    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
});

function submitForm(event) {
    event.preventDefault(); // 기본 동작 방지
    const form = event.target;
    const url = form.action;
    const data = new FormData(form);
    fetch(url, {
        method: 'POST',
        body: data,
    })
    .then(response => {
        if (response.ok) {
            alert('문의가 성공적으로 등록되었습니다.');
        } else {
            throw new Error('문의 등록 중 오류가 발생하였습니다.');
        }
    })
    .catch(error => {
        alert(error.message);
    });
}

const accordionHeaders = document.querySelectorAll('.accordion-header');

accordionHeaders.forEach(header => {
header.addEventListener('click', event => {
    const currentHeader = event.currentTarget;
    const accordionItem = currentHeader.parentElement;
    const accordionContent = accordionItem.querySelector('.accordion-content');
    const toggleBtn = currentHeader.querySelector('.toggle-btn');
    
    accordionItem.classList.toggle('active');
    toggleBtn.classList.toggle('active');
    
    if (accordionItem.classList.contains('active')) {
    accordionContent.style.maxHeight = accordionContent.scrollHeight + 'px';
    } else {
    accordionContent.style.maxHeight = 0;
    }
});
});