// let user_name = sessionStorage.getItem("name");
let user_points = sessionStorage.getItem("points");
let user_time = sessionStorage.getItem("time");
let total_points = sessionStorage.getItem("total_points");
// document.querySelector("span.name").innerHTML = user_name;
document.querySelector("span.points").innerHTML = user_points;
document.querySelector("span.time_taken").innerHTML = user_time;
document.querySelector("span.total_points").innerHTML = total_points;

if (user_points/total_points * 100 >= 80) {
    document.querySelector("span.conclusion").innerHTML = "Congrats! You Passed! ";
} else {
    document.querySelector("span.conclusion").innerHTML = "Failed! Yor Score is less than 80%! ";
}


