const form = document.querySelector('.regForm');

form.addEventListener('submit', (event) => {
    event.preventDefault();

    const user_fullname = document.querySelector('.regForm input[name="name"]').value;
    const user_email = document.querySelector('.regForm input[name="email"]').value;
    const user_date_of_birth = document.querySelector('.regForm input[name="date_of_birth"]').value;
    const user_gender = document.querySelectorAll('.regForm input[name="gender"]');
    const user_location = document.querySelector('.regForm input[name="location"]').value;
    const user_major = document.querySelector('.regForm input[name="major"]').value;
    const user_target_field = document.querySelector('.regForm select[name="target_field"]').value;
    const user_graduation_date = document.querySelector('.regForm input[name="graduation_date"]').value;
    const user_years_of_experience = document.querySelector('.regForm input[name="years_of_experience"]').value;
    const submitBTN = document.querySelector('.regForm input[type="submit"]');

    const userData = {};

    userData.name = user_fullname;
    userData.email = user_email;
    userData.date_of_birth = user_date_of_birth;
    userData.location = user_location;
    userData.major = user_major;
    userData.target_field = user_target_field;
    userData.graduation_date = user_graduation_date;
    userData.years_of_experience = parseInt(user_years_of_experience);

    user_gender.forEach((gender) => {
        if (gender.checked) {
            if (gender.id === 'male') {
                userData.gender = "ذكر";
            }
            else {
                userData.gender = "أنثى";
            }
        }
    })

    if (user_target_field === '---') {
        alert('يرجى اختيار المسار الذي ترغب فيه');
        return false;
    }

    console.log(userData);

      
    var headers = new Headers();
    headers.append("Content-Type", "application/json");

    var requestOptions = {
        method: 'POST',
        body: JSON.stringify(userData),
        redirect: 'follow',
        headers: headers
    };
      
    fetch("http://localhost:8000/sign_up", requestOptions)
    .then(() => {
        alert('تم ارفاق معلوماتك بنجاح, يرجى الان الاجابه على الاسئلة التالية');

        const locationPath = window.location.href.split("/");
        locationPath.pop();
        locationPath.push("quiz.html");
        window.location.href = locationPath.join("/");
    })
    .catch(error => console.log('error', error));
})