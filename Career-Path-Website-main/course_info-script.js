/* Toggle the outline */

const showMoreBTN = document.querySelector('.showMoreBTN');
const arrow = document.querySelector('.showMoreBTN i');
const outline = document.querySelector('.outline');

showMoreBTN.addEventListener('click', () => {
    outline.classList.toggle('active');
    if (outline.classList.contains('active')) {
        arrow.style.transform = "rotate(180deg)";
    }
    else {
        arrow.style.transform = "rotate(0deg)";
    }
})

/* Fetching data from JSON file */

const courseName = document.querySelector('.courseName');
const price = document.querySelector('.price');
const field = document.querySelector('.field span');
const learningStyle = document.querySelector('.learningStyle span');
const duration = document.querySelector('.duration span');
const provider = document.querySelector('.provider span');
const courseLink = document.querySelector('.courseLink a');
const lecturesList = document.querySelector('.description .outline .lecturesList');

fetch('Courses.json')
    .then(function (response) {
        return response.json();
    })
    .then(function (data) {
        courseName.innerHTML = data.courses[0].course_name;
        price.innerHTML = data.courses[0].course_price;
        field.innerHTML = data.courses[0].course_field;
        learningStyle.innerHTML = data.courses[0].is_online === true ? 'أونلاين' : 'وجاهي';
        duration.innerHTML = data.courses[0].course_duration;
        provider.innerHTML = data.courses[0].course_provider;
        courseLink.setAttribute('href', data.courses[0].course_url);
        lecturesList.innerHTML = "";
        console.log(data.courses[0].course_description);
        data.courses[0].course_description.forEach((lectureName) => {
            const lectureElement = document.createElement('li');
            lectureElement.innerHTML = lectureName;
            lectureElement.style.lineHeight = '26px';
            lecturesList.appendChild(lectureElement);
        })
    })
    .catch(function (error) {
        console.log('Error fetching JSON: ' + error);
    })