$(document).ready(function () {
  $("#name--input").click(function () {
    let name = $("#name--input").val(); // input 요소에서 key 값을 가져옵니다.

    $.ajax({
      url: "/signUp", // index.py 파일의 경로를 입력해주세요.
      method: "POST", // POST 방식으로 요청을 보냅니다.
      data: { key: name }, // key 값을 서버로 전송합니다.
      success: function (response) {
        // 서버로부터 성공적으로 응답을 받았을 때 실행될 코드를 작성해주세요.
        alert("등록 완료!");
        console.log(response);
      },
      error: function (error) {
        // 서버와의 통신 중 에러가 발생했을 때 실행될 코드를 작성해주세요.
        window.location.href = "error.html"; // 에러가 발생했을 때 error.html 페이지로 이동합니다.
        console.log(error);
      },
    });
  });
});

//이를 사용하려면 Flask 서버에서 '/register' 경로에 대한 POST 요청을 처리하는 코드를 작성해야 합니다.
