<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>QuickPoll - Instant Feedback Platform</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 50px;
    }

    #poll-container {
      max-width: 400px;
      margin: auto;
      padding: 20px;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    button {
      padding: 10px;
      margin-top: 10px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <div id="poll-container">
    <h2>Create a Quick Poll</h2>
    <label for="question">Question:</label>
    <input type="text" id="question" placeholder="Enter your question">

    <label for="options">Options (comma-separated):</label>
    <input type="text" id="options" placeholder="Option 1, Option 2, ...">

    <button onclick="createPoll()">Create Poll</button>
  </div>

  <script>
    function createPoll() {
      var question = document.getElementById('question').value;
      var options = document.getElementById('options').value.split(',').map(option => option.trim());

      if (!question || options.length < 2) {
        alert('Please enter a valid question and at least two options.');
        return;
      }

      var pollUrl = generatePollUrl(question, options);
      alert('Your poll is created! Share this link: ' + pollUrl);
    }

    function generatePollUrl(question, options) {
      var baseUrl = 'https://example.com/poll?';
      var encodedQuestion = encodeURIComponent(question);
      var encodedOptions = options.map(option => encodeURIComponent(option)).join('&');
      return baseUrl + 'q=' + encodedQuestion + '&' + encodedOptions;
    }
  </script>
</body>
</html>
