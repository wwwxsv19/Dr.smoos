$(document).ready(function () {
  // 등록 버튼 클릭 이벤트 핸들러
  $("#rebtn").click(function () {
    // 입력한 이름 값 가져오기
    var name = $(".name--input").val();

    // Ajax 요청 생성
    $.ajax({
      url: "/register", // '/register' 경로로 요청
      type: "POST", // POST 방식으로 요청
      data: JSON.stringify({ name: name }), // 요청 데이터 설정
      contentType: "application/json", // 요청 헤더 설정
      success: function (response) {
        // 요청이 성공적으로 완료되면 처리할 코드 작성
        console.log("이름 등록이 완료되었습니다.");
      },
      error: function (xhr, status, error) {
        // 요청이 실패했을 때 처리할 코드 작성
        console.log("이름 등록에 실패했습니다.");
        console.log(error);
      },
    });
  });
});

//이를 사용하려면 Flask 서버에서 '/register' 경로에 대한 POST 요청을 처리하는 코드를 작성해야 합니다.
