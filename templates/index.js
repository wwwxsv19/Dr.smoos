// 사용자가 등록되어 있는지 확인하는 변수 'isUserRegistered'를 가정합니다.
// 실제 변수나 메소드로 대체해야 합니다.
let isUserRegistered = true;

// 서버 응답에 따라 적절한 페이지로 리디렉션하는 함수
function redirectToPage() {
  if (isUserRegistered) {
    window.location.href = "registered_user.html";
  } else {
    window.location.href = "registration_user_no.html";
  }
}

// opendoorbtn 버튼에 클릭 이벤트 리스너를 추가합니다.
$(document).ready(function () {
  $("#opendoorbtn").on("click", function () {
    // 버튼이 클릭되었을 때 실행될 코드를 작성합니다.
    // 예시: 가짜 API 호출
    $.ajax({
      url: "/api/checkUserRegistration", // 엔드포인트 URL을 업데이트하세요.
      method: "GET",
      success: function (response) {
        isUserRegistered = response.isRegistered; // 서버에서 'isRegistered' 키로 JSON을 받는다고 가정합니다.
        redirectToPage(); // API 호출이 완료된 후에 리디렉션 함수를 호출합니다.
      },
      error: function (error) {
        console.error("사용자 등록 확인 중 오류가 발생했습니다.", error);
        window.location.href = "error.html";
      },
    });
  });

  // opendoorbtn 버튼이 클릭되었을 때 실행될 코드를 추가합니다.
  $("#opendoorbtn").trigger("click");
});
