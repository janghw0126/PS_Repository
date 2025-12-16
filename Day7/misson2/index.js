// app div 선택
const app = document.getElementById('app');

// select 요소 생성
const select = document.createElement('select');
select.id = 'skills';

// option 데이터
const options = [
  { value: 'javascript', text: 'Javascript' },
  { value: 'next', text: 'Next.js' },
  { value: 'react', text: 'React.js' },
  { value: 'typescript', text: 'TypeScript' },
];

// option 생성 후 select에 추가
options.forEach((optionData) => {
  const option = document.createElement('option');
  option.value = optionData.value;
  option.textContent = optionData.text;

  select.appendChild(option);
});

// select를 app에 추가
app.appendChild(select);

// 값 변경 이벤트 추가
select.addEventListener('change', (event) => {
  console.log(event.target.value);
});