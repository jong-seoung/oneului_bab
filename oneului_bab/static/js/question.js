document.addEventListener('DOMContentLoaded', function() {
    const textarea = document.querySelector('#textarea');

    textarea.addEventListener('input', function() {
        this.style.height = 'auto';
        this.style.height = this.scrollHeight + 'px';
    });
});

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

const toggleBtns = document.querySelectorAll(".toggle-btn");

// 각각의 .toggle-btn 요소에 대해 click 이벤트 리스너를 등록합니다.
toggleBtns.forEach((toggleBtn) => {
    toggleBtn.addEventListener("click", () => {
        const accordionHeader = toggleBtn.parentElement;
        
        accordionHeader.classList.toggle("active");
    });
});