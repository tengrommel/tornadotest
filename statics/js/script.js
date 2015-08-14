/**
 * Created by teng on 15-8-13.
 */
function getCookie(name){
    var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return x ? x[1]:undefined;
}
// 函数getCookie()的作用是得到cookie值，然后将这个值放到向后端post的数据中var pd = {"username":user, "password":pwd, "_xsrf":getCookie("_xsrf")};

jQuery(document).ready(function(){
   $("#login").click(function () {
       // jquery的val()取得该元素的值
       var user = $("#username").val()
       var pwd = $("#password").val()
       // 即将得到的user和pwd值
       var pd = {"username": user, "password":pwd, "_xsrf":getCookie("_xsrf")}
       $.ajax({
           type:"post",
           url:"/",
           data:pd,
           cache:false,
           success: function (data) {
               window.location.href = "/user?user=" +data
           },
           error: function () {
               alert("error!")
           }
       })
   })
})