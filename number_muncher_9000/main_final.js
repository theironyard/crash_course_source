var numberButtons   = document.querySelectorAll('.digit');
var operatorButtons = document.querySelectorAll('.op');
var answerArea      = document.getElementById('answer');
var clearButton     = document.querySelector('.clear');
var equalsButton    = document.querySelector('.equals');

var firstNumber;
var operator;

for (var i = 0; i < numberButtons.length; i++) {
  numberButtons[i].addEventListener('click', function(e) {
    
    var newNumberVal = e.target.innerHTML;
    var oldNumberVal = document.getElementById('answer').innerHTML;

    if (answerArea.innerHTML.length < 7) {
      document.getElementById('answer').innerHTML = oldNumberVal+newNumberVal;
    } else {
      alert('Sorry, that number is too big. We can\'t math that hard');
    }
  });
}

for (var i = 0; i < operatorButtons.length; i++) {
  operatorButtons[i].addEventListener('click', function(e) {

    firstNumber = answerArea.innerHTML;
    operator = e.target.innerHTML;
    answerArea.innerHTML = '';
  });
}

clearButton.addEventListener('click', function() {

  answerArea.innerHTML = '';
});

equalsButton.addEventListener('click', function() {

  var answer;

  if (operator === '+') {
    answer = Number(firstNumber) + Number(answerArea.innerHTML);
  } else if (operator === '-') {
    answer = Number(firstNumber) - Number(answerArea.innerHTML);
  } else if (operator === 'x') {
    answer = Number(firstNumber) * Number(answerArea.innerHTML);
  } else {
    answer = Number(firstNumber) / Number(answerArea.innerHTML);
  }

  if (answer > 9999999) {
    answerArea.innerHTML = 'too big';
  } else {
    answerArea.innerHTML = String(answer).slice(0, 7);
  }
});