// 요소 선택
const text = document.getElementById('text');
const button = document.getElementById('changeTextButton');

// 버튼 클릭 이벤트 추가
button.addEventListener('click', () => {
  text.textContent = '텍스트가 변경되었습니다!';
});