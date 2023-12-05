// 가상의 데이터베이스에서 가져온 데이터 예시
let records = [
  { date: "2022-01-01/08:34", name: "홍길동" },
  { date: "2022-01-02/08:11", name: "이순신" },
  { date: "2022-01-03/08:00", name: "강감찬" },
];

// "name"과 "date" 정보만을 포함한 새로운 배열 생성
let newData = records.map(function (record) {
  return {
    name: record.name,
    date: record.date,
  };
});

// tbody 요소 선택
let recordMain = document.getElementById("record--main");

// 데이터를 순회하면서 행(tr)을 생성하여 tbody에 추가
newData.forEach(function (record) {
  // 새로운 행(tr) 요소 생성
  let newRow = document.createElement("tr");

  // 이름(name) 셀(td) 생성
  let nameCell = document.createElement("td");
  nameCell.textContent = record.name;
  newRow.appendChild(nameCell);

  // 날짜(date) 셀(td) 생성
  let dateCell = document.createElement("td");
  dateCell.textContent = record.date;
  newRow.appendChild(dateCell);

  // tbody에 행(tr) 추가
  recordMain.appendChild(newRow);
});
