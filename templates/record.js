// 가상의 데이터베이스에서 가져온 데이터 예시
let records = [
  { date: "2022-01-01", fingerprint: "지문1", name: "홍길동" },
  { date: "2022-01-02", fingerprint: "지문2", name: "이순신" },
  { date: "2022-01-03", fingerprint: "지문3", name: "강감찬" },
];

// tbody 요소 선택
let recordMain = document.getElementById("record--main");

// 데이터를 순회하면서 행(tr)을 생성하여 tbody에 추가
records.forEach(function (record) {
  // 새로운 행(tr) 요소 생성
  let newRow = document.createElement("tr");

  // 날짜(date) 셀(td) 생성
  let dateCell = document.createElement("td");
  dateCell.textContent = record.date;
  newRow.appendChild(dateCell);

  // 지문 정보(fingerprint) 셀(td) 생성
  let fingerprintCell = document.createElement("td");
  fingerprintCell.textContent = record.fingerprint;
  newRow.appendChild(fingerprintCell);

  // 이름(name) 셀(td) 생성
  let nameCell = document.createElement("td");
  nameCell.textContent = record.name;
  newRow.appendChild(nameCell);

  // tbody에 행(tr) 추가
  recordMain.appendChild(newRow);
});
