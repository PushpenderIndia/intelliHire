let questions = [
  {"id":1, "question":"What is the name of the company that developed Hadoop?", "options": ["a. Yahoo!", "b. Google", "c. Amazon", "d. Facebook"], "answer": "a. Yahoo!" }, 
  {"id":2, "question":"What is the main use for Hadoop?", "options": ["a. To process large data sets in a parallel, distributed computing environment.", "b. To store large data sets in a parallel, distributed file system.", "c. To process and analyze log files from web servers.", "d. To provide a parallel, distributed SQL database."], "answer": "a. To process large data sets in a parallel, distributed computing environment." }, 
  {"id":3, "question":"What is the name of the project that was started to develop Hadoop?", "options": ["a. Nutch", "b. Hbase", "c. Cassandra", "d. Mahout"], "answer": "a. Nutch" }, 
  {"id":4, "question":"What is the main use for Hbase?", "options": ["a. To store large data sets in a parallel, distributed file system.", "b. To process large data sets in a parallel, distributed computing environment.", "c. To provide a parallel, distributed SQL database.", "d. To process and analyze log files from web servers."], "answer": "c. To provide a parallel, distributed SQL database." },
  {"id":5, "question":"What is the main use for Cassandra?", "options": ["a. To store large data sets in a parallel, distributed file system.", "b. To process large data sets in a parallel, distributed computing environment.", "c. To provide a parallel, distributed SQL database.", "d. To process and analyze log files from web servers."], "answer": "a. To store large data sets in a parallel, distributed file system." }];
let question_count = 0;
let points = 0;
let total_points = 0;

window.onload = function () {
  show(question_count);

};

function next() {


  // if the question is last then redirect to final page
  if (question_count == questions.length - 1) {
    sessionStorage.setItem("time", time);
    clearInterval(mytime);
    location.href = "/end_quiz";
  }
  console.log(question_count);

  let user_answer = document.querySelector("li.option.active").innerHTML;
  // check if the answer is right or wrong
  if (user_answer == questions[question_count].answer) {
    points += 10;
    sessionStorage.setItem("points", points);
  }
  total_points += 10;
  sessionStorage.setItem("total_points", total_points);
  console.log(points);

  question_count++;
  show(question_count);
}

function show(count) {
  let question = document.getElementById("questions");
  let [first, second, third, fourth] = questions[count].options;

  question.innerHTML = `
  <h2>Q${count + 1}. ${questions[count].question}</h2>
   <ul class="option_group">
  <li class="option">${first}</li>
  <li class="option">${second}</li>
  <li class="option">${third}</li>
  <li class="option">${fourth}</li>
</ul> 
  `;
  toggleActive();
}

function toggleActive() {
  let option = document.querySelectorAll("li.option");
  for (let i = 0; i < option.length; i++) {
    option[i].onclick = function () {
      for (let i = 0; i < option.length; i++) {
        if (option[i].classList.contains("active")) {
          option[i].classList.remove("active");
        }
      }
      option[i].classList.add("active");
    };
  }
}
