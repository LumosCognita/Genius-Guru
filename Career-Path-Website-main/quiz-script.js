window.onload = () => {

const main = document.querySelector('main');
const header = document.querySelector('header');

let headerHeight = window.getComputedStyle(header);

main.style.height = `calc(100vh - ${headerHeight.height}px)`;

/* Question Number Counter */



/* Typewriter Effect */

// const typewriters = document.querySelectorAll('.typewriter');
// const delay = 40;

// typewriters.forEach((typewriter) => {
//     const text = typewriter.textContent.trim();
//     typewriter.textContent = "";

//     let i = 0;
//     function typewriterEffect() {
//         if (i < text.length) {
//             typewriter.textContent += text.charAt(i);
//             i++;
//             if (!typewriter.classList.contains('questionText')) {
//                 setTimeout(typewriterEffect, 150);
//             }

//             else {
//                 setTimeout(typewriterEffect, delay);
//             }
//         }
//     }

//     typewriterEffect();
// })

// =========================================================


/* Saving the user choices into a JSON object and setting the counter */

    const answerOptions = document.querySelector('#answerOptions');
    const nextBTN = document.querySelector('.nextBTN');
    let questionNumber = document.querySelector('.questionNumber');
    let counter = 2;

    let questions = [];
    let submittedQuestions = [];
    let questionIndex = 1;

    nextBTN.addEventListener('click', () => {
        const selectedIndex = answerOptions.selectedIndex;
        console.debug({selectedValue: selectedIndex});
        if (selectedIndex === 0) {
            return;
        }

        //Store the answer to prev. question
        submittedQuestions.push({
            ...questions[questionIndex-1], 
            "user_answer": selectedIndex
        });
        console.debug({submittedQuestions});

        if (questionNumber.innerHTML < 15) {
            if (counter < 10) {
                questionNumber.innerHTML = `0${counter}`;
            }

            else {
                questionNumber.innerHTML = `${counter}`;
            }

            counter++;
            changeQuestion();
        }
    })

    const questionText = document.querySelector('.questionText');

    function typingEffect(typewriter) {
        questionText.textContent = "";

        let i = 0;
        function typewriterEffect() {
            if (i < typewriter.length) {
                questionText.textContent += typewriter.charAt(i);
                i++;
                setTimeout(typewriterEffect, 50);
            }
        }

        typewriterEffect();
    }

    function typingEffectAnswers(answersList) {
        const answerSlots = document.querySelectorAll('.answersList li');
        let currentAnswerIndex = 0;
        let currentCharacterIndex = 0;

        answerSlots.forEach((slot) => {
            slot.textContent = "";
        })

        function typewriterEffect() {
            if (currentAnswerIndex < answersList.length) {
                const slotText = answerSlots[currentAnswerIndex];
                const currentAnswer = answersList[currentAnswerIndex];
                const { label } = currentAnswer;

                if (currentCharacterIndex < label.length) {
                    slotText.textContent += label.charAt(currentCharacterIndex);
                    currentCharacterIndex++;
                    setTimeout(typewriterEffect, 25);
                } else {
                    currentAnswerIndex++;
                    currentCharacterIndex = 0;
                    setTimeout(typewriterEffect, 1000); // Wait for 1 second before moving to the next answer
                }
            }
        }

        typewriterEffect(); // Start the typewriter effect
    }

    function changeQuestion() {
        if (questionIndex < questions.length) {
            typingEffect(questions[questionIndex].question);
            typingEffectAnswers(questions[questionIndex].options);
            questionIndex++;
        } else {
            localStorage.setItem("questions", JSON.stringify({"questions": submittedQuestions}));
            const locationPath = window.location.href.split("/");
            locationPath.pop();
            locationPath.push("user_profile.html");
            window.location.href = locationPath.join("/");
        }
    }

    function showTheFirstQuestion() {
        fetch('http://localhost:8000/get_quiz?user_major=SE')
            .then(function (response) {
                return response.json()
            })
            .then(function (data) {
                questions = data.questions;
                console.log({questions});
                if (questionIndex < data.questions.length) {
                    typingEffect(data.questions[0].question);
                    typingEffectAnswers(data.questions[0].options);
                }
                console.log(data.questions[0].options[0].label);
            })
            .catch(function (error) {
                console.error('Failed to fetch quiz:', error);
            })
    }

    showTheFirstQuestion();
};