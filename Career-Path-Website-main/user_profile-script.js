/* Defining the Courses Numbers */

const courses = document.querySelectorAll('.course');

courses.forEach((course, index) => {
    if (index > 9) {
        course.setAttribute('data-index', `${index + 1}`);
    }
    else {
        course.setAttribute('data-index', `0${index + 1}`);
    }
})

/* Setting the Courses Descriptions Positions */

const coursesDescs = document.querySelectorAll('.courseDescription');

coursesDescs.forEach((courseDesc, index) => {
    if (index % 2 !== 0) {
        courseDesc.style.right = "75px";
    }

    else {
        courseDesc.style.left = "75px";
    }
});

/* Fetching Courses Details from JSON file */

window.onload = () => {
    const answereQuestionsString = localStorage.getItem("questions");
    if (answereQuestionsString === null) {
        alert('حدث خطأ ما في ادخال معلوماتك سوف يتم ارجاعك لصفحة الامتحان القصير')
        const locationPath = window.location.href.split("/");
        locationPath.pop();
        locationPath.push("quiz.html");
        window.location.href = locationPath.join("/");
        return;
    }
    
    const courseName = document.querySelectorAll('.courseName');
    const coursePrice = document.querySelectorAll('.price');
    const courseLink = document.querySelectorAll('.courseLink a');
    const courseDuration = document.querySelectorAll('.duration span');
    const courseProvider = document.querySelectorAll('.provider span');
    const recommendationText = document.querySelector('.recommendationText p');

    var headers = new Headers();
    headers.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'POST',
        body: answereQuestionsString,
        headers: headers
    };

    console.log('test');
    fetch('http://localhost:8000/generate_career_path', requestOptions)
    .then(response => {console.log('test2'); return response.json(); })
    .then(data => buildPageFromResponse(JSON.parse(data)))
    .catch(error => console.log('error', error));


    function buildPageFromResponse(data) {
        console.log({data});

        data.Path[0].courses.forEach((course, index) => {
            courseName[index].innerHTML = course.name;
            coursePrice[index].innerHTML = course.Price;
            courseLink[index].setAttribute('href', course.link);
            courseDuration[index].innerHTML = course.Duration;
            courseProvider[index].innerHTML = course.Provider;
        })
        recommendationText.innerHTML = data.Path[0].additional_info;
        console.log("I'm here");
    }
}